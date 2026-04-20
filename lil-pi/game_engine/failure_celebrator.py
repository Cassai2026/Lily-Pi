import random

class FailureCelebrator:
    def __init__(self):
        self.positive_reframes = [
            "OUSH! New data acquired. That was a great experiment.",
            "Logic gap detected! This is where the real learning happens.",
            "Sovereign move. You just found a way that doesn't work. What's next?",
            "System evolution in progress. Your brain is re-wiring right now!"
        ]

    def get_celebration(self, error_type):
        # Maps specific error types to high-energy encouragement
        base = random.choice(self.positive_reframes)
        return f"[HUD 🏺] {base} (Error: {error_type})"
    def log_failure_for_teacher(self, error_type, user_input, expected_output):
        # Instead of just 'wrong', we log the 'why' for the Audit Trail
        log_dir = "../audit_logs/pedagogy"
        import os
        if not os.path.exists(log_dir): os.makedirs(log_dir)
        with open(f"{log_dir}/learning_gaps.txt", "a") as f:
            f.write(f"ERROR: {error_type} | INPUT: {user_input} | EXPECTED: {expected_output}\n")
    def adjust_vibration(self, frustration_level):
        # If the child is frustrated, use a soft 'calm' pulse. 
        # If they are curious, use a 'high-energy' pulse.
        if frustration_level > 50:
            return "SOFT_CALM_PULSE"
        return "HIGH_ENERGY_SUCCESS_PULSE"
if __name__ == "__main__":
    celebrator = FailureCelebrator()
    print(celebrator.get_celebration("MATH_LOGIC_ERROR"))
    celebrator.log_failure_for_teacher("MATH", "2+2=5", "4")
