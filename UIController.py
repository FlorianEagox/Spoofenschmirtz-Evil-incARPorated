import Net_Utils
import Net_Controller
import subprocess
import gi.repository
from WebRenderer import WebRenderer
from Host import Host
import webbrowser
import threading
import time
import keyboard
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

# Try importing TKinter from Python3, otherwise, use the Python2 version.
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from WebRenderer import WebRenderer

# PlaceHolder Function
def test(event):
    print("it works!")


class UIController:
    def __init__(self, root):
        self.menuBar = Menu(root)
        root.config(menu=self.menuBar)
        # root.tk.call('tk', 'scaling', 2.0)

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

        # **************TOOL BAR***************

        self.toolBar = Frame(root, bg="blue")

        self.btnHostScan = Button(self.toolBar, text="Host Scan", command=self.displayHosts)
        self.btnHostScan.pack(side=LEFT, padx=5, pady=5)

        self.btnPickInt = Button(self.toolBar, text="Choose Interface", command=self.chooseInterface)
        self.btnPickInt.pack(side=LEFT)

        self.btnArpSpoof = Button(self.toolBar, text="ARP Spoof", command=self.runSpoof)
        self.btnArpSpoof.pack(side=RIGHT, padx=5)

        self.btnViewContet = Button(self.toolBar, text="View", command=self.view)
        self.btnViewContet.pack(side=RIGHT)

        self.toolBar.pack(side=TOP, fill=X)

        self.midSection = Frame(root)

        # *************SIDE PANEL****************

        self.sidePanel = Frame(self.midSection, width=120, bg="white", relief=SUNKEN)
        self.sidePanel.pack(fill=Y, side=LEFT)
        self.lbxHosts = Listbox(self.sidePanel)
        self.lbxHosts.pack(fill=Y, side=LEFT)
        self.lbxHosts.bind("<Double-Button-1>", self.doubleClickListItem)

        # *************WEB VIEW******************

        self.webFrameHolder = Frame(self.midSection, width=600, height=400)
        self.webFrameHolder.pack(after=self.sidePanel)
        self.midSection.pack()

        # **********SSL STRIP OUTPUT*****************
        self.txtOut = Text(root)
        self.txtOut.pack(fill=X, after=self.midSection)

        # *************STATUS BAR****************
        self.statusBar = Label(root, text="Status", bd=1, relief=SUNKEN, anchor=W)
        self.statusBar.pack(after=self.txtOut, side=BOTTOM, fill=X)

        # **********DELETE THIS!!!!!!***************
        threading.Thread(target=self.pThread).start()

    def pThread(self):
        lock = threading.Lock()
        while lock:
            if Net_Controller.isSpoofRunning:
                try:  # used try so that if user pressed other than the given key error will not be shown
                    if keyboard.is_pressed('q'):  # if key 'q' is pressed
                        self.txtOut.insert(INSERT, open("html", 'r').read())
                        time.sleep(0.5)
                    elif keyboard.is_pressed('b'):
                        self.txtOut.insert(INSERT, open("post", 'r').read())
                        time.sleep(0.5)
                except:
                    break  # if user pressed a key other than the given key the loop will break

    def view(self):
        open("/home/seth/outPut.html", "w").write(self.txtOut.get("1.0", END))
        web = WebRenderer(self)
        GObject.threads_init()
        Gtk.main()
    def displayHosts(self):
        Net_Controller.hosts.clear()
        self.lbxHosts.delete(0, END)
        for host in Net_Utils.getHosts():
            print(host)
            Net_Controller.hosts.insert(len(Net_Controller.hosts), Host(host))
            self.lbxHosts.insert(END, host)

    def chooseInterface(self):
        win = Tk()
        lblPrompt = Label(win, text="Choose a network interface device")
        lblPrompt.pack()
        lbxInts = Listbox(win)
        for intf in subprocess.check_output(Net_Utils.interface_finder, shell=True).splitlines():
            lbxInts.insert(END, intf)
        lbxInts.pack()
        btnSelect = Button(win, text="Select", command=lambda: (lbxInts.get(lbxInts.curselection()),
                                                                win.destroy()))
        btnSelect.pack(side=RIGHT)
        win.mainloop()

    def doubleClickListItem(self, event):
        win = Tk()
        selectedHost = self.lbxHosts.get(self.lbxHosts.curselection())
        host = None
        for h in Net_Controller.hosts:
            if h.ip == selectedHost:
                host = h

        lblIP = Label(win, text="IP: " + host.ip)
        lblIP.pack()
        btnPing = Button(win, text="Ping", command=host.ping)
        btnPing.pack()
        win.mainloop()

    def runSpoof(self):
        Net_Utils.spoof(self, self.lbxHosts.get(self.lbxHosts.curselection()))
