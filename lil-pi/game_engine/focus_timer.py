import time

class FocusTimer:
    def __init__(self):
        self.start_time = 0
        self.duration = 1500 # 25 Minutes standard (Sovereign Pomodoro)
        self.is_active = False

    def start_session(self, minutes=25):
        self.start_time = time.time()
        self.duration = minutes * 60
        self.is_active = True
        return f"[HUD ⏳] FOCUS SESSION INITIALIZED: {minutes}m"
    def get_time_remaining(self):
        if not self.is_active: return "00:00"
        elapsed = time.time() - self.start_time
        remaining = max(0, self.duration - elapsed)
        mins, secs = divmod(int(remaining), 60)
        return f"{mins:02d}:{secs:02d}"
    def check_flow_state(self):
        # If the timer is in the 'Deep Middle' (5-20 mins), 
        # trigger the Somatic Dimmer to block external notifications.
        elapsed = time.time() - self.start_time
        if 300 < elapsed < 1200:
            return "FLOW_SHIELD_ACTIVE"
        return "AMBIENT_MODE"
if __name__ == "__main__":
    ft = FocusTimer()
    print(ft.start_session(1)) # 1 minute test
    time.sleep(2)
    print(f"REMAINING: {ft.get_time_remaining()}")
    print(f"SHIELD STATUS: {ft.check_flow_state()}")
