import os
import subprocess
import sys

# Get the absolute path of where this script actually lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

def ignition():
    print(f"--- [IGNITION] Node 29 Booting from Sovereign Path: {BASE_DIR} ---")
    target = os.path.join(BASE_DIR, "main.py")
    subprocess.run([sys.executable, target], check=False)
    
if __name__ == "__main__":
    ignition()
