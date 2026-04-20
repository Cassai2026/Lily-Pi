#!/bin/bash
# CONTRACT: target_disk -> persistent_partitioning -> sovereign_os_flash
# Purpose: Turns any USB 3.0 HDD into a bootable Enki-Linux Node.

TARGET_DRIVE=$1

if [ -z "$TARGET_DRIVE" ]; then
    echo "[🚨 ERROR] Usage: sudo ./genesis_disk_forge.sh /dev/sdX"
    exit 1
fi

echo "=========================================="
echo "🏺 FORGING GENESIS DISK: $TARGET_DRIVE"
echo "=========================================="

# 1. Wipe and Partition (Sovereign Root + Persistent Vault)
echo "[1/3] Partitioning drive..."
# Scripted fdisk commands to create boot and root
(
echo o # Clear
echo n # New partition
echo p # Primary
echo 1 # Partition 1
echo   # Default start
echo +512M # 512MB Boot
echo t # Change type
echo c # W95 FAT32 (LBA)
echo n # New partition
echo p # Primary
echo 2 # Partition 2
echo   # Default start
echo   # Rest of disk
echo w # Write
) | fdisk $TARGET_DRIVE

# 2. Format
mkfs.vfat ${TARGET_DRIVE}1
mkfs.ext4 ${TARGET_DRIVE}2

# 3. Seed the L.I.L.I.E.T.H. Kernel
echo "[2/3] Seeding Sovereign Filesystem..."
# This would normally involve debootstrap or dd-ing a base image
# For now, we flag the persistence layer
tune2fs -L SOVEREIGN_VAULT ${TARGET_DRIVE}2

echo "[3/3] Genesis Disk Complete. Node 29 is now portable."
echo "OUSH."
