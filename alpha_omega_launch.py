# CONTRACT: system_start -> process_orchestration -> total_node_ignition
# Purpose: The single master command to boot the entire 10^47 Ecosystem.

import subprocess
import time
import sys
import os

class AlphaOmega:
    def __init__(self):
        self.processes = []
        print("===================================================")
        print("🏺 LILIETH-PI: ALPHA OMEGA GENESIS SEQUENCE INITIATED")
        print("===================================================")

    def launch_subsystem(self, name, command, working_dir="."):
        print(f"[GENESIS] Igniting {name}...")
        try:
            # Popen runs it in the background
            p = subprocess.Popen(command, cwd=working_dir, shell=True)
            self.processes.append((name, p))
            time.sleep(1) # Staggered boot to prevent CPU spiking
        except Exception as e:
            print(f"[🚨 FAULT] Failed to ignite {name}: {e}")

    def ignite_all(self):
        # 1. Boot the 3D God View Dashboard (Port 8080)
        self.launch_subsystem("Mesh God View", "python mesh_dashboard.py", "ui")
        
        # 2. Boot the Ghost Hardware (Simulates the Pi 5 / Oakleys)
        self.launch_subsystem("Ghost Hardware", "python ghost_hardware.py", "hardware")
        
        # 3. Boot the Node Heartbeat
        self.launch_subsystem("Node Heartbeat", "python node_heartbeat.py", ".")
        
        # 4. Boot the Core Sovereign Spine
        self.launch_subsystem("Sovereign Core", "python sovereign_boot.py", ".")
        
        print("\n[GENESIS] ALL SYSTEMS ACTIVE. NODE 29 IS BREATHING.")
        print("[GENESIS] Press Ctrl+C to initiate Ghost Protocol (Shutdown).")

    def shutdown(self):
        print("\n[GHOST PROTOCOL] Terminating all subsystems...")
        for name, p in self.processes:
            p.terminate()
            print(f"[GHOST PROTOCOL] {name} offline.")
        print("[GHOST PROTOCOL] Node 29 has vanished. OUSH.")
        sys.exit(0)

if __name__ == "__main__":
    master = AlphaOmega()
    try:
        master.ignite_all()
        # Keep the main thread alive while subprocesses run
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        master.shutdown()
