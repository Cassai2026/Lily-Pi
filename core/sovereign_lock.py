from cryptography.fernet import Fernet
import os

class SovereignLock:
    def __init__(self):
        self.key_path = "core/node_29.key"
        if not os.path.exists(self.key_path):
            self.key = Fernet.generate_key()
            with open(self.key_path, "wb") as key_file:
                key_file.write(self.key)
        else:
            with open(self.key_path, "rb") as key_file:
                self.key = key_file.read()
        self.cipher = Fernet(self.key)

    def encrypt_heartbeat(self, progress_data):
        return self.cipher.encrypt(progress_data.encode())

    def decrypt_heartbeat(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data).decode()

if __name__ == "__main__":
    lock = SovereignLock()
    secret = lock.encrypt_heartbeat("Level_14_Mastery:9CU_Copper")
    print(f"[HUD] 🔒 HEARTBEAT ENCRYPTED: {secret[:20]}...")
