import tkinter as tk
from subject import Subject
from observer import ConcreteObserver
from tkinter import scrolledtext

class App:
    def __init__(self, root):
        self.subject = Subject()

        self.output_label = tk.Label(root, text="", fg="red")
        self.output_label.pack()

        self.observer1 = ConcreteObserver("Observer 1", self.output_label, self)
        self.observer2 = ConcreteObserver("Observer 2", self.output_label, self)
        self.subject.attach(self.observer1)
        self.subject.attach(self.observer2)

        self.label = tk.Label(root, text="Enter new state:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Update State", command=self.update_state)
        self.button.pack()
        
        self.log_text = scrolledtext.ScrolledText(root, width=40, height=10)
        self.log_text.pack()
        

    def update_state(self):
        state = int(self.entry.get())
        self.subject.set_state(state)
        self.output_label.config(text=f"State updated to: {state}")
    
    def log_to_console(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.yview(tk.END)