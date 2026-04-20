import datetime

class ResearchLogger:
    def __init__(self):
        self.log_path = "docs/research_logs.txt"

    def record_interaction(self, subject, observation):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_path, "a") as f:
            f.write(f"[{timestamp}] {subject}: {observation}\n")
        print(f"[NODE 29] Research logged: {observation}")

if __name__ == "__main__":
    logger = ResearchLogger()
    logger.record_interaction("Cognitive_Psych", "Subject demonstrated 20% faster retention via HUD scaffolding.")
