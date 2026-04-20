class NonVerbalNudge:
    def __init__(self):
        self.quick_nudges = ["Yes", "No", "Help", "Break", "More"]

    def trigger_nudge_projection(self, nudge_index):
        nudge = self.quick_nudges[nudge_index]
        print(f"[HUD] 🎯 TRIGGERING NUDGE: {nudge}")
        # Automatically sends this to the Thought Projector
        return nudge

if __name__ == "__main__":
    nvn = NonVerbalNudge()
    nvn.trigger_nudge_projection(2) # Help
