import json
from core.sovereign_lock import SovereignLock

class ResurrectionLedger:
    def __init__(self):
        self.ledger_path = "docs/sovereign_vault/progress_ledger.json"
        self.lock = SovereignLock()

    def save_progress(self, student_id, mastery_string):
        encrypted_pulse = self.lock.encrypt_heartbeat(mastery_string)
        
        # Save to the persistent SSD vault
        entry = {student_id: encrypted_pulse.decode()}
        with open(self.ledger_path, "w") as f:
            json.dump(entry, f)
        print(f"[HUD] 🧬 PROGRESS ANCHORED. Resurrection Link established.")

if __name__ == "__main__":
    ledger = ResurrectionLedger()
    ledger.save_progress("Student_Alpha", "Module_39_Complete")
