# windows-release-api
A RESTful API for Windows release information.

## Get all Windows release information
- **Endpoint:** `GET https://windows-release.azurewebsites.net/windows.json`
- **Request parameters**: No.
- **Responses**: an array. Each element contains the information about a Windows product (10/11), its release information URL, and a list of its versions.

| Key                   | Value type               | Description                                                          |
---                     ---                        ---
| windowsName           | String                   | The name of Windows product                                          |
| releaseInformationURL | String                   | Reference link to the Microsoft's official release information       |
| versions              | Array of version objects | Released versions of the product                                     |
