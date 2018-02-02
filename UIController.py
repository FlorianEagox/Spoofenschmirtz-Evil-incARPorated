import Net_Utils
import Net_Controller
import subprocess
from Host import Host

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

        self.btnHostScan = Button(self.toolBar, text="Host Scan", command=self.displayHosts)
        self.btnHostScan.pack(side=LEFT, padx=5, pady=5)

        self.btnPickInt = Button(self.toolBar, text="Choose Interface", command=self.chooseInterface)
        self.btnPickInt.pack(side=LEFT)

        self.toolBar.pack(side=TOP, fill=X)

        # *************SIDE PANEL****************

        self.sidePanel = Frame(root, width=120, bg="white", relief=SUNKEN)
        self.sidePanel.pack(fill=Y, side=LEFT)
        self.lbxHosts = Listbox(self.sidePanel)
        self.lbxHosts.pack(fill=Y, side=LEFT)
        self.lbxHosts.bind("<Button-3>", self.doubleClickListItem)
        # *************STATUS BAR****************
        self.statusBar = Label(root, text="Status", bd=1, relief=SUNKEN, anchor=W)
        self.statusBar.pack(side=BOTTOM, fill=X)
        root.tk.call('tk', 'scaling', 2.0)

    def displayHosts(self):
        Net_Controller.hosts.clear()
        self.lbxHosts.delete(0, END)
        for host in Net_Utils.getHosts():
            print(host)
            #Net_Controller.hosts.insert(END, Host(host))
            self.lbxHosts.insert(END, host)

    def doubleClickListItem(self):
        print(self.lbxHosts.curselection())

    def chooseInterface(self):
        win = Tk()
        lblPrompt = Label(win, text="Choose a network interface device")
        lblPrompt.pack()
        lbxInts = Listbox(win)
        for intf in subprocess.check_output("ifconfig | sed 's/[ \t].*//;/^\(lo\|\)$/d'", shell=True).splitlines():
            lbxInts.insert(END, intf)
        lbxInts.pack()
        btnSelect = Button(win, text="Select", command=lambda: (lbxInts.get(lbxInts.curselection()),
                                                                 win.destroy()))
        btnSelect.pack(side=RIGHT)
        win.mainloop()
