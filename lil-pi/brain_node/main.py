import socket
import numpy as np
import datetime
import os

def sovereign_logger(result, addr):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] SOURCE: {addr} | RESULT: {result}\n"
    log_dir = "../audit_logs"
    if not os.path.exists(log_dir): os.makedirs(log_dir)
    with open(f"{log_dir}/sovereign_audit_trail.txt", "a") as f:
        f.write(log_entry)

def tone_of_voice_audit(audio_data):
    try:
        volume = np.linalg.norm(audio_data)
        if volume > 800: return "⚠️ AGGRESSION_DETECTED"
        if volume > 400: return "🟢 STATIC_ENVIRONMENT"
        return "⚪ SILENCE"
    except:
        return "⚙️ DATA_CORRUPT"

def start_brain():
    UDP_IP = "0.0.0.0"
    UDP_PORT = 5005
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print("--- 🏺 ENKI BRAIN: NODE 29 ACTIVE ---")
    try:
        while True:
            data, addr = sock.recvfrom(2048)
            result = tone_of_voice_audit(np.frombuffer(data, dtype=np.int16))
            sovereign_logger(result, addr)
            print(f"[HUD] {result}")
    except KeyboardInterrupt:
        print("\n[SYSTEM] AUDIT SECURED. OUSH.")

if __name__ == "__main__":
    start_brain()
