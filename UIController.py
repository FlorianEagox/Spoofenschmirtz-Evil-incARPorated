try:
    from Tkinter import *
except ImportError:
    from tkinter import *


def test():
    print("it works!")


class UIController:

    def __init__(self, root):
        self.menuBar = Menu(root)
        root.config(menu=self.menuBar)

        # ************MenuBar*****************
        # Creates the file menu and add the save, new, and exit buttons to it.
        self.fileMenu = Menu(self.menuBar)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)

        self.fileMenu.add_command(label="New", command=test)
        self.fileMenu.add_command(label="Save", command=test)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=root.quit)
        # Creates the help menu and adds a help btn
        self.helpMenu = Menu(self.menuBar)
        self.menuBar.add_cascade(label="Help", menu=self.helpMenu)

        self.helpMenu.add_command(label="Help Me!!!", command=test)

        # **************ToolBar***************

        self.toolBar = Frame(root, bg="blue")
        self.btnInsert = Button(self.toolBar, text="Image Insert", command=test)
        self.btnInsert.pack(side=LEFT, padx=5, pady=5)
        self.btnPrint = Button(self.toolBar, text="Print", command=test)
        self.btnPrint.pack(side=LEFT, padx=5, pady=5)
        self.toolBar.pack(side=TOP, fill=X)

        # *************SIDE PANEL****************

        self.sidePanel = Frame(root, width=120, bg="white", relief=SUNKEN)
        self.sidePanel.pack(fill=Y, side=LEFT)
        self.lbxHosts = Listbox(self.sidePanel)
        self.lbxHosts.pack()

        self.lbxHosts.insert(END, "Lol")

        # *************STATUS BAR****************

        self.statusBar = Label(root, text="Status", bd=1, relief=SUNKEN, anchor=W)
        self.statusBar.pack(side=BOTTOM, fill=X)
