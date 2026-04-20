class AssetScanner:
    def __init__(self):
        self.asset_registry = {
            "PET_BOTTLE": {"value": 1.5, "material": "Polymer"},
            "COPPER_SCRAP": {"value": 15.0, "material": "9CU_Conductive"},
            "GRAPHENE_WASTE": {"value": 50.0, "material": "Thermal_Node"}
        }

    def scan_environment(self, detected_object):
        print(f"[HUD] 🔍 SCANNING PHYSICAL ASSET: {detected_object}...")
        if detected_object in self.asset_registry:
            data = self.asset_registry[detected_object]
            print(f"[HUD] ✅ ASSET IDENTIFIED: {detected_object}")
            print(f"[HUD] VALUE: {data['value']} VT (Vulnerability Tokens)")
            print(f"[HUD] USE: Refine into {data['material']} for 3D Printing.")
        else:
            print("[HUD] ⚪ UNKNOWN MATERIAL: No Sovereign Value assigned.")

if __name__ == "__main__":
    scanner = AssetScanner()
    scanner.scan_environment("COPPER_SCRAP")
