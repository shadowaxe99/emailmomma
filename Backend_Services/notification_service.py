```python
import uuid
from datetime import datetime
from pytz import timezone

class Notification:
    def __init__(self, user_id, message, priority):
        self.notification_id = str(uuid.uuid4())
        self.user_id = user_id
        self.message = message
        self.priority = priority
        self.timestamp = datetime.now(timezone('UTC'))

    def to_dict(self):
        return {
            "notification_id": self.notification_id,
            "user_id": self.user_id,
            "message": self.message,
            "priority": self.priority,
            "timestamp": self.timestamp.isoformat()
        }

class NotificationService:
    def __init__(self, db):
        self.db = db

    def send_notification(self, user_id, message, priority):
        notification = Notification(user_id, message, priority)
        self.db.insert('notifications', notification.to_dict())

    def get_notifications(self, user_id):
        return self.db.find('notifications', {'user_id': user_id})

    def mark_as_read(self, notification_id):
        self.db.update('notifications', {'notification_id': notification_id}, {'read': True})

    def delete_notification(self, notification_id):
        self.db.delete('notifications', {'notification_id': notification_id})
```