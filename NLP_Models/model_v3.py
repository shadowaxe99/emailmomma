```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.callbacks import ModelCheckpoint
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd

class NLPModelV3:
    def __init__(self, data_path):
        self.data_path = data_path
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def load_data(self):
        df = pd.read_csv(self.data_path)
        X = df['text']
        y = df['label']

        label_encoder = LabelEncoder()
        y = label_encoder.fit_transform(y)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.X_train = np.array(X_train)
        self.X_test = np.array(X_test)
        self.y_train = np.array(y_train)
        self.y_test = np.array(y_test)

    def build_model(self):
        self.model = Sequential()
        self.model.add(LSTM(128, input_shape=(self.X_train.shape[1:]), activation='relu', return_sequences=True))
        self.model.add(Dropout(0.2))

        self.model.add(LSTM(128, activation='relu'))
        self.model.add(Dropout(0.2))

        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dropout(0.2))

        self.model.add(Dense(10, activation='softmax'))

    def compile_model(self):
        self.model.compile(loss='sparse_categorical_crossentropy',
                           optimizer='adam',
                           metrics=['accuracy'])

    def train_model(self):
        checkpoint = ModelCheckpoint('model_v3.h5', monitor='val_loss', verbose=1, save_best_only=True, mode='min')
        callbacks_list = [checkpoint]

        self.model.fit(self.X_train,
                       self.y_train,
                       batch_size=64,
                       epochs=10,
                       validation_data=(self.X_test, self.y_test),
                       callbacks=callbacks_list)

    def evaluate_model(self):
        loss, accuracy = self.model.evaluate(self.X_test, self.y_test)
        print(f'Loss: {loss}, Accuracy: {accuracy}')

    def process(self):
        self.load_data()
        self.build_model()
        self.compile_model()
        self.train_model()
        self.evaluate_model()

if __name__ == "__main__":
    model_v3 = NLPModelV3('data.csv')
    model_v3.process()
```