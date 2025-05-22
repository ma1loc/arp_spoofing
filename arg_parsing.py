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

import	argparse
import	re

def is_valid_ip(ip):
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    if re.match(pattern, ip):
        parts = ip.split(".")
        return all(0 <= int(part) <= 255 for part in parts)
    return False

def arg_parsing():
    parser = argparse.ArgumentParser(description="ARP Spoofing Script")
    
    parser.add_argument("-t", "--target", required=True, help="IP address of the target/victim to spoof")
    parser.add_argument("-r", "--router", required=True, help="IP address of the router (gateway)")
    
    return parser.parse_args()
