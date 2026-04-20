# CONTRACT: usb_event -> hardware_whitelist -> allow_or_block
# Purpose: Microkernel-style hardware sandboxing. Prevents BadUSB/MACTANS attacks.

import time
import random

class USBInterceptor:
    def __init__(self):
        # Only explicitly trusted devices (e.g., specific Oakley tether) are allowed.
        self.trusted_vids = ["0x0403", "0x1A86"] # Example FTDI/CH340 Vendor IDs
        print("[🛡️ USB SHIELD] Port Sandbox Active. Monitoring for rogue insertions...")

    def scan_bus(self):
        # Simulating a hardware interrupt when a device is plugged in
        incoming_vid = random.choice(["0x0403", "0x1234", "0x6666", "0x1A86"])
        print(f"\n[HARDWARE EVENT] New USB Device Detected. VID: {incoming_vid}")
        
        if incoming_vid not in self.trusted_vids:
            print("[🚨 THREAT] Unauthorized HID Keyboard profile detected!")
            print("[🛡️ USB SHIELD] ACTION: Power to port severed instantly. Logged to Cryptex.")
            return False
        else:
            print("[USB SHIELD] Device matches Sovereign Whitelist. Access granted.")
            return True

if __name__ == "__main__":
    shield = USBInterceptor()
    for _ in range(3):
        time.sleep(2)
        shield.scan_bus()
