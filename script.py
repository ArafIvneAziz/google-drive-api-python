import os.path
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Set up credentials
creds = None
if os.path.exists('token.json'):
    with open('token.json') as f:
        creds = Credentials.from_authorized_user_info(json.load(f))

# Set up Google Drive API
service = build('drive', 'v3', credentials=creds)

# Function to generate direct download link for a file
def generate_direct_download_link(file_id):
    file = service.files().get(fileId=file_id, fields='webContentLink').execute()
    return file['webContentLink'].replace('view', 'uc')

# Usage example
link = generate_direct_download_link('14bVqz0FpiF5LPiYFtvlC6lwchQaeJDnt')
print(link)
