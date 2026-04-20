class ContextEngine:
    def __init__(self):
        self.active_objects = []
    def ingest_vision_data(self, detected_objects):
        # Prioritize high-value assets for learning
        self.active_objects = [obj for obj in detected_objects if obj.get('priority', 0) > 5]
        return self.active_objects[0] if self.active_objects else "ENV_STATIC"
