import argparse
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
    def __init__(self, demo_seconds=None, clear_screen=True):
        config_path = os.path.join(BASE_DIR, "config.yaml")
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)

        self.imu = IMUDriver()
        self.gps = GPSDriver()
        self.enki = EnkiBridge(
            critical_tilt=self.config["thresholds"]["critical_tilt"],
            critical_temp=self.config["thresholds"]["critical_temp"],
        )
        self.logger = SovereignLogger(self.config['telemetry']['log_directory'])
        self.sys = SystemMonitor()
        self.start_time = time.time()
        self.demo_seconds = demo_seconds
        self.should_clear_screen = clear_screen

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        if self.should_clear_screen:
            self.clear_screen()
        print(f"--- {self.config['system']['node_id']} OPERATIONAL ---")
        print("------------------------------------------------")
        if self.demo_seconds is not None:
            print(f"[DEMO] Running deterministic demo for {self.demo_seconds} seconds.")

        loop_count = 0
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
                    "cpu": health['cpu_usage'],
                    "lat": location["lat"],
                    "lon": location["lon"],
                }

                if self.demo_seconds is not None and loop_count == 5:
                    data["pitch"] = self.config["thresholds"]["critical_tilt"] + 7

                alert = self.enki.analyze_state(data)
                self.logger.log_event(data, alert)

                # Professional HUD Telemetry String
                status = f"\r[T+{uptime:04d}s] | CPU: {data['cpu']}% | TEMP: {data['temp']}C | PITCH: {data['pitch']} "

                if alert:
                    sys.stdout.write(f"\n[🤖 ENKI] {alert}\n")

                sys.stdout.write(status)
                sys.stdout.flush()
                loop_count += 1
                if self.demo_seconds is not None and (time.time() - self.start_time) >= self.demo_seconds:
                    print("\n\n[✅] DEMO COMPLETE. LOGS SAVED.")
                    break

                time.sleep(self.config['telemetry']['update_rate'])
        except KeyboardInterrupt:
            print("\n\n[🛑] SYSTEM HALTED. LOGS SAVED.")

def parse_args():
    parser = argparse.ArgumentParser(description="Run Lily-Pi HUD telemetry loop.")
    parser.add_argument(
        "--demo-seconds",
        type=int,
        default=None,
        help="Run a deterministic investor demo for N seconds and exit cleanly.",
    )
    parser.add_argument(
        "--no-clear",
        action="store_true",
        help="Do not clear terminal before starting output.",
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    app = LilyPiHUD(demo_seconds=args.demo_seconds, clear_screen=not args.no_clear)
    app.run()
