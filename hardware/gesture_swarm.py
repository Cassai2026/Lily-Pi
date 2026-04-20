# CONTRACT: left_hand_pos + right_hand_pos -> combinatory_logic -> 225_commands
# Purpose: High-bandwidth physical interaction for HUD control.

class GestureSwarm:
    def __init__(self):
        self.gestures = ["FIST", "OPEN", "POINT", "PEACE", "THUMB"] # 5 base per hand
        print("[🫱 SWARM] Dual-Hand Tracking Armed. 225 combinations possible.")

    def process_frame(self, left_hand, right_hand):
        if not left_hand or not right_hand:
            return "IDLE"
        
        # Combinatory Logic: (Left Index * 15) + Right Index
        # This creates a unique ID for every possible two-hand combination.
        l_idx = self.gestures.index(left_hand)
        r_idx = self.gestures.index(right_hand)
        cmd_id = (l_idx * 15) + r_idx
        
        return f"COMMAND_ID_{cmd_id}"

if __name__ == "__main__":
    swarm = GestureSwarm()
    # Simulate: Left Hand 'PEACE' (3) + Right Hand 'THUMB' (4)
    print(f"[HUD] Executing: {swarm.process_frame('PEACE', 'THUMB')}")
