# CONTRACT: system_stats -> log -> monitor
import psutil
import time

class NodeHeartbeat:
    def __init__(self):
        self.active = True

    def pulse(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        print(f"[HEARTBEAT] CPU: {cpu}% | RAM: {ram}% | STATE: ACTIVE")

if __name__ == "__main__":
    hb = NodeHeartbeat()
    while True:
        hb.pulse()
        time.sleep(5)
