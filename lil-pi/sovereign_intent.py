# CONTRACT: raw_user_input -> sanitization_layer -> interpreted_intent
# Purpose: Safety barrier between user and core logic.

class IntentInterpreter:
    def __init__(self):
        self.safe_keywords = ["LEARN", "STOP", "MAP", "STATUS"]

    def interpret(self, raw_input):
        sanitized = raw_input.upper().strip()
        if sanitized in self.safe_keywords:
            return sanitized
        return "UNKNOWN_INTENT_REJECTED"

if __name__ == "__main__":
    ii = IntentInterpreter()
    print(f"Result: {ii.interpret('  learn ')}") # Valid
    print(f"Result: {ii.interpret('DELETE SYSTEM')}") # Rejected
