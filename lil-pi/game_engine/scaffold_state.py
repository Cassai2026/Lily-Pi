class ScaffoldState:
    def __init__(self):
        self.modes = ["DISCOVERY", "SCAFFOLDING", "ZEN_SHIELD"]
        self.current_mode = "DISCOVERY"
        self.frustration_threshold = 75

    def update_state(self, biometrics):
        if biometrics['heart_rate'] > self.frustration_threshold:
            self.current_mode = "ZEN_SHIELD"
        elif biometrics['focus_score'] < 40:
            self.current_mode = "SCAFFOLDING"
        else:
            self.current_mode = "DISCOVERY"
        return self.current_mode
