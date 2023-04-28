# Google Drive Direct Download Link Generator

This repository contains a script for generating direct download links for files stored in Google Drive. This script can be used to quickly and easily share files with anyone, without needing to send or store large files.

## Requirements
- Python 3
- Google Drive API credentials

## Setup
1. Create a [Google OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) credentials file and store it as `token.json` in the same directory as the script.
2. Install the required Python packages:

``` bash
pip install -r requirements.txt
```

## Usage
1. Retrieve the file ID for the file you wish to generate a link for.
2. Call the `generate_direct_download_link` function, passing in the file ID as an argument:

``` python
link = generate_direct_download_link('your-file-id-which-you-want-to-install')
print(link)
```

The generated link can now be used to directly download the file. 
