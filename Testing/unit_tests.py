```python
import unittest
from Backend_Services.user_service import UserService
from Backend_Services.email_service import EmailService
from Backend_Services.notification_service import NotificationService
from Backend_Services.analytics_service import AnalyticsService
from Backend_Services.system_health_service import SystemHealthService

class TestEmailMasterScheduler(unittest.TestCase):

    def setUp(self):
        self.user_service = UserService()
        self.email_service = EmailService()
        self.notification_service = NotificationService()
        self.analytics_service = AnalyticsService()
        self.system_health_service = SystemHealthService()

    def test_user_service(self):
        user_id = "test_user"
        self.user_service.add_user(user_id)
        self.assertTrue(self.user_service.user_exists(user_id))
        self.user_service.remove_user(user_id)
        self.assertFalse(self.user_service.user_exists(user_id))

    def test_email_service(self):
        email_id = "test_email"
        self.email_service.add_email(email_id)
        self.assertTrue(self.email_service.email_exists(email_id))
        self.email_service.remove_email(email_id)
        self.assertFalse(self.email_service.email_exists(email_id))

    def test_notification_service(self):
        notification_id = "test_notification"
        self.notification_service.add_notification(notification_id)
        self.assertTrue(self.notification_service.notification_exists(notification_id))
        self.notification_service.remove_notification(notification_id)
        self.assertFalse(self.notification_service.notification_exists(notification_id))

    def test_analytics_service(self):
        user_id = "test_user"
        self.analytics_service.track_user(user_id)
        self.assertTrue(self.analytics_service.user_tracked(user_id))
        self.analytics_service.untrack_user(user_id)
        self.assertFalse(self.analytics_service.user_tracked(user_id))

    def test_system_health_service(self):
        self.assertTrue(self.system_health_service.check_system_health())

if __name__ == '__main__':
    unittest.main()
```