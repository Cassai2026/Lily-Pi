#!/bin/bash
# 🏺 LILIETH PI: Ephemeral Shield
CACHE_DIR="/mnt/lilieth_cache"
echo "tmpfs   $CACHE_DIR   tmpfs   defaults,noatime,size=256M   0   0" | sudo tee -a /etc/fstab
sudo mount -a
echo "[SHIELD] Ephemeral Vault Active. Wiping Static..."
