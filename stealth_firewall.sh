#!/bin/bash
# CONTRACT: incoming_packet -> silent_drop -> zero_response
# Purpose: Stealth "Black-Hole" firewall to make Node 29 invisible to scans.

# 1. Flush existing rules
iptables -F

# 2. Set Default Policies to DROP (Everything is forbidden unless allowed)
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# 3. Allow Loopback (Internal system talk)
iptables -A INPUT -i lo -j ACCEPT

# 4. Allow Established Connections (Only talk back to those we started)
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# 5. The "Sovereign Port" (Allow Mesh Gossip on our specific LoRa/UDP port)
iptables -A INPUT -p udp --dport 10470 -j ACCEPT

# 6. LOG and SILENT DROP (Don't send 'Reset' packets, just vanish)
iptables -A INPUT -j DROP

echo "[🛡️ FIREWALL] Node 29 is now in Stealth Mode. Invisible to Nmap and Port Scans."
