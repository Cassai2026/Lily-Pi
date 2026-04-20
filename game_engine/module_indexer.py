import os

class SovereignIndexer:
    def __init__(self, root_path):
        self.root_path = root_path
        self.modules = []

    def scan_ecosystem(self):
        print(f"[CEREBRAL] Indexing Enki Ecosystem at: {self.root_path}")
        if not os.path.exists(self.root_path):
            print(f"[ERROR] Path not found: {self.root_path}")
            return
        for root, dirs, files in os.walk(self.root_path):
            for file in files:
                if file.endswith(".py"):
                    self.modules.append(os.path.join(root, file))
        print(f"[SUCCESS] {len(self.modules)} Sovereign Modules Indexed. OUSH.")

if __name__ == "__main__":
    # This points to where your 330 modules live locally
    indexer = SovereignIndexer("./Genesis_Ecosystem/Enki-AI")
    indexer.scan_ecosystem()
