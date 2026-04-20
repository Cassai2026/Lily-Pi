class CognitiveMirror:
    def __init__(self):
        self.intent_log = []

    def verify_intent(self, user_statement):
        # Checks if the user is acting with agency or just passive scrolling/querying
        if len(user_statement.split()) < 3:
            print("[HUD] 🛡️ COGNITIVE SHIELD: Intent too vague. Be specific, Architect.")
            return False
        
        print(f"[HUD] ✅ INTENT ANCHORED: '{user_statement}'")
        self.intent_log.append(user_statement)
        return True

    def privacy_purge(self):
        # Wipes the intent log to ensure no behavioral profile can be built
        self.intent_log = []
        print("[SYSTEM] 💨 COGNITIVE PURGE: Behavioral traces vaporized.")

if __name__ == "__main__":
    mirror = CognitiveMirror()
    mirror.verify_intent("I want to understand the atomic structure of 9CU copper.")
