```python
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google_account():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def create_google_calendar_service():
    creds = authenticate_google_account()
    service = build('calendar', 'v3', credentials=creds)
    return service

def add_event_to_google_calendar(user_id, appointment_id, start_time, end_time, summary, description, location):
    service = create_google_calendar_service()
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'attendees': [
            {'email': user_id},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"Event created: {event.get('htmlLink')}")
    return event.get('id')

def delete_event_from_google_calendar(user_id, appointment_id):
    service = create_google_calendar_service()
    service.events().delete(calendarId='primary', eventId=appointment_id).execute()
    print(f"Event deleted: {appointment_id}")

def update_event_in_google_calendar(user_id, appointment_id, start_time, end_time, summary, description, location):
    service = create_google_calendar_service()
    event = service.events().get(calendarId='primary', eventId=appointment_id).execute()

    event['summary'] = summary
    event['location'] = location
    event['description'] = description
    event['start']['dateTime'] = start_time.isoformat()
    event['end']['dateTime'] = end_time.isoformat()

    updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()
    print(f"Event updated: {updated_event.get('htmlLink')}")
    return updated_event.get('id')
```