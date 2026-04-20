class RaveHUD:
    def __init__(self):
        self.alert_color = "Red_Static"

    def signal_breach(self, threat_name):
        print(f"[HUD] 🚨 RAVE ALERT: '{threat_name}' attempted to breach your Node.")
        print("[HUD] 🛡️ TEACHER: 'Don't worry, Architect. I've shielded our mind.'")

if __name__ == "__main__":
    alert = RaveHUD()
    alert.signal_breach("Unknown_Spyware_X")
