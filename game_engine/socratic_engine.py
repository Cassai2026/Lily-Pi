class SocraticTeacher:
    def __init__(self):
        self.question_count = 0
        self.understanding_score = 0

    def ask_question(self, topic):
        self.question_count += 1
        questions = {
            "9CU_Copper": "Why do we use copper ions in the graphene instead of just plastic?",
            "PET_Polymer": "How does heat change the shape of the bottle?",
            "Sovereign_Logic": "What happens to the data when we wipe the RAM cache?"
        }
        query = questions.get(topic, "What is the most interesting thing you see right now?")
        print(f"[HUD] ❓ SOCRATIC QUERY: {query}")
        return query

    def evaluate_response(self, response_keywords, expected_keywords):
        # Logic to check if the child is on the right track
        matches = set(response_keywords) & set(expected_keywords)
        if len(matches) > 0:
            self.understanding_score += 10
            print(f"[HUD] 🌟 EXCELLENT: You recognized the importance of {list(matches)[0]}!")
            return True
        print("[HUD] 🤔 TEACHER: Almost! Think about how the energy moves...")
        return False

if __name__ == "__main__":
    st = SocraticTeacher()
    st.ask_question("9CU_Copper")
