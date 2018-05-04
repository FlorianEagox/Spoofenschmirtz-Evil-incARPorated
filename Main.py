# Program Entry Point
import UIController
import subprocess

try:
    from Tkinter import *
except ImportError:
    from tkinter import * #python2
subprocess.call(['./arpsetup.sh'])
# Launch an instance of the UI
root = Tk()
ui = UIController.UIController(root)
root.mainloop()
