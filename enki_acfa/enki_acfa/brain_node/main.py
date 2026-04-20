import socket
import cv2
import numpy as np

def start_sovereign_brain():
    UDP_IP = "0.0.0.0" 
    UDP_PORT = 5005
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    
    print("--- 🏺 ENKI BRAIN: NODE 29 ACTIVE ---")
    while True:
        data, addr = sock.recvfrom(65535)
        nparr = np.frombuffer(data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if frame is not None:
            cv2.imshow("SOVEREIGN_HUD_FEED", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'): break
if __name__ == "__main__":
    start_sovereign_brain()
