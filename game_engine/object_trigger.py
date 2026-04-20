class ObjectLessonTrigger:
    def __init__(self):
        self.last_object = None
        # Mapping Enki-AI Module IDs to Physical Objects
        self.lesson_map = {
            "PET_BOTTLE": "Module_212: Polymer Chain Alchemics",
            "COPPER_SCRAP": "Module_39: 9CU Frequency & Energy",
            "GRAPHENE_SHEET": "Module_1047: Thermal Sovereignty"
        }

    def detect_and_load(self, seen_object):
        if seen_object in self.lesson_map and seen_object != self.last_object:
            self.last_object = seen_object
            lesson_id = self.lesson_map[seen_object]
            print(f"[HUD] 👁️ TEACHER RECOGNIZED: {seen_object}")
            print(f"[HUD] 📚 LOADING {lesson_id}...")
            return lesson_id
        return None

if __name__ == "__main__":
    trigger = ObjectLessonTrigger()
    trigger.detect_and_load("COPPER_SCRAP")
