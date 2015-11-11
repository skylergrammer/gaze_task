from gaze_task import Task
import tkinter as tk
from datetime import datetime


root = tk.Tk()
task = Task(root, ['red.png', 'blue.jpg'], n_iters=100, height=400, width=400)
task.start()
root.mainloop()
