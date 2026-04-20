import socket
import numpy as np
import os

def check_vitality_index(heart_rate):
    # The 42-Pulse Athletic Buffer calibration
    baseline = 42
    if heart_rate > (baseline * 2):
        return "⚠️ VITALITY ALERT: HIGH CORTISOL DETECTED. ACTIVATE SHIELD."
    return "🟢 VITALITY STABLE: ATHLETIC BUFFER ACTIVE."

def start_acfa_brain():
    UDP_IP = "0.0.0.0"
    UDP_PORT = 5005
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    
    print("--- 🏺 ACFA BRAIN: NEURO-LEARNER SUPPORT ACTIVE ---")
    
    try:
        while True:
            data, addr = sock.recvfrom(2048)
            # Simulated incoming Biometric + Audio Data
            # Format: [HeartRate, Volume]
            input_data = np.frombuffer(data, dtype=np.int16)
            
            if len(input_data) >= 2:
                hr_status = check_vitality_index(input_data[0])
                print(f"[ACFA HUD] {hr_status}")
    except KeyboardInterrupt:
        print("\n[SYSTEM] ACFA SECURED. OUSH.")

if __name__ == "__main__":
    start_acfa_brain()
