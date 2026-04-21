import json, os
class SovereignLogger:
    def __init__(self, log_dir):
        self.path = os.path.join(log_dir, "audit.json")
        if not os.path.exists(log_dir): os.makedirs(log_dir)
    def log_event(self, data, alert):
        with open(self.path, "a") as f:
            f.write(json.dumps({"data": data, "alert": alert}) + "\n")
