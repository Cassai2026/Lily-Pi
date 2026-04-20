# CONTRACT: raw_data, keystream -> xor_encryption -> ciphertext
# Purpose: Ultra-lightweight, on-sensor stream cipher to prevent interception.

from itertools import cycle

class DracoCipher:
    def __init__(self, sovereign_key="10E47_IRON_SHIELD_GENESIS"):
        self.key = sovereign_key.encode()
        print("[🛡️ DRACO] Stream Cipher Initialized. Keys locked.")

    def encrypt_stream(self, data: str) -> bytes:
        """Applies XOR keystream encryption. Fast enough for real-time ESP32 video."""
        data_bytes = data.encode()
        # XOR each byte of data with a cycling byte of the key
        encrypted = bytes(a ^ b for a, b in zip(data_bytes, cycle(self.key)))
        return encrypted

    def decrypt_stream(self, encrypted_data: bytes) -> str:
        """XOR is symmetric. Running it again with the same key decrypts it."""
        decrypted = bytes(a ^ b for a, b in zip(encrypted_data, cycle(self.key)))
        return decrypted.decode()

if __name__ == "__main__":
    draco = DracoCipher()
    
    # Simulate Oakley Telemetry
    raw_telemetry = "PUPIL: 3.2mm | TARGET: M32_ARCHES | THREAT: 0"
    print(f"\n[EYE NODE] Raw: {raw_telemetry}")
    
    # Encrypt
    scrambled = draco.encrypt_stream(raw_telemetry)
    print(f"[📡 AIRWAVES] Intercepted Data: {scrambled.hex()}")
    
    # Decrypt at the Pi 5
    recovered = draco.decrypt_stream(scrambled)
    print(f"[PI 5 CORE] Recovered: {recovered}")
