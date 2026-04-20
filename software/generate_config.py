import os
import subprocess

def generate_sovereign_keys():
    print("[SYSTEM] 🔑 GENERATING SOVEREIGN ENCRYPTION KEYS...")
    # In a real Linux environment, we use 'wg genkey'
    # For now, we create placeholders that you will swap on the Pi 5
    priv_key = "PRIMARY_PRIVATE_KEY_STUB_1047"
    pub_key = "PRIMARY_PUBLIC_KEY_STUB_1047"
    
    config_template = f"""
[Interface]
Address = 10.0.0.1/24
ListenPort = 51820
PrivateKey = {priv_key}
PostUp = iptables -A FORWARD -i %i -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i %i -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

# Peer: Oakley_Glasses_Node_29
[Peer]
PublicKey = CLIENT_PUBLIC_KEY_STUB
AllowedIPs = 10.0.0.2/32
"""
    with open("software/wg0.conf", "w") as f:
        f.write(config_template)
    print("[SYSTEM] ✅ software/wg0.conf generated. Ready for iron-layer deployment.")

if __name__ == "__main__":
    generate_sovereign_keys()
