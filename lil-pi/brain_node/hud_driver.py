import cv2
import numpy as np

class LilyPiHUD:
    def __init__(self):
        self.baseline_hr = 42
        self.alert_color = (0, 0, 255) # Red for Aggression
        self.safe_color = (0, 255, 0)  # Green for Sovereign Flow

    def render_overlay(self, frame, heart_rate, noise_level):
        # Calculate the Vitality Index shift
        status_color = self.safe_color
        label = "SOVEREIGN FLOW"

        if heart_rate > 84 or noise_level > 700:
            status_color = self.alert_color
            label = "SHIELD ACTIVE: HIGH STATIC"

        # Draw the ACFA Interface
        cv2.putText(frame, f"PULSE: {heart_rate} BPM", (20, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, status_color, 2)
        cv2.putText(frame, label, (20, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, status_color, 2)
        
        # Apply a 'Somatic Tint' to lower sensory friction
        overlay = frame.copy()
        cv2.rectangle(overlay, (0,0), (frame.shape[1], frame.shape[2] if len(frame.shape)>2 else 100), status_color, -1)
        return cv2.addWeighted(overlay, 0.1, frame, 0.9, 0)

if __name__ == "__main__":
    print("--- 🏺 LILY-PI ACFA: HUD DRIVER READY ---")
