# CONTRACT: raw_text -> enki_parser -> structured_json_lesson
# Purpose: Converts flat text into Socratic teaching data.

import json
import time

class CurriculumForge:
    def __init__(self):
        self.vault_path = "../enki_acfa/knowledge_vault.json"
        # Load existing vault or create empty
        try:
            with open(self.vault_path, "r") as f:
                self.vault = json.load(f)
        except FileNotFoundError:
            self.vault = {"lessons": []}

    def ingest(self, topic, raw_text, difficulty=1):
        # Basic parsing: split by sentences (placeholder for AI summarization)
        facts = [s.strip() for s in raw_text.split('.') if len(s) > 10]
        
        lesson = {
            "topic": topic.upper(),
            "ingested_at": time.time(),
            "difficulty": difficulty,
            "core_facts": facts,
            "socratic_prompt": f"Why is {topic} important for the Mesh?"
        }
        
        self.vault["lessons"].append(lesson)
        
        with open(self.vault_path, "w") as f:
            json.dump(self.vault, f, indent=4)
            
        print(f"[FORGE] Successfully ingested lesson: {topic}")

if __name__ == "__main__":
    forge = CurriculumForge()
    # Example ingestion
    sample_text = "Copper is a highly conductive metal. It is used in 9CU analysis. Heat dissipation is critical."
    forge.ingest("Copper Dynamics", sample_text, difficulty=2)
