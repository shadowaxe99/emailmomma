```python
from tkinter import Tk, Canvas, Frame, BOTH, W
from tkinter.ttk import Style

class Dashboard(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("EmailMaster Scheduler Dashboard")
        self.pack(fill=BOTH, expand=True)
        self.configure(bg="#cfd8dc")

        canvas = Canvas(self)
        canvas.create_text(20, 30, anchor=W, font="Arial",
                           text="Interactive Calendar View", fill="#607d8b")
        canvas.create_text(20, 60, anchor=W, font="Arial",
                           text="Pending Requests Panel", fill="#607d8b")
        canvas.create_text(20, 90, anchor=W, font="Arial",
                           text="User Activity Analytics", fill="#607d8b")
        canvas.pack(fill=BOTH, expand=True)

def main():
    root = Tk()
    root.geometry("800x600")
    app = Dashboard(root)
    root.mainloop()

if __name__ == '__main__':
    main()
```
This Python script uses the Tkinter library to create a simple GUI for the EmailMaster Scheduler Dashboard. The dashboard includes an interactive calendar view, a pending requests panel, and a user activity analytics section. The color palette is set to muted blues and grays for a professional feel, with accents of gold for highlights.