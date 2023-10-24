```python
import unittest
from Backend_Services.user_service import UserService
from Backend_Services.email_service import EmailService
from Backend_Services.notification_service import NotificationService
from Backend_Services.analytics_service import AnalyticsService
from Backend_Services.system_health_service import SystemHealthService

class IntegrationTests(unittest.TestCase):

    def setUp(self):
        self.user_service = UserService()
        self.email_service = EmailService()
        self.notification_service = NotificationService()
        self.analytics_service = AnalyticsService()
        self.system_health_service = SystemHealthService()

    def test_user_email_integration(self):
        user_id = "test_user"
        email_id = "test_email"
        self.user_service.create_user(user_id)
        self.email_service.send_email(email_id, user_id)
        user_emails = self.user_service.get_user_emails(user_id)
        self.assertIn(email_id, user_emails)

    def test_email_notification_integration(self):
        email_id = "test_email"
        notification_id = "test_notification"
        self.email_service.send_email(email_id)
        self.notification_service.create_notification(notification_id, email_id)
        email_notifications = self.email_service.get_email_notifications(email_id)
        self.assertIn(notification_id, email_notifications)

    def test_user_analytics_integration(self):
        user_id = "test_user"
        self.user_service.create_user(user_id)
        self.analytics_service.track_user_activity(user_id, "login")
        user_activity = self.analytics_service.get_user_activity(user_id)
        self.assertIn("login", user_activity)

    def test_system_health_integration(self):
        self.system_health_service.monitor_system_load()
        self.system_health_service.monitor_system_latency()
        system_health = self.system_health_service.get_system_health()
        self.assertIn("load", system_health)
        self.assertIn("latency", system_health)

if __name__ == "__main__":
    unittest.main()
```