# CONTRACT: rogue_payload -> udp_broadcast -> trigger_iron_shield
# Purpose: Simulates a hostile node injecting static into the Stretford Mesh.

import socket
import json
import time
import random

class ChaosInjector:
    def __init__(self, target_port=10470):
        self.port = target_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        print("===================================================")
        print("⚠️  CHAOS INJECTOR ONLINE. PREPARING TO FLOOD MESH.")
        print("===================================================")

    def inject_static(self):
        # Generate a fake, unauthorized MAC/Node ID
        rogue_id = f"ROGUE_{random.randint(1000, 9999)}"
        
        payload = {
            "node_id": rogue_id,
            "status": "MALFORMED_STATIC_PAYLOAD",
            "threat_level": 9, # Extreme Threat
            "data": "0xDEADBEEF" * 10 
        }
        
        message = json.dumps(payload).encode('utf-8')
        print(f"[🔥 INJECT] Firing Level 9 Static Burst from {rogue_id}...")
        
        # Rapid-fire 5 packets to simulate a flood attack
        for _ in range(5):
            self.sock.sendto(message, ('<broadcast>', self.port))
            time.sleep(0.1)
            
        print("[🔥 INJECT] Burst complete. Watch the Node 29 logs.")

if __name__ == "__main__":
    injector = ChaosInjector()
    try:
        while True:
            input("\n[Press ENTER to fire a Chaos Burst into the Mesh (Ctrl+C to exit)]")
            injector.inject_static()
    except KeyboardInterrupt:
        print("\n[CHAOS INJECTOR] Powered down. The Mesh is safe.")
