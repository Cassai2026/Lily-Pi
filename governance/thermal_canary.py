# CONTRACT: cpu_temp vs cpu_load -> side_channel_detection -> ghost_protocol
# Purpose: Detects remote RAM-dumping attacks via thermal anomalies.

import time

class ThermalCanary:
    def __init__(self):
        self.baseline_temp_per_load = 0.5 # Degrees C per 1% load (Estimated)
        self.ambient_offset = 35.0
        print("[🛡️ CANARY] Thermal Side-Channel Shield Active.")

    def audit_vitals(self, current_temp, current_load):
        # Calculate expected temp based on load
        expected_temp = self.ambient_offset + (current_load * self.baseline_temp_per_load)
        
        # If temp is 10 degrees higher than it should be for this load...
        if current_temp > (expected_temp + 10.0):
            print(f"\n[🚨 THERMAL ANOMALY] Temp: {current_temp}C | Load: {current_load}%")
            print("[🚨 CANARY] High probability of Side-Channel RAM Extraction!")
            return "INITIATE_GHOST_PROTOCOL"
        
        return "STATE_STABLE"

if __name__ == "__main__":
    shield = ThermalCanary()
    # Test normal state
    print(f"Status: {shield.audit_vitals(45.0, 20)}")
    # Test anomaly state (High heat, low load = suspicious)
    print(f"Status: {shield.audit_vitals(65.0, 10)}")
