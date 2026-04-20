# CONTRACT: camera_sensor -> esp32_udp_broadcast -> pi5_vision_node
# Purpose: Near-zero latency vision streaming for the Split-Brain architecture.

import socket
import time

class ESP32VisionStreamer:
    def __init__(self, pi_ip="192.168.1.29", port=10471):
        self.target = (pi_ip, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(f"[👁️ EYE] Vision Streamer Active. Targeting Brain at {pi_ip}")

    def stream_mock_frame(self):
        # Simulating a 640x480 compressed JPEG frame
        fake_frame_data = b"\xff\xd8" + b"\x00" * 1024 + b"\xff\xd9"
        try:
            self.sock.sendto(fake_frame_data, self.target)
            return True
        except Exception as e:
            print(f"[🚨 EYE ERROR] Stream interrupted: {e}")
            return False

if __name__ == "__main__":
    eye = ESP32VisionStreamer()
    print("[EYE] Initiating Split-Brain Link...")
    for i in range(100): # Stream 100 frames
        eye.stream_mock_frame()
        time.sleep(0.03) # ~30 FPS
    print("[EYE] Test Stream Complete.")
