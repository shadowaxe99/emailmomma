```python
from Backend_Services.user_service import UserSchema
from Backend_Services.notification_service import sendNotification

class OnboardingTutorial:
    def __init__(self, user_id):
        self.user_id = user_id
        self.steps = [
            "Welcome to EmailMaster Scheduler!",
            "Let's start by setting up your calendar.",
            "Now, let's connect your email accounts.",
            "Here's how to schedule your first appointment.",
            "You can view your appointments on the dashboard.",
            "Notifications will appear here when you receive new emails.",
            "That's it! You're all set up."
        ]
        self.current_step = 0

    def next_step(self):
        if self.current_step < len(self.steps):
            message = self.steps[self.current_step]
            sendNotification(self.user_id, message)
            self.current_step += 1
        else:
            print("Tutorial completed.")

class FeedbackSurvey:
    def __init__(self, user_id):
        self.user_id = user_id
        self.questions = [
            "How easy was it to set up your account?",
            "How helpful was the onboarding tutorial?",
            "Do you have any suggestions for improving the onboarding process?"
        ]
        self.responses = {}

    def ask_question(self, question_number):
        if question_number < len(self.questions):
            response = input(self.questions[question_number])
            self.responses[question_number] = response
        else:
            print("Survey completed. Thank you for your feedback!")

def start_onboarding(user_id):
    tutorial = OnboardingTutorial(user_id)
    for _ in range(len(tutorial.steps)):
        tutorial.next_step()

    survey = FeedbackSurvey(user_id)
    for i in range(len(survey.questions)):
        survey.ask_question(i)
```