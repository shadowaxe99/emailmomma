```python
import datetime
from collections import Counter
from typing import List, Dict

class AnalyticsService:
    def __init__(self, user_data: Dict, email_data: Dict):
        self.user_data = user_data
        self.email_data = email_data

    def analyze_user_behavior(self, user_id: str) -> Dict:
        user_emails = [email for email in self.email_data if email['user_id'] == user_id]
        email_times = [email['timestamp'] for email in user_emails]
        email_hours = [timestamp.hour for timestamp in email_times]

        # Count the number of emails sent each hour
        email_frequency_by_hour = Counter(email_hours)

        # Find the hour with the most emails sent
        peak_hour = email_frequency_by_hour.most_common(1)[0][0]

        # Count the number of emails sent each day of the week
        email_days = [timestamp.weekday() for timestamp in email_times]
        email_frequency_by_day = Counter(email_days)

        # Find the day with the most emails sent
        peak_day = email_frequency_by_day.most_common(1)[0][0]

        return {
            'peak_hour': peak_hour,
            'peak_day': peak_day,
            'total_emails': len(user_emails)
        }

    def system_health_metrics(self) -> Dict:
        total_users = len(self.user_data)
        total_emails = len(self.email_data)

        # Calculate the average number of emails per user
        avg_emails_per_user = total_emails / total_users if total_users > 0 else 0

        return {
            'total_users': total_users,
            'total_emails': total_emails,
            'avg_emails_per_user': avg_emails_per_user
        }
```