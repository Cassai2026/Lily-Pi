import re

class AbstractionLayer:
    def __init__(self):
        # Dictionary of 'Heavy' words vs 'Sovereign' simplifications
        self.abstraction_map = {
            "ASYCHRONOUS": "Doing things at different times",
            "BIPARTITE": "Two parts working together",
            "CONDUCTIVITY": "How fast the pulse moves",
            "INFRASTRUCTURE": "The skeleton of the town"
        }

    def simplify_text(self, raw_text):
        # Replaces complex technical terms with somatic meanings
        processed = raw_text
        for complex_word, simple_word in self.abstraction_map.items():
            processed = re.sub(rf'\b{complex_word}\b', simple_word, processed, flags=re.IGNORECASE)
        return processed
    def check_density(self, text):
        # Counts syllables or word length to judge if the text is 'Too Heavy'
        words = text.split()
        heavy_count = sum(1 for word in words if len(word) > 10)
        density_score = (heavy_count / len(words)) * 100 if words else 0
        return density_score # Threshold > 20% triggers automatic abstraction
    def inject_metaphor(self, text, user_interest):
        # Adds a visual metaphor based on the child's favorite things
        if "data" in text.lower() and user_interest == "TRAINS":
            return f"{text}. Think of the data like passengers on a high-speed train."
        return text
if __name__ == "__main__":
    abstractor = AbstractionLayer()
    raw = "The CONDUCTIVITY of the INFRASTRUCTURE is vital."
    print(f"[HUD RAW] {raw}")
    print(f"[HUD ABS] {abstractor.simplify_text(raw)}")
