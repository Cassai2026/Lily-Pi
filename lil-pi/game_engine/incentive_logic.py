class IncentiveLogic:
    def __init__(self):
        self.vt_balance = 0.0
        self.multipliers = {"FOCUS": 1.5, "RESILIENCE": 2.0, "DISCOVERY": 1.2}

    def calculate_gain(self, action_type, duration_seconds, success_state):
        # Rewards the PATH, not just the result
        base_gain = (duration_seconds / 60) * 10 
        multiplier = self.multipliers.get(action_type.upper(), 1.0)
        
        if not success_state:
            # Step 110 Synergy: More tokens for trying and failing!
            multiplier *= 1.5 
            
        gain = base_gain * multiplier
        return round(gain, 2)
    def update_wallet(self, amount):
        # Links to the Sovereign Wallet module
        self.vt_balance += amount
        print(f"[HUD 💰] VT EARNED: +{amount}. TOTAL: {self.vt_balance}")
        return self.vt_balance
    def check_achievements(self):
        # Milestones for the 29th Node
        milestones = {100: "NEOPHYTE_ARCHITECT", 500: "SOVEREIGN_GUIDE", 1000: "ETHER_MASTER"}
        for threshold, title in milestones.items():
            if self.vt_balance >= threshold:
                print(f"[HUD 🏆] RANK UP: {title}")
if __name__ == "__main__":
    il = IncentiveLogic()
    # Scenaro: 5 min focus session, failed the task (High Resilience)
    earned = il.calculate_gain("FOCUS", 300, False)
    il.update_wallet(earned)
    il.check_achievements()
