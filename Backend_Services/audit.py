```python
import os
from zapv2 import ZAPv2

class AuditService:
    def __init__(self):
        self.zap = ZAPv2(apikey=os.getenv('ZAP_API_KEY'))

    def start_audit(self, target_url):
        """
        Start the audit process for the given target URL.
        """
        # Start the spider
        self.zap.spider.scan(target_url)

        # Progress monitoring
        while int(self.zap.spider.status) < 100:
            # Poll the status
            print('Spider progress %: {}'.format(self.zap.spider.status))
            time.sleep(2)

        print('Spider completed')

        # Start the active scan
        self.zap.ascan.scan(target_url)

        # Progress monitoring
        while int(self.zap.ascan.status) < 100:
            # Poll the status
            print('Scan progress %: {}'.format(self.zap.ascan.status))
            time.sleep(5)

        print('Scan completed')

        # Report the results
        print('Hosts: {}'.format(', '.join(self.zap.core.hosts)))
        print('Alerts: ')
        print(self.zap.core.alerts())

    def conduct_audit(self):
        """
        Conduct the audit process for the EmailMaster Scheduler.
        """
        target_url = os.getenv('TARGET_URL')
        self.start_audit(target_url)

audit_service = AuditService()
audit_service.conduct_audit()
```