import time
from imu_driver import IMUDriver
from gps_driver import GPSDriver
from enki_bridge import EnkiBridge
from logger import SovereignLogger

class HUDSystem:
    def __init__(self):
        self.imu = IMUDriver()
        self.gps = GPSDriver()
        self.enki = EnkiBridge()
        self.logger = SovereignLogger()
        self.start_time = time.time()

    def run_loop(self):
        try:
            while True:
                motion = self.imu.get_motion()
                location = self.gps.get_location()
                
                data = {
                    "uptime": int(time.time() - self.start_time),
                    "pitch": motion['pitch'],
                    "roll": motion['roll'],
                    "lat": location['lat'],
                    "lon": location['lon']
                }

                alert = self.enki.analyze_state(data)
                
                # Seal the data in the Cryptex
                self.logger.log_event(data, alert)
                
                output = f"[HUD] T+{data['uptime']}s | PITCH: {data['pitch']} | ROLL: {data['roll']}"
                if alert:
                    print(f"\n[🤖 ENKI] {alert}")
                
                print(output, end="\r")
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\n[🛑] Audit Sealed. SHUTDOWN.")

if __name__ == "__main__":
    HUDSystem().run_loop()
