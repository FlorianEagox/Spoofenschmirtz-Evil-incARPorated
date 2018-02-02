import UIController
import Net_Utils
try:
    from Tkinter import *
except ImportError:
    from tkinter import *


root = Tk()
ui = UIController.UIController(root)
root.mainloop()


