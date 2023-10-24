```python
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

class EmailClassifierModelV1:
    def __init__(self):
        self.model = Pipeline([
            ('vectorizer', CountVectorizer()),
            ('nb', MultinomialNB())
        ])

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))

    def predict(self, email_text):
        return self.model.predict([email_text])

    def save_model(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.model, file)

    def load_model(self, filename):
        with open(filename, 'rb') as file:
            self.model = pickle.load(file)

# Example usage:
# email_model = EmailClassifierModelV1()
# email_model.train(X, y)  # X and y are your training data
# email_model.save_model('model_v1.pkl')
# email_model.load_model('model_v1.pkl')
# email_model.predict("Schedule a meeting with John Doe tomorrow at 10 AM")
```