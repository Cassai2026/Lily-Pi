import json
import time
import os

class SovereignLogger:
    def __init__(self, log_dir="D:/Lily-Pi/logs"):
        self.log_path = os.path.join(log_dir, f"audit_{int(time.time())}.json")
        print(f"[📂] Audit Log Initialized: {self.log_path}")

    def log_event(self, telemetry, alert=None):
        entry = {
            "timestamp": time.time(),
            "telemetry": telemetry,
            "alert": alert
        }
        with open(self.log_path, "a") as f:
            f.write(json.dumps(entry) + "\n")
