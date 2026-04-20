import time
from core.ghost_protocol import GhostProtocol

class SovereignWatchdog:
    def __init__(self, pulse_threshold=140):
        self.pulse_threshold = pulse_threshold
        self.ghost = GhostProtocol()

    def monitor_pulse(self, current_hr):
        # If the child hits a panic state, protect the data
        if current_hr > self.pulse_threshold:
            print(f"[WATCHDOG] ⚠️ EXTREME SOMATIC STRESS: {current_hr} BPM.")
            self.ghost.execute_purge("Biometric Distress")

    def check_physical_integrity(self, gpio_tamper_detected):
        if gpio_tamper_detected:
            print("[WATCHDOG] ⚠️ HARDWARE TAMPER DETECTED.")
            self.ghost.execute_purge("Physical Breach")

if __name__ == "__main__":
    watchdog = SovereignWatchdog()
    watchdog.monitor_pulse(150) # Simulate a panic spike
