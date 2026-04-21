class IMUDriver:
    def __init__(self):
        self.bus = None
        print("[🛰️ IMU] Simulation Mode Active")
    def get_motion(self):
        return {"pitch": 1.2, "roll": -0.5}
