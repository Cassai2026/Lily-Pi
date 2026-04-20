class AVSync:
    def __init__(self):
        self.latency_offset = 0.05 # 50ms for the 29th Node speed

    def sync_subtitle(self, audio_timestamp, text):
        # Syncing the bone-conduction audio with the Oakley HUD display
        print(f"[HUD] [Subtitle @ {audio_timestamp}]: {text}")

if __name__ == "__main__":
    sync = AVSync()
    sync.sync_subtitle("00:01", "The past is wiped. The future is coded.")
