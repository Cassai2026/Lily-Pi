class ObjectLessonTrigger:
    def __init__(self):
        self.last_detected = None
        self.lesson_database = {
            "PET_BOTTLE": "Lesson 1: The Alchemical Polymer. How plastic becomes thread.",
            "COPPER_WIRE": "Lesson 2: The Path of Energy. 9CU and Signal Integrity.",
            "GRAPHENE_FLAKE": "Lesson 3: The 2D Giant. Thermal management on the edge."
        }

    def process_vision_input(self, object_label):
        if object_label != self.last_detected:
            print(f"[HUD] 👁️ TEACHER RECOGNIZED: {object_label}")
            self.last_detected = object_label
            return self.trigger_lesson(object_label)
        return None

    def trigger_lesson(self, label):
        lesson = self.lesson_database.get(label, "Teacher is curious... tell me what this is?")
        print(f"[HUD] 📖 AUTOMATIC LESSON: {lesson}")
        return lesson

if __name__ == "__main__":
    trigger = ObjectLessonTrigger()
    trigger.process_vision_input("COPPER_WIRE")
