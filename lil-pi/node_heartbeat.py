# CONTRACT: system_stats -> log -> monitor
import psutil
import time

class NodeHeartbeat:
    def __init__(self):
        self.active = True

    def pulse(self):
        try:
            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory().percent
            print(f"[HEARTBEAT] CPU: {cpu}% | RAM: {ram}% | STATE: ACTIVE")
        except Exception as e:
            print(f"[FAULT] Heartbeat failure: {e}")

if __name__ == "__main__":
    hb = NodeHeartbeat()
    while True:
        hb.pulse()
        time.sleep(5)
