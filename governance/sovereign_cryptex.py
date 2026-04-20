# CONTRACT: action_data -> sha256_hash -> immutable_chain_entry
# Purpose: Cryptographic, tamper-evident ledger for all Node 29 actions.

import hashlib
import json
import time
import os

class SovereignCryptex:
    def __init__(self, ledger_file="node_29_ledger.json"):
        self.ledger_file = ledger_file
        self.chain = []
        self._boot_ledger()

    def _boot_ledger(self):
        if os.path.exists(self.ledger_file):
            with open(self.ledger_file, 'r') as f:
                self.chain = json.load(f)
            print(f"[CRYPTEX] Ledger loaded. Integrity verified: {self.verify_chain()}")
        else:
            print("[CRYPTEX] Forging Genesis Block...")
            self._create_block(data="NODE_29_GENESIS_IGNITION", previous_hash="0" * 64)

    def _hash_block(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def _create_block(self, data, previous_hash):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time.time(),
            "data": data,
            "previous_hash": previous_hash
        }
        block["hash"] = self._hash_block(block)
        self.chain.append(block)
        self._save_ledger()
        return block

    def _save_ledger(self):
        with open(self.ledger_file, 'w') as f:
            json.dump(self.chain, f, indent=4)

    def log_action(self, module, action, threat_level=0):
        """Public method to log a sovereign action."""
        previous_hash = self.chain[-1]["hash"] if self.chain else "0" * 64
        payload = {
            "module": module,
            "action": action,
            "threat_level": threat_level
        }
        self._create_block(payload, previous_hash)
        print(f"[🛡️ LEDGER] Action cryptographically sealed. Index: {len(self.chain)}")

    def verify_chain(self):
        """Checks if any past logs have been altered."""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            
            # Re-calculate the hash of the current block WITHOUT its stored hash
            temp_block = {k: v for k, v in current.items() if k != "hash"}
            recalculated_hash = self._hash_block(temp_block)

            if current["hash"] != recalculated_hash or current["previous_hash"] != previous["hash"]:
                return False
        return True

if __name__ == "__main__":
    cryptex = SovereignCryptex()
    
    # Simulate some node actions
    time.sleep(0.5)
    cryptex.log_action("EYE_NODE", "Initiated ESP32 Handshake", threat_level=0)
    time.sleep(0.5)
    cryptex.log_action("ENKI_ORACLE", "Queried Wikipedia: Copper", threat_level=1)
    time.sleep(0.5)
    cryptex.log_action("IRON_SHIELD", "Blocked unverified network ping", threat_level=4)
    
    # Verify the truth
    print(f"\n[AUDIT] Is the Node 29 timeline mathematically pure? {cryptex.verify_chain()}")
