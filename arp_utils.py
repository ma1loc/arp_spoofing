# ╔══════════════════════════════════════════════════════════════════════════╗
# ║                                                                          ║
# ║             ███╗   ███╗ █████╗  ██╗██╗      ██████╗  ██████╗             ║
# ║             ████╗ ████║██╔══██╗███║██║     ██╔═══██╗██╔════╝             ║
# ║             ██╔████╔██║███████║╚██║██║     ██║   ██║██║                  ║
# ║             ██║╚██╔╝██║██╔══██║ ██║██║     ██║   ██║██║                  ║
# ║             ██║ ╚═╝ ██║██║  ██║ ██║███████╗╚██████╔╝╚██████╗             ║
# ║             ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═╝╚══════╝ ╚═════╝  ╚═════╝             ║
# ║                                                                          ║
# ║    Project: arp_spoofing v1.0.0                                          ║
# ║    Created: 2025-05-22                                                   ║
# ║    Author: ma1loc (youness anflous)                                      ║
# ║                                                                          ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import	os
import	sys
from	scapy.all import ARP, Ether, srp
from	rgb_msg import w_print

def	is_root():
	id = os.geteuid()
	if (id != 0):
		w_print("[!] You must run this script as root", newline=True)
		sys.exit(1)

def	get_mac_addr(ip):
	request = ARP(pdst=ip)
	broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
	packet = broadcast/request
	answered, _ = srp(packet, timeout=1, verbose=False)
	if answered:
		return (answered[0][1].hwsrc)
	return None
