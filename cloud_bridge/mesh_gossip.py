# CONTRACT: node_state -> udp_broadcast -> mesh_peer_discovery
# Purpose: Decentralized Peer-to-Peer communication for the Stretford Mesh.

import socket
import threading
import json
import time

class MeshGossip:
    def __init__(self, node_id="29", port=10470):
        self.node_id = node_id
        self.port = port
        self.peers = {} # Dictionary of discovered nodes
        self.active = True
        
        # Setup UDP Socket for Broadcasting
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock.bind(("", self.port))
        
        print(f"[MESH GOSSIP] Node {self.node_id} radio initialized on port {self.port}.")

    def _listen_for_whispers(self):
        while self.active:
            try:
                data, addr = self.sock.recvfrom(1024)
                message = json.loads(data.decode('utf-8'))
                
                sender_id = message.get("node_id")
                # Don't listen to our own echoes
                if sender_id and sender_id != self.node_id:
                    self.peers[sender_id] = {
                        "ip": addr[0],
                        "last_seen": time.time(),
                        "status": message.get("status")
                    }
                    print(f"\n[📡 MESH] Whisper received from Node {sender_id} at {addr[0]}")
            except Exception as e:
                pass

    def _broadcast_presence(self):
        while self.active:
            payload = {
                "node_id": self.node_id,
                "status": "SOVEREIGN_ACTIVE",
                "timestamp": time.time()
            }
            message = json.dumps(payload).encode('utf-8')
            # Broadcast to the entire local subnet
            self.sock.sendto(message, ('<broadcast>', self.port))
            time.sleep(5) # Pulse every 5 seconds

    def ignite(self):
        print("[MESH GOSSIP] Entering the swarm...")
        threading.Thread(target=self._listen_for_whispers, daemon=True).start()
        threading.Thread(target=self._broadcast_presence, daemon=True).start()
        
        try:
            while True:
                time.sleep(10)
                # Prune dead nodes (not seen in 15 seconds)
                current_time = time.time()
                dead_nodes = [n for n, d in self.peers.items() if current_time - d["last_seen"] > 15]
                for n in dead_nodes:
                    del self.peers[n]
                    print(f"[📡 MESH] Node {n} dropped from the swarm.")
                    
                print(f"[MESH GOSSIP] Active Peers in Swarm: {len(self.peers)}")
        except KeyboardInterrupt:
            self.active = False
            print("[MESH GOSSIP] Radio silenced.")

if __name__ == "__main__":
    radio = MeshGossip()
    radio.ignite()
