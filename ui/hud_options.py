class HUDOptions:
    def __init__(self):
        self.options = []

    def display_options(self, option_list):
        self.options = option_list
        print("[HUD] 🔘 SELECT AN OPTION VIA GESTURE:")
        for i, opt in enumerate(self.options):
            print(f"  [{i+1}] {opt}")

    def capture_gesture_selection(self, selection_index):
        # Link this to the ACD_interface gesture logic
        selected = self.options[selection_index - 1]
        print(f"[HUD] ✅ SELECTED: {selected}")
        return selected

if __name__ == "__main__":
    ho = HUDOptions()
    ho.display_options(["Conductivity", "Strength", "Color"])
