```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the webhook events
WEBHOOK_EVENTS = ["NewEmail", "NewAppointment", "NewNotification"]

# Define the webhook endpoints
WEBHOOK_ENDPOINTS = {}

# Function to register a new webhook
@app.route('/webhooks', methods=['POST'])
def register_webhook():
    data = request.get_json()
    event = data.get('event')
    url = data.get('url')

    if event not in WEBHOOK_EVENTS:
        return jsonify({'error': 'Invalid event'}), 400

    if not url:
        return jsonify({'error': 'URL is required'}), 400

    if event not in WEBHOOK_ENDPOINTS:
        WEBHOOK_ENDPOINTS[event] = []

    WEBHOOK_ENDPOINTS[event].append(url)

    return jsonify({'message': 'Webhook registered successfully'}), 201

# Function to trigger a webhook
def trigger_webhook(event, payload):
    if event not in WEBHOOK_ENDPOINTS:
        return

    for url in WEBHOOK_ENDPOINTS[event]:
        requests.post(url, json=payload)

# Function to trigger a NewEmail webhook
def trigger_new_email_webhook(email_id):
    payload = {'email_id': email_id}
    trigger_webhook('NewEmail', payload)

# Function to trigger a NewAppointment webhook
def trigger_new_appointment_webhook(appointment_id):
    payload = {'appointment_id': appointment_id}
    trigger_webhook('NewAppointment', payload)

# Function to trigger a NewNotification webhook
def trigger_new_notification_webhook(notification_id):
    payload = {'notification_id': notification_id}
    trigger_webhook('NewNotification', payload)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
```