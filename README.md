# ARP Spoofing Tool
A Python-based tool for performing ARP spoofing attacks on local networks for penetration testing and educational purposes.

## Features
- **Bidirectional Spoofing**: Intercepts traffic between target and gateway by spoofing both directions
- **Automatic MAC Resolution**: Automatically discovers MAC addresses of target and router
- **Network Restoration**: Restores legitimate ARP entries when the attack is stopped
- **IP Validation**: Validates input IP addresses to ensure proper format
- **Colorized Output**: Uses color-coded terminal messages for better readability
- **Graceful Exit**: Handles interruption signals and properly restores network state

## Prerequisites
- Python 3.x
- Root/Administrator privileges (required for raw packet operations)
- Linux/Unix operating system (recommended for best compatibility)

## Installation
1. Clone the repository or download the source code
2. Install the required dependencies:
```bash
pip install scapy
```

## Project Structure
```
arp_spoofing/
├── arp.py              # ARP spoofing and restoration functions
├── arp_spoofing.py     # Main entry point for the application
├── arp_utils.py        # Utility functions (root check, MAC resolution)
├── arg_parsing.py      # Command-line argument parsing
├── rgb_msg.py          # Colored output functions
└── README.md
6 files
```

## Usage
### Basic Usage
Perform ARP spoofing between a target and router:
```bash
sudo python arp_spoofing.py -t 192.168.1.100 -r 192.168.1.1
```

### Using Long Form Arguments
```bash
sudo python arp_spoofing.py --target 192.168.1.100 --router 192.168.1.1
```

## Command Line Arguments
| Argument | Long Form | Description |
|----------|-----------|-------------|
| `-t` | `--target` | IP address of the target/victim to spoof (required) |
| `-r` | `--router` | IP address of the router/gateway (required) |

## Output Format
The tool displays real-time packet information:
```
[+] packet_send -> 1
[+] packet_send -> 2
[+] packet_send -> 3
...
```

When stopped with Ctrl+C:
```
^C
[*] Restoring network...
[+] Quit
```

## How It Works
1. The tool resolves MAC addresses for both target and router using ARP requests
2. Sends crafted ARP responses to both target and router:
   - Tells the target that the attacker's MAC address belongs to the router
   - Tells the router that the attacker's MAC address belongs to the target
3. All traffic between target and router is redirected through the attacker's machine
4. On exit, sends legitimate ARP responses to restore normal network communication

## Security and Ethical Use
This tool is intended for authorized penetration testing and educational purposes only. Please ensure you have explicit written permission before testing on any network. Unauthorized use of this tool may be illegal and unethical.

## Troubleshooting
### Common Issues
- **"You must run this script as root"**: The application requires root privileges to send raw packets
- **"Failed to get MAC for [IP]"**: The target IP address is unreachable or not responding to ARP requests
- **"IPs format not valid"**: One or both IP addresses are not in valid IPv4 format

### Debug Steps
1. Verify target and router IPs are reachable with `ping`
2. Check current ARP table with `arp -a`
3. Ensure you're on the same network segment as the targets
4. Verify network interface is active and properly configured

## Contributing
Contributions are welcome for educational improvements! Please feel free to submit a Pull Request.
