from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

token = ('token.pickle')
creds = pickle.load(token)
service = build('calendar', 'v3', credentials=creds)

page_token = None
while True:
    events = service.events().list(calenderID='primary', pageToken=page_token).execute()
    for event in events['items']:
        print(event['summary'])
    page_token = events.get('nextPageToken')
    if not page_token:
        break
