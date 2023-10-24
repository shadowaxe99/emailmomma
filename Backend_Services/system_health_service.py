```python
import psutil
import time
from datetime import datetime

class SystemHealthService:
    def __init__(self):
        self.start_time = time.time()

    def get_system_uptime(self):
        uptime = time.time() - self.start_time
        return str(datetime.timedelta(seconds=uptime))

    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self):
        memory = psutil.virtual_memory()
        return memory.percent

    def get_disk_usage(self):
        disk = psutil.disk_usage('/')
        return disk.percent

    def monitor_system_health(self):
        while True:
            print("System Uptime: ", self.get_system_uptime())
            print("CPU Usage: ", self.get_cpu_usage())
            print("Memory Usage: ", self.get_memory_usage())
            print("Disk Usage: ", self.get_disk_usage())
            time.sleep(60)

if __name__ == "__main__":
    system_health_service = SystemHealthService()
    system_health_service.monitor_system_health()
```