class MaterialTransmutator:
    def __init__(self):
        self.target_age = 10 

    def simplify_concept(self, complex_text):
        print("[HUD] 🔄 TRANSMUTING COMPLEX DATA INTO SOVEREIGN KNOWLEDGE...")
        # Dictionary of 'Sovereign Metaphors'
        metaphors = {
            "Electricity": "Like water flowing through a pipe.",
            "Graphene": "Like a super-strong spider web made of carbon.",
            "AI": "Like a very fast student who learns from you."
        }
        for key, val in metaphors.items():
            if key in complex_text:
                return val
        return "Let's find a metaphor for this together."

if __name__ == "__main__":
    mt = MaterialTransmutator()
    print(f"[HUD] TEACHER SAYS: {mt.simplify_concept('Graphene is a 2D material.')}")
