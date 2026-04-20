class LessonSequencer:
    def __init__(self):
        self.max_steps = 5

    def sequence_data(self, raw_knowledge):
        # Breaks raw data into 5 physical/visual steps
        # This prevents the 'Wall of Text' friction for neuro-learners
        scaffold = [
            f"OBSERVE: Focus on {raw_knowledge}",
            "CONNECT: How does this feel in the 4D space?",
            "ISOLATE: Identify one specific part.",
            "APPLY: Use the ACD to interact.",
            "REFLECT: What changed in the Vault?"
        ]
        return scaffold
