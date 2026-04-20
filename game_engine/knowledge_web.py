class KnowledgeWeb:
    def __init__(self):
        self.nodes = {}
        self.links = []

    def add_concept(self, concept, category):
        self.nodes[concept] = category
        print(f"[HUD] 🕸️ NODE ADDED TO WEB: {concept} ({category})")

    def create_link(self, concept_a, concept_b, relationship):
        self.links.append((concept_a, concept_b, relationship))
        print(f"[HUD] 🔗 LINK FORGED: {concept_a} --[{relationship}]--> {concept_b}")

    def generate_3d_view(self):
        # This prepares the spatial data for the Oakley HUD projection
        print("[HUD] 📐 GENERATING SPATIAL MIND-MAP...")
        for a, b, rel in self.links:
            print(f"[HUD] Drawing Projection: {a} to {b} (Logic: {rel})")

if __name__ == "__main__":
    web = KnowledgeWeb()
    web.add_concept("9CU Copper", "Material")
    web.add_concept("Energy Flow", "Physics")
    web.create_link("9CU Copper", "Energy Flow", "Conducts")
    web.generate_3d_view()
