import random
class SocraticQuery:
    def __init__(self):
        self.prompts = [
            "What do you notice about the way this moves?",
            "How does this connect to what we saw earlier?",
            "If we changed one thing here, what would happen?"
        ]
    def generate_question(self, context_topic):
        return f"[HUD] Topic: {context_topic} | {random.choice(self.prompts)}"
