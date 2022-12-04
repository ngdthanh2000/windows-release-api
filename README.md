# windows-release-api
A RESTful API for Windows release information.

## Get all Windows release information
- **Endpoint:** `GET https://windows-release.azurewebsites.net/windows.json`
- **Request parameters**: No.
- **Responses**: an array. Each element contains the information about a Windows product (10/11), its release information URL, and a list of its versions.

| Key                   | Value type               | Description                                                          |
| ---                   |  ---                     |    ---                                                               |
| `windowsName`           | String                   | The name of Windows product                                          |
| `releaseInformationURL` | String                   | Reference link to the Microsoft's official release information       |
| `versions`              | Array of version objects | Released versions of the product                                     |

**The version object structure**
| Key                   | Value type               | Description                                                          |
| ---                   |  ---                     |    ---                                                               |
| `versionName`           | String                   | The name of Windows version                                          |
| `osBuild`               | String                   | The build number associated with the following Windows version (also the prefix of all build numbers under the version)|
| `builds`                | Array of build objects   | Builds under the following version                                    |

**The build object structure**
| Key                   | Value type               | Description                                                          |
| ---                   |  ---                     |    ---                                                               |
| `servicingOption`           | String                   | The servicing options associated with the build, as documented by Microsoft |
| `availabilityDate`               | String of date (yyyy-MM-dd)                 | The release date of the build |
| `build`                | String   | The build number                                |
| `kb` | String | The KB associated with the build |

**Example response**
```json
[
	{
		"windowsName": "Windows 11",
		"releaseInformationURL": "https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information",
		"versions": [
			{
				"versionName": "22H2",
				"osBuild": "22621",
				"builds": [
					{
						"servicingOption": "General Availability Channel",
						"availabilityDate": "2022-11-29",
						"build": "22621.900",
						"kb": "KB5020044"
					}
				]
			}
		]
	}
]
```
