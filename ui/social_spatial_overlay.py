class SocialSpatialOverlay:
    def __init__(self):
        self.overlay_active = True

    def draw_social_guide(self, person_coords, emotion_label):
        # Draws a soft 'Social Aura' on the HUD around people
        print(f"[HUD] 🧘 SOCIAL SCAFFOLD: {emotion_label} aura around Target at {person_coords}")
        print(f"[HUD] 🏺 MENTOR SAYS: 'They seem {emotion_label}. Try a friendly greeting.'")

if __name__ == "__main__":
    ss_overlay = SocialSpatialOverlay()
    ss_overlay.draw_social_guide("[320, 240]", "Happy")
