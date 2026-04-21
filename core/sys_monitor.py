import psutil
class SystemMonitor:
    def get_stats(self):
        return {"cpu_usage": psutil.cpu_percent(), "ram_usage": psutil.virtual_memory().percent, "cpu_temp": 0}
