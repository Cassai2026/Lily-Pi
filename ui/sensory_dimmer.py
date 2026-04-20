class SensoryDimmer:
    def __init__(self):
        self.hud_opacity = 1.0
        self.voice_volume = 1.0

    def adjust_for_friction(self, friction_level):
        if friction_level == "ENGAGE_SHIELD":
            self.hud_opacity = 0.3 # Dim the HUD to reduce cognitive load
            self.voice_volume = 0.5 # Soften the teacher's voice
            print("[HUD] 🌑 SHIELD ACTIVE: HUD Dimmed 70% | Volume Softened.")
        else:
            self.hud_opacity = 1.0
            self.voice_volume = 1.0
            print("[HUD] ☀️ AMBIENT MODE: Full Clarity.")

if __name__ == "__main__":
    dimmer = SensoryDimmer()
    dimmer.adjust_for_friction("ENGAGE_SHIELD")
