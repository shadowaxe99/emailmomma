```python
import pytz
from datetime import datetime

class TimeZoneDatabase:
    def __init__(self):
        self.timezones = pytz.all_timezones

    def get_current_time_in_timezone(self, timezone):
        if timezone not in self.timezones:
            raise ValueError(f"Invalid timezone: {timezone}")
        tz = pytz.timezone(timezone)
        return datetime.now(tz)

    def convert_time_between_timezones(self, time, from_tz, to_tz):
        if from_tz not in self.timezones or to_tz not in self.timezones:
            raise ValueError(f"Invalid timezone(s): {from_tz}, {to_tz}")
        from_tz = pytz.timezone(from_tz)
        to_tz = pytz.timezone(to_tz)
        return time.replace(tzinfo=from_tz).astimezone(to_tz)

timezone_database = TimeZoneDatabase()
```