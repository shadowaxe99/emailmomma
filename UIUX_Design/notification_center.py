```python
import tkinter as tk
from tkinter import ttk
from Backend_Services.notification_service import get_notifications

class NotificationCenter(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        self.parent.title("Notification Center")
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.config(background="lavender")

        # Define the different GUI widgets
        self.notification_label = ttk.Label(self.parent, text="Notifications:")
        self.notification_label.grid(row=0, column=0, sticky=tk.W)

        self.notification_tree = ttk.Treeview(self.parent)
        self.notification_tree.grid(row=1, column=0, sticky='nsew')
        self.notification_tree.heading('#0', text='Notification ID')
        self.notification_tree['columns'] = ('Priority', 'Message', 'Read')
        self.notification_tree.heading('Priority', text='Priority')
        self.notification_tree.heading('Message', text='Message')
        self.notification_tree.heading('Read', text='Read')

        # Populate the treeview with notifications
        self.populate_notification_tree()

    def populate_notification_tree(self):
        notifications = get_notifications()
        for notification in notifications:
            read_status = 'Read' if notification['read'] else 'Unread'
            self.notification_tree.insert('', 'end', text=notification['notification_id'],
                                          values=(notification['priority'], notification['message'], read_status))

def run_notification_center():
    root = tk.Tk()
    NotificationCenter(root)
    root.mainloop()

if __name__ == "__main__":
    run_notification_center()
```