import os
import sys

# Get the absolute path of where this script actually lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

def ignition():
    print(f"--- [IGNITION] Node 29 Booting from Sovereign Path: {BASE_DIR} ---")
    # Add actual subprocess calls here later
    
if __name__ == "__main__":
    ignition()
