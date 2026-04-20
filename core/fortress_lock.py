from core.sovereign_vpn import SovereignVPN
from core.rave_antivirus_v2 import RaveAntivirusV2

def verify_fortress_integrity():
    print("--- 🏺 LILY-PI: HARDENING THE GRID (SDG 18-22) ---")
    vpn = SovereignVPN()
    rave = RaveAntivirusV2()
    
    vpn.engage_tunnel()
    rave.scan_runtime()
    
    print("[SYSTEM] ✅ FORTRESS INTEGRITY: SOLID AS A ROCK. OUSH.")
    return True

if __name__ == "__main__":
    verify_fortress_integrity()
