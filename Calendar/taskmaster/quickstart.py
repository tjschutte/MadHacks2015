from datetime import datetime
import os

from apiclient.discovery import build
from httplib2 import Http
import oauth2client
from oauth2client import client
from oauth2client import tools
from .models import Event


SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Calendar API Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-api-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print 'Storing credentials to ' + credential_path
    return credentials

def GetEvents():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    service = build('calendar', 'v3', http=credentials.authorize(Http()))

    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print 'Getting the upcoming 10 events'
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=100, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    toReturn = []
    for e in events:
        toAdd = Event(startDate = datetime.strptime(e['start'].get('dateTime', e['start'].get('date'))[0:10], '%Y-%M-%d'), title= e['summary'])
        toReturn.append(toAdd)
        print toAdd.startDate.date()
    return toReturn

def newGetEvents():
    user = User.Objects.filter(username = 'Tom')
    storage = Storage(CredentialsModel, 'id', user, 'credential')
    credential = storage.get()


##
##def main():
##    """Shows basic usage of the Google Calendar API.
##
##    Creates a Google Calendar API service object and outputs a list of the next
##    10 events on the user's calendar.
##    """
##    credentials = get_credentials()
##    service = build('calendar', 'v3', http=credentials.authorize(Http()))
##
##    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
##    print 'Getting the upcoming 10 events'
##    eventsResult = service.events().list(
##        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
##        orderBy='startTime').execute()
##    events = eventsResult.get('items', [])
##
##    if not events:
##        print 'No upcoming events found.'
##    for event in events:
##        start = event['start'].get('dateTime', event['start'].get('date'))
##        print start, event['summary']
##if __name__ == '__main__':
##    main()

