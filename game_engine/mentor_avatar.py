class MentorAvatar:
    def __init__(self):
        self.avatar_state = "IDLE"
        self.position = "RIGHT_PERIPHERY"

    def point_at_object(self, object_name):
        print(f"[HUD] 🏺 MENTOR: Points toward the {object_name}.")
        self.avatar_state = "GUIDING"
        return f"Look there! That is {object_name}."

    def social_nudge(self, emotion_detected):
        # Linking to our Emotional Intelligence module
        if emotion_detected == "confusion":
            print("[HUD] 🏺 MENTOR: Nudges child... 'It's okay to ask for help.'")
        elif emotion_detected == "anger":
            print("[HUD] 🏺 MENTOR: 'Step back, let's find a quiet space.'")

if __name__ == "__main__":
    mentor = MentorAvatar()
    mentor.point_at_object("9CU Copper Scrap")
