# CONTRACT: test_mode -> fake_sensor_data -> local_network
# Purpose: Simulates physical Pi 5 and ESP32 hardware for Windows testing.

import time
import random
import threading

class GhostHardware:
    def __init__(self):
        self.active = True
        print("[GHOST] Hardware Emitter Initialized (Windows Mode)")

    def emit_thermal(self):
        while self.active:
            temp = round(random.uniform(35.0, 50.0), 1)
            print(f"[GHOST SENSOR] Simulated CPU Temp: {temp}C")
            time.sleep(3)

    def emit_vision_pulse(self):
        while self.active:
            # Simulates the ESP32 sending a frame metadata packet
            lux = random.randint(100, 2000)
            print(f"[GHOST VISION] Oakley Frame Received | Lux: {lux}")
            time.sleep(1)

    def ignite(self):
        threading.Thread(target=self.emit_thermal, daemon=True).start()
        threading.Thread(target=self.emit_vision_pulse, daemon=True).start()
        print("[GHOST] Simulation running. Press Ctrl+C to stop.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.active = False
            print("[GHOST] Shutting down.")

if __name__ == "__main__":
    ghost = GhostHardware()
    ghost.ignite()
