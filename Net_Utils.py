import socket, struct
import subprocess
import re


ipValidator = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

def def_gateway():
	with open("/proc/net/route") as file:
		for line in file:
			fields = line.strip().split()
			if fields[1] != '00000000' or not int(fields[3], 16) & 2:
				continue
				ip = socket.inet_ntoa(struct.pack("<L", int(fields[2], 16))).split(".")
				ip[len(ip) - 1] = '0'
				return str(".".join(ip))


def getHosts():
	arpScanResult = subprocess.check_output("arp-scan -I wlp1s0 -l", shell=True)
	hosts = re.findall(ipValidator, str(arpScanResult))
	return hosts
