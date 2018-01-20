from tkinter import *
import tkinter.messagebox


def test():
    print("it works!")


def drawAtMouse(e):
    canvas.create_rectangle(e.x, e.y, e.x+1, e.y+1, fill="black")


root = Tk()

menuBar = Menu(root)
root.config(menu=menuBar)

# ************MenuBar*****************
# Creates the file menu and add the save, new, and exit buttons to it.
fileMenu = Menu(menuBar)
menuBar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="New", command=test)
fileMenu.add_command(label="Save", command=test)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)
# Creates the help menu and adds a help btn
helpMenu = Menu(menuBar)
menuBar.add_cascade(label="Help", menu=helpMenu)

helpMenu.add_command(label="Help Me!!!", command=test)


# **************ToolBar***************
toolBar = Frame(root, bg="blue")
btnInsert = Button(toolBar, text="Image Insert", command=test)
btnInsert.pack(side=LEFT, padx=5, pady=5)
btnPrint = Button(toolBar, text="Print", command=test)
btnPrint.pack(side=LEFT, padx=5, pady=5)
toolBar.pack(side=TOP, fill=X)

# *************STATUS BAR****************
statusBar = Label(root, text="Status", bd=1, relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)

# **********MESSAGE BOXES**********
tkinter.messagebox.showinfo("GLEWP!!!!!", "have you been krewpying your glewp regularly? I don't think you have!!!")
tkinter.messagebox.showwarning("Critical nourishment", "I'm hungry")
tkinter.messagebox.showerror("RED ALERT", "It appears that there's a faggot using this computer")
answer = tkinter.messagebox.askyesno("RED ALERT", "Ready the cannons?")
print(answer)

# ********* CANVASES ************

canvas = Canvas(root, width=200, height=100)
canvas.pack()
canvas.bind("<Motion>", drawAtMouse)

root.mainloop()
