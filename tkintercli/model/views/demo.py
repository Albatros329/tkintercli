import tkinter as tk
from tkintercli import controller as get_controller

class Demo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = get_controller
        
        tk.Label(self, text="Hello world !").pack()
