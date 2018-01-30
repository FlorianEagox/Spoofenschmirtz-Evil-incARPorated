import UIController as UIC
import Net_Utils
try:
    from Tkinter import *
except ImportError:
    from tkinter import *


print(Net_Utils.getHosts())

root = Tk()
ui = UIC.UIController(root)
root.mainloop()

