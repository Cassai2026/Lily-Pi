import cv2
import numpy as np
import socket
import os
from game_engine.emotional_intelligence import EmotionalIntelligence
from ui.av_sync import AVSync

class LilyPiProductionBrain:
    def __init__(self):
        self.ei = EmotionalIntelligence()
        self.av = AVSync()
        self.visor_w, self.visor_h = 1920, 1080

    def run(self):
        UDP_IP = "0.0.0.0"
        UDP_PORT = 5005
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))
        
        print("--- 🏺 LILY-PI PRO: NODE 29 STANDBY ---")
        print("Waiting for Oakley 9CU Signal...")
        
        try:
            while True:
                # 1. Listen for Oakley Feed
                data, addr = sock.recvfrom(65535)
                
                # 2. Emotional Intelligence Nudge
                emotion_nudge = self.ei.read_expression("simulated_input")
                
                # 3. Render 180 Degree Peripheral HUD
                canvas = np.zeros((self.visor_h, self.visor_w, 3), dtype=np.uint8)
                canvas[:] = (30, 30, 30) # Somatic Charcoal Shield
                
                # Center HUD for reading / Non-Verbal Support
                cv2.putText(canvas, f"FEELING: {emotion_nudge}", (600, 900), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 255), 3)
                
                cv2.imshow("LILY_PI_PRO_VISOR", canvas)
                if cv2.waitKey(1) & 0xFF == ord('q'): break
        except KeyboardInterrupt:
            print("\n[SYSTEM] SECURING NODE. OUSH.")

if __name__ == "__main__":
    node = LilyPiProductionBrain()
    node.run()
