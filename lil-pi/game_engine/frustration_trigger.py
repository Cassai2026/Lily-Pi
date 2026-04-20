class FrustrationTrigger:
    def __init__(self):
        self.cooldown_active = False

    def evaluate_frustration(self, heart_rate, gaze_stability):
        # Logic to kill the lesson if the child is over-stimulated
        if heart_rate > 95 or gaze_stability < 0.3:
            self.cooldown_active = True
            return "[HUD] 🧘 INTERVENTION: Sensory Overload. Dimming HUD."
        self.cooldown_active = False
        return "[HUD] 🟢 FLOW_STATE_STABLE"
