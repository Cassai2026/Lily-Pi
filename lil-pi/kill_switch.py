# CONTRACT: signal_check -> system_halt -> cleanup
# Purpose: Emergency shutdown for Node 29.

import os
import sys

class KillSwitch:
    def __init__(self, watch_file="STOP_NODE"):
        self.watch_file = watch_file

    def check(self):
        if os.path.exists(self.watch_file):
            print("[🚨 KILL SWITCH ACTIVATED] Shutting down Node 29...")
            # Perform cleanup
            os.remove(self.watch_file)
            sys.exit(0)

if __name__ == "__main__":
    # Create the file to test: New-Item STOP_NODE
    ks = KillSwitch()
    ks.check()
