```python
import datetime
from Backend_Services.notification_service import sendNotification

class Webinar:
    def __init__(self, title, description, date_time, duration):
        self.title = title
        self.description = description
        self.date_time = date_time
        self.duration = duration
        self.participants = []

    def add_participant(self, user_id):
        self.participants.append(user_id)
        sendNotification(user_id, f"You have been added to the webinar: {self.title}")

    def remove_participant(self, user_id):
        self.participants.remove(user_id)
        sendNotification(user_id, f"You have been removed from the webinar: {self.title}")

    def get_details(self):
        return {
            "title": self.title,
            "description": self.description,
            "date_time": self.date_time.strftime("%m/%d/%Y, %H:%M:%S"),
            "duration": self.duration,
            "participants": self.participants
        }

def hostWebinar(title, description, date_time, duration):
    webinar = Webinar(title, description, date_time, duration)
    return webinar
```