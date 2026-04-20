class BloomTaxonomy:
    def __init__(self):
        self.levels = ["REMEMBER", "UNDERSTAND", "APPLY", "ANALYZE", "EVALUATE", "CREATE"]

    def get_level_prompt(self, current_index):
        # Shifts from simple identification to complex creation
        if current_index < len(self.levels):
            return f"[HUD] MISSION LEVEL: {self.levels[current_index]}"
        return "[HUD] MISSION LEVEL: CREATE"
