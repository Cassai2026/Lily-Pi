class EnkiBridge:
    def __init__(self, critical_tilt=45, critical_temp=75):
        self.critical_tilt = critical_tilt
        self.critical_temp = critical_temp

    def analyze_state(self, data):
        if abs(data["pitch"]) > self.critical_tilt:
            return "⚠️ STEEP INCLINE"
        if data["temp"] > self.critical_temp:
            return "🔥 HIGH CPU TEMP"
        return None
