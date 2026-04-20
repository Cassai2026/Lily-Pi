class SomaticPulseSync:
    def __init__(self, baseline_hr=65):
        self.baseline = baseline_hr
        self.current_state = "CALM"

    def analyze_vitals(self, heart_rate):
        print(f"[HUD] ❤️ MONITORING PULSE: {heart_rate} BPM")
        
        if heart_rate > (self.baseline * 1.4): # 40% above baseline
            self.current_state = "STRESSED"
            print("[HUD] ⚠️ SENSORY FRICTION DETECTED: Engaging Shielding.")
            return "ENGAGE_SHIELD"
        elif heart_rate < (self.baseline * 0.8):
            self.current_state = "FOCUSED"
            return "MAINTAIN_FLOW"
        else:
            self.current_state = "CALM"
            return "STANDARD_MODE"

if __name__ == "__main__":
    sync = SomaticPulseSync(70)
    sync.analyze_vitals(110)
