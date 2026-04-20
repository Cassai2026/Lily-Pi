class TeacherFeedback:
    def __init__(self):
        self.emojis = {"success": "🌟", "thinking": "🤔", "focus": "🧘"}

    def show_feedback(self, status_type, message):
        icon = self.emojis.get(status_type, "📖")
        print(f"[HUD] {icon} TEACHER: {message}")

if __name__ == "__main__":
    tf = TeacherFeedback()
    tf.show_feedback("success", "You've mastered the PET Polymer Lesson!")
