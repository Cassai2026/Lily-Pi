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
        # Create a transparent layer for the 4D effect
        overlay = frame.copy()
        h, w, _ = frame.shape
        return overlay, h, w
