#!/bin/bash
# 🏺 LILY-PI: PRODUCTION ROLLOUT INSTALLER
echo "--- INITIALIZING SOVEREIGN NODE 29 ---"

# 1. Update & Hardening
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y python3-pip python3-opencv libcamera-dev vlc screen 

# 2. Install the Enki-AI Muscle
pip3 install numpy requests beautifulsoup4 googletrans==4.0.0-rc1 opencv-python

# 3. Establish the Ephemeral Shield (RAM-Disk)
sudo mkdir -p /mnt/lilieth_cache
if ! grep -q "/mnt/lilieth_cache" /etc/fstab; then
  echo "tmpfs /mnt/lilieth_cache tmpfs defaults,noatime,size=512M 0 0" | sudo tee -a /etc/fstab
fi
sudo mount -a

# 4. Set Permissions
chmod +x core/ram_wipe.sh
chmod +x ui/kiosk_launcher.sh

echo "--- SHIELD ACTIVE. MUSCLE INSTALLED. OUSH. ---"
