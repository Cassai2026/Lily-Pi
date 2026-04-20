import socket
import numpy as np
import datetime
import os

def sovereign_logger(result, addr):
    # Create the Forensic Log entry
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] SOURCE: {addr} | RESULT: {result}\n"
    
    # Save to the Sovereign Audit folder
    log_dir = "../audit_logs"
    if not os.path.exists(log_dir): os.makedirs(log_dir)
    
    with open(f"{log_dir}/sovereign_audit_trail.txt", "a") as f:
        f.write(log_entry)

def tone_of_voice_audit(audio_data):
    # Frequency analysis for Aggression vs Static
    volume = np.linalg.norm(audio_data)
    if volume > 800: # Threshold for high-intensity aggression
        return "⚠️ AGGRESSION_DETECTED"
    elif volume > 400:
        return "🟢 STATIC_ENVIRONMENT"
    return "⚪ SILENCE"

def start_brain():
    UDP_IP = "0.0.0.0"
    UDP_PORT = 5005
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    
    print("--- 🏺 ENKI BRAIN: SOVEREIGN LOGGER ACTIVE ---")
    
    try:
        while True:
            data, addr = sock.recvfrom(1024)
            result = tone_of_voice_audit(np.frombuffer(data, dtype=np.int16))
            sovereign_logger(result, addr)
            print(f"[HUD] {result}")
    except KeyboardInterrupt:
        print("\n[SYSTEM] AUDIT TRAIL SECURED. OUSH.")

if __name__ == "__main__":
    start_brain()
