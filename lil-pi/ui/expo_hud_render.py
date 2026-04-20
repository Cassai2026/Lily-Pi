import cv2
import numpy as np
import time

class ExpoHUD:
    def __init__(self):
        self.pine_green = (34, 139, 34)  # The 10^47 Signature Color
        self.alert_red = (0, 0, 255)
        self.white = (255, 255, 255)
        self.font = cv2.FONT_HERSHEY_SIMPLEX

    def create_overlay(self, frame):
        overlay = frame.copy()
        h, w, _ = frame.shape
        return overlay, h, w

    def draw_corners(self, img, w, h):
        length = 50
        t = 2
        cv2.line(img, (20, 20), (20 + length, 20), self.pine_green, t)
        cv2.line(img, (20, 20), (20, 20 + length), self.pine_green, t)
        cv2.line(img, (w-20, 20), (w-20-length, 20), self.pine_green, t)
        cv2.line(img, (w-20, 20), (w-20, 20 + length), self.pine_green, t)
        cv2.line(img, (20, h-20), (20 + length, h-20), self.pine_green, t)
        cv2.line(img, (20, h-20), (20, h-20-length), self.pine_green, t)
        cv2.line(img, (w-20, h-20), (w-20-length, h-20), self.pine_green, t)
        cv2.line(img, (w-20, h-20), (w-20, h-20-length), self.pine_green, t)

    def draw_telemetry(self, img, node_id="29", cpu_load="14%"):
        cv2.putText(img, f"NODE: {node_id}", (40, 60), self.font, 0.7, self.pine_green, 2)
        cv2.putText(img, f"MESH: STRETFORD_GRID", (40, 90), self.font, 0.6, self.pine_green, 1)
        cv2.putText(img, f"LOAD: {cpu_load}", (40, 120), self.font, 0.6, self.pine_green, 1)
        cv2.putText(img, "STATUS: SOVEREIGN", (40, 150), self.font, 0.6, (0, 255, 0), 1)

    def draw_crosshair(self, img, w, h):
        cx, cy = w // 2, h // 2
        cv2.circle(img, (cx, cy), 10, self.pine_green, 1)
        cv2.line(img, (cx - 20, cy), (cx + 20, cy), self.pine_green, 1)
        cv2.line(img, (cx, cy - 20), (cx, cy + 20), self.pine_green, 1)

    def draw_subtitles(self, img, text, w, h):
        text_size = cv2.getTextSize(text, self.font, 0.7, 2)[0]
        tx = (w - text_size[0]) // 2
        cv2.rectangle(img, (tx - 10, h - 80), (tx + text_size[0] + 10, h - 40), (0,0,0), -1)
        cv2.putText(img, text, (tx, h - 55), self.font, 0.7, self.white, 2)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    hud = ExpoHUD()
    while True:
        ret, frame = cap.read()
        if not ret: break
        overlay, h, w = hud.create_overlay(frame)
        hud.draw_corners(overlay, w, h)
        hud.draw_telemetry(overlay)
        hud.draw_crosshair(overlay, w, h)
        hud.draw_subtitles(overlay, "OBSERVE: COPPER THERMAL DYNAMICS", w, h)
        final = cv2.addWeighted(frame, 0.7, overlay, 0.3, 0)
        cv2.imshow("LILIETH-PI SOVEREIGN HUD", final)
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    cap.release()
    cv2.destroyAllWindows()
