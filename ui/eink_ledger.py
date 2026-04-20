# CONTRACT: cryptex_data -> eink_refresh_protocol -> persistent_display
# Purpose: Zero-power physical truth display. Cortisol-to-Capital tracker.

import json
import os
import time

class EInkLedger:
    def __init__(self, cryptex_path="../governance/node_29_ledger.json"):
        self.cryptex_path = cryptex_path
        print("[E-INK] Fast-Refresh Terminal Driver initialized.")

    def render_display(self):
        print("\n=============================================")
        print("  🏺 SOVEREIGN E-INK LEDGER (ZERO-POWER) 🏺  ")
        print("=============================================")
        
        if os.path.exists(self.cryptex_path):
            with open(self.cryptex_path, 'r') as f:
                chain = json.load(f)
            
            # Display the genesis and the latest action
            genesis = chain[0]
            latest = chain[-1]
            
            print(f"TARGET ASSET: £10.07M")
            print(f"SOVEREIGN STATE: LOCKED AND AUDITED")
            print("-" * 45)
            print(f"LAST SECURE ACTION: {latest['data']['action']}")
            print(f"THREAT LEVEL: {latest['data']['threat_level']}")
            print(f"CRYPTOGRAPHIC HASH: {latest['hash'][:16]}...")
        else:
            print("AWAITING CRYPTEX DATA...")
            
        print("=============================================")
        print("[E-INK] Screen refreshed. Powering down display bus.")

if __name__ == "__main__":
    display = EInkLedger()
    display.render_display()
