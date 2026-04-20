class ProgressPulse:
    def __init__(self):
        self.total_xp = 0
        self.rank = "Novice Architect"

    def earn_xp(self, amount, skill_category):
        self.total_xp += amount
        print(f"[HUD] ✨ XP GAINED: +{amount} in {skill_category}")
        print(f"[HUD] TOTAL XP: {self.total_xp} | RANK: {self.rank}")
        self.check_rank_up()

    def check_rank_up(self):
        if self.total_xp > 1000 and self.rank == "Novice Architect":
            self.rank = "Sovereign Builder"
            print("[HUD] 🎊 RANK UP: YOU ARE NOW A SOVEREIGN BUILDER!")

if __name__ == "__main__":
    pulse = ProgressPulse()
    pulse.earn_xp(150, "9CU_Material_Science")
