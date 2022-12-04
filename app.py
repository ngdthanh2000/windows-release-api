from flask import Flask
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

@app.route("/")
def home():
    return "Up"

@app.route("/windows.json")
def parser():
    WIN_11_URL = 'https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information'
    WIN_10_URL = 'https://learn.microsoft.com/en-us/windows/release-health/release-information'
    win_11 = parse(WIN_11_URL, 'Windows 11', 1)
    win_10 = parse(WIN_10_URL, 'Windows 10', 2)
    return [win_11, win_10]

def parse(uri, windows_name, num_skipped_table = 0):
    result = {'windowsName': windows_name, 'releaseInformationURL': uri}
    request = requests.get(uri)
    versions = parse_versions(request.text, num_skipped_table)
    result['versions'] = versions
    return result

def parse_versions(text, num_skipped_table):
    versions = []
    soup = BeautifulSoup(text, 'html.parser')
    for table in soup.find_all('table')[num_skipped_table:]:
        title_ele = table.find_previous_sibling('strong')
        if (title_ele is None):
            title_ele = table.find_previous_sibling('summary')
        regex_res = re.search(r"Version (\S+).*\(OS build (\d+)\).*", title_ele.text)
        version_txt = regex_res.group(1)
        build_txt = regex_res.group(2)
        version_dict = {"versionName": version_txt, "osBuild": build_txt}
        builds = []
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            build = {}
            build['servicingOption'] = cols[0].text
            build['availabilityDate'] = cols[1].text
            build['build'] = cols[2].text
            build['kb'] = cols[3].text
            builds.append(build)
        version_dict['builds'] = builds
        versions.append(version_dict)
    return versions