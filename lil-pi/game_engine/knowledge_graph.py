class KnowledgeGraph:
    def __init__(self):
        # The web of connections: {Topic: [Related_Nodes]}
        self.graph = {
            "COPPER": ["ELECTRICITY", "9CU_CONDUCTIVE", "THERMAL_DYNAMICS"],
            "GRAPHENE": ["COOLING", "STRENGTH", "CARBON_STRUCTURE"],
            "PI5": ["QUAD_POWER", "LINUX", "SOVEREIGN_NODE"]
        }
        self.learned_nodes = set()

    def discover_node(self, node_name):
        node = node_name.upper()
        if node in self.graph:
            self.learned_nodes.add(node)
            return f"[HUD 🕸️] CONNECTION ESTABLISHED: {node}"
        return "[HUD] ⚪ UNKNOWN NODE"
    def suggest_next_path(self, current_node):
        # Suggests the 'next step' based on the neighbors in the graph
        node = current_node.upper()
        neighbors = self.graph.get(node, [])
        unlearned = [n for n in neighbors if n not in self.learned_nodes]
        if unlearned:
            import random
            return f"[HUD 🎓] Curious about {random.choice(unlearned)} next?"
        return "[HUD] 🏆 TOPIC FULLY MAPPED."
    def check_synergy(self, node_a, node_b):
        # Logic to see if two topics 'link' to create a new insight
        if node_b.upper() in self.graph.get(node_a.upper(), []):
            return True
        return False
if __name__ == "__main__":
    kg = KnowledgeGraph()
    print(kg.discover_node("COPPER"))
    print(kg.suggest_next_path("COPPER"))
