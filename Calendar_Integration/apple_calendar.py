```python
import requests
from icalendar import Calendar, Event
from datetime import datetime
from pytz import timezone

class AppleCalendarIntegration:
    def __init__(self, user_id):
        self.user_id = user_id
        self.calendar_url = f"https://www.icloud.com/calendar/{self.user_id}"

    def get_appointments(self):
        response = requests.get(self.calendar_url)
        calendar = Calendar.from_ical(response.text)
        appointments = []
        for component in calendar.walk():
            if component.name == "VEVENT":
                appointments.append({
                    'summary': component.get('summary'),
                    'start': component.get('dtstart').dt,
                    'end': component.get('dtend').dt,
                    'location': component.get('location'),
                    'description': component.get('description')
                })
        return appointments

    def create_appointment(self, appointment):
        event = Event()
        event.add('summary', appointment['summary'])
        event.add('dtstart', datetime.strptime(appointment['start'], "%Y-%m-%dT%H:%M:%S%z"))
        event.add('dtend', datetime.strptime(appointment['end'], "%Y-%m-%dT%H:%M:%S%z"))
        event.add('location', appointment['location'])
        event.add('description', appointment['description'])
        calendar = Calendar()
        calendar.add_component(event)
        response = requests.post(self.calendar_url, data=calendar.to_ical())
        return response.status_code == 200

    def delete_appointment(self, appointment_id):
        response = requests.delete(f"{self.calendar_url}/{appointment_id}")
        return response.status_code == 200
```