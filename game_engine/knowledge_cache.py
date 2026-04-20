import os
import json

class LocalKnowledgeCache:
    def __init__(self):
        self.cache_dir = "./docs/offline_vault"
        if not os.path.exists(self.cache_dir): os.makedirs(self.cache_dir)
        self.index_file = f"{self.cache_dir}/index.json"

    def cache_lesson(self, topic, content):
        file_name = f"{topic.replace(' ', '_').lower()}.txt"
        file_path = f"{self.cache_dir}/{file_name}"
        
        with open(file_path, "w") as f:
            f.write(content)
        
        # Update index for rapid retrieval
        self._update_index(topic, file_path)
        print(f"[HUD] 💾 OFFLINE SYNC: '{topic}' locked to local SSD.")

    def _update_index(self, topic, path):
        index = {}
        if os.path.exists(self.index_file):
            with open(self.index_file, "r") as f: index = json.load(f)
        
        index[topic] = path
        with open(self.index_file, "w") as f: json.dump(index, f)

if __name__ == "__main__":
    cache = LocalKnowledgeCache()
    cache.cache_lesson("9CU Copper Properties", "High conductivity, antimicrobial, 29th Node essential.")
