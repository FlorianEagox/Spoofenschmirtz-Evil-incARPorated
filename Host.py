import os
from tkinter import messagebox

class Host:
    def __init__(self, ip):
        self.ip = ip


    def ping(self):
        messagebox.showinfo("Ping Result", "Host is up!" if os.system("ping -c 1 " + self.ip) == 0 else "Host is down =(")


