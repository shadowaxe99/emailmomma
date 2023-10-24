```python
import pytz
from datetime import datetime

class TimeZoneConversion:
    def __init__(self):
        self.utc = pytz.UTC

    def convert_to_utc(self, local_time, local_tz):
        """
        Convert local time to UTC time
        """
        local_tz = pytz.timezone(local_tz)
        local_time = local_tz.localize(local_time)
        utc_time = local_time.astimezone(self.utc)
        return utc_time

    def convert_from_utc(self, utc_time, target_tz):
        """
        Convert UTC time to target timezone
        """
        target_tz = pytz.timezone(target_tz)
        target_time = utc_time.astimezone(target_tz)
        return target_time

    def convert_between_tz(self, local_time, local_tz, target_tz):
        """
        Convert time from one timezone to another
        """
        utc_time = self.convert_to_utc(local_time, local_tz)
        target_time = self.convert_from_utc(utc_time, target_tz)
        return target_time

if __name__ == "__main__":
    tz_converter = TimeZoneConversion()
    local_time = datetime.now()
    local_tz = "America/New_York"
    target_tz = "Asia/Kolkata"
    converted_time = tz_converter.convert_between_tz(local_time, local_tz, target_tz)
    print(f"Time in {target_tz} is {converted_time}")
```