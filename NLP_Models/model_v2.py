```python
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

class EmailNLPModelV2:
    def __init__(self):
        self.model = None
        self.vectorizer = TfidfVectorizer()

    def preprocess(self, data):
        processed_data = self.vectorizer.fit_transform(data)
        return processed_data

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model = make_pipeline(self.vectorizer, SVC(kernel='linear'))
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))

    def predict(self, email):
        processed_email = self.preprocess(email)
        prediction = self.model.predict(processed_email)
        return prediction

    def save_model(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.model, file)

    def load_model(self, filename):
        with open(filename, 'rb') as file:
            self.model = pickle.load(file)
```
