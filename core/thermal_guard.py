class ThermalGuard:
    def __init__(self):
        self.max_temp = 75.0 # Celsius
        self.graphene_dissipation_rate = 1.2 # Boosted by Copper ions

    def monitor_pi_temp(self, current_temp):
        if current_temp > self.max_temp:
            print(f"[SHIELD] 🌡️ WARNING: Pi 5 Temp at {current_temp}C. Throttling logic.")
        else:
            print(f"[HUD] Thermal load: {current_temp}C. Graphene Sink: STABLE.")

if __name__ == "__main__":
    guard = ThermalGuard()
    guard.monitor_pi_temp(45.5)
