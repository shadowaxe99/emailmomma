```python
import random
from typing import List
from Backend_Services.user_service import UserSchema

class ChatbotSupport:
    def __init__(self):
        self.responses = {
            "greeting": ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Greetings! How can I help you?"],
            "farewell": ["Goodbye! Have a great day!", "Bye! Feel free to ask if you have more questions.", "Farewell! Don't hesitate to reach out if you need anything."],
            "unknown": ["I'm sorry, I didn't understand that. Could you please rephrase?", "I'm not sure I understand. Could you clarify?", "Apologies, but I'm having trouble understanding. Could you rephrase that?"]
        }

    def provide_support(self, user_id: str, message: str) -> str:
        """
        Function to provide in-app support.
        """
        user = UserSchema.get_user(user_id)
        if not user:
            return "User not found."

        if "hello" in message.lower() or "hi" in message.lower() or "hey" in message.lower():
            return random.choice(self.responses["greeting"])
        elif "bye" in message.lower() or "goodbye" in message.lower() or "farewell" in message.lower():
            return random.choice(self.responses["farewell"])
        else:
            return random.choice(self.responses["unknown"])
```
