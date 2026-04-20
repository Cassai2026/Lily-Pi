class AgencyHUD:
    def __init__(self):
        self.overlay_active = True

    def request_purpose(self):
        print("[HUD] 🏺 SOCRATIC CHECK: What is the purpose of this inquiry?")
        # This waits for a voice or gesture input to prove agency
        return "AWAITING_INTENT"

if __name__ == "__main__":
    hud = AgencyHUD()
    hud.request_purpose()
