import os
import psutil
import time

class RaveAntivirus:
    def __init__(self):
        self.whitelist = ["python", "bash", "ssh", "wireguard", "lily-pi"]
        self.threat_threshold = 85.0 # CPU usage limit for unauthorized procs

    def scan_for_static(self):
        print("[RAVE] 🛡️ SCANNING SYSTEM FREQUENCY...")
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                # If a process isn't whitelisted and is acting aggressively
                if proc.info['name'] not in self.whitelist and proc.info['cpu_percent'] > self.threat_threshold:
                    print(f"[RAVE] ⚠️ STATIC DETECTED: {proc.info['name']} (PID: {proc.info['pid']})")
                    self.quarantine(proc)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    def quarantine(self, proc):
        print(f"[RAVE] ☣️ ISOLATING THREAT: {proc.info['name']}")
        # Terminate the process immediately
        os.kill(proc.info['pid'], 9)
        print(f"[RAVE] ✅ THREAT NEUTRALIZED. OUSH.")

if __name__ == "__main__":
    rave = RaveAntivirus()
    while True:
        rave.scan_for_static()
        time.sleep(5)
