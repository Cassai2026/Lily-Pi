# CONTRACT: city_api_data + lora_sensor_data -> truth_audit -> discrepancy_log
# Purpose: Audits municipal environmental claims against live sensor metrics.

import json
import random

class CityIngestor:
    def __init__(self):
        self.official_data = {"air_quality": 0, "traffic_load": "LOW"}
        print("[🏙️ CITY INGESTOR] Connected to Stretford Smart-City Grid.")

    def audit_environment(self, my_sensor_val):
        # Simulate fetching official municipal data
        self.official_data["air_quality"] = round(random.uniform(10.0, 15.0), 2)
        
        print(f"\n[AUDIT] Municipal Official PM2.5: {self.official_data['air_quality']}")
        print(f"[AUDIT] Sovereign Node PM2.5: {my_sensor_val}")
        
        diff = abs(self.official_data["air_quality"] - my_sensor_val)
        
        if diff > 5.0:
            print("[🚨 DISCREPANCY] Official data does not match Sovereign Truth!")
            return "THREAT_DETECTED: DATA_MANIPULATION"
        
        print("[AUDIT] Data Consensus: VERIFIED.")
        return "CONSENSUS_STABLE"

if __name__ == "__main__":
    auditor = CityIngestor()
    # Simulate a high-pollution reading from your LoRa nodes
    auditor.audit_environment(my_sensor_val=22.5)
