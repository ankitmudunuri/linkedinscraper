from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

path = __file__.replace("scripts\\datainsert.py", "")

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.


def datainsert(datalist, sheetname):
    SPREADSHEET_ID = 'null'
    RANGE_NAME = 'A:E'

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(f'{path}files\\token.json'):
        creds = Credentials.from_authorized_user_file(f'{path}files\\token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                f'{path}files\\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(f'{path}files\\token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()

        value_range_body = {
            'values': datalist
        }
        
        sheet.values().update(
            spreadsheetId=SPREADSHEET_ID,
            valueInputOption="USER_ENTERED",
            range=sheetname + RANGE_NAME,
            body=value_range_body
        ).execute()

    except HttpError as err:
        print(err)