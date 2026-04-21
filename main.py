import sys
import os
import time
import yaml

# Add core to path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'core'))

from imu_driver import IMUDriver
from gps_driver import GPSDriver
from enki_bridge import EnkiBridge
from logger import SovereignLogger
from sys_monitor import SystemMonitor

class LilyPiHUD:
    def __init__(self):
        config_path = os.path.join(BASE_DIR, "config.yaml")
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        
        self.imu = IMUDriver()
        self.gps = GPSDriver()
        self.enki = EnkiBridge()
        self.logger = SovereignLogger(self.config['telemetry']['log_directory'])
        self.sys = SystemMonitor()
        self.start_time = time.time()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        self.clear_screen()
        print(f"--- {self.config['system']['node_id']} OPERATIONAL ---")
        print("------------------------------------------------")
        try:
            while True:
                motion = self.imu.get_motion()
                location = self.gps.get_location()
                health = self.sys.get_stats()
                uptime = int(time.time() - self.start_time)
                
                data = {
                    "uptime": uptime,
                    "pitch": motion['pitch'],
                    "temp": health['cpu_temp'],
                    "cpu": health['cpu_usage']
                }

                alert = self.enki.analyze_state(data)
                self.logger.log_event(data, alert)
                
                # Professional HUD Telemetry String
                status = f"\r[T+{uptime:04d}s] | CPU: {data['cpu']}% | TEMP: {data['temp']}C | PITCH: {data['pitch']} "
                
                if alert:
                    sys.stdout.write(f"\n[🤖 ENKI] {alert}\n")
                
                sys.stdout.write(status)
                sys.stdout.flush()
                
                time.sleep(self.config['telemetry']['update_rate'])
        except KeyboardInterrupt:
            print("\n\n[🛑] SYSTEM HALTED. LOGS SAVED.")

if __name__ == "__main__":
    app = LilyPiHUD()
    app.run()
