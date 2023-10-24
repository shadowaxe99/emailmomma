```python
import matplotlib.pyplot as plt
import pandas as pd
from Backend_Services.analytics_service import analyzeUserBehavior

class DataVisualizationService:
    def __init__(self):
        self.user_behavior_data = None

    def fetch_user_behavior_data(self, user_id):
        self.user_behavior_data = analyzeUserBehavior(user_id)

    def create_interactive_chart(self, user_id):
        self.fetch_user_behavior_data(user_id)

        df = pd.DataFrame(self.user_behavior_data)
        df.plot(kind='bar', x='time', y='frequency', title='User Scheduling Patterns')

        plt.show()

    def export_user_behavior_data(self, user_id, file_format='csv'):
        self.fetch_user_behavior_data(user_id)

        df = pd.DataFrame(self.user_behavior_data)

        if file_format == 'csv':
            df.to_csv(f'user_{user_id}_behavior_data.csv')
        elif file_format == 'xlsx':
            df.to_excel(f'user_{user_id}_behavior_data.xlsx')
        else:
            print("Invalid file format. Please choose either 'csv' or 'xlsx'.")

data_visualization_service = DataVisualizationService()
```
