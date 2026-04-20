# CONTRACT: sender_key + request -> capability_check -> execution
# Purpose: Microkernel-style security. Enforces Principle of Least Privilege.

class CapabilityIPC:
    def __init__(self):
        self.registry = {
            "EYE_NODE_KEY_1047": ["READ_VISION", "SEND_GOSSIP"],
            "ENKI_BRAIN_KEY_888": ["READ_VISION", "WRITE_CRYPTEX", "SPEAK_SOMATIC"]
        }

    def send_message(self, key, action):
        permissions = self.registry.get(key, [])
        if action in permissions:
            print(f"[🗝️ IPC] Access Granted: {action}")
            return True
        else:
            print(f"[🚨 SECURITY] Access Denied: Key {key[:6]} lacks '{action}' capability.")
            return False

if __name__ == "__main__":
    ipc = CapabilityIPC()
    # The Brain can speak
    ipc.send_message("ENKI_BRAIN_KEY_888", "SPEAK_SOMATIC")
    # The Eye tries to write to the Cryptex (Illegitimate)
    ipc.send_message("EYE_NODE_KEY_1047", "WRITE_CRYPTEX")
