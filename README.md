# Lily-Pi
Lilieth / enki for Pi
# 🏺 LILIETH PI: The Ephemeral Edge Node
**Status:** Active | **License:** Sovereign (GPLv3 / CC BY-NC) | **Node:** 29

## The Mandate
This repository contains the architecture to flash a standard Raspberry Pi into a **Lilieth Sovereign Node**. It is designed to provide Zero-Lag, neurodivergent-first AI access to the 47,000 without relying on expensive corporate hardware. 

## The "Ephemeral Cache" Engineering
To protect the hardware and ensure absolute data sovereignty, this OS does not write AI cache to the SD card. 
1. The Pi utilizes a `tmpfs` RAM Disk for all cloud-sync operations.
2. It fetches the data from the Enki-AI Cloud/Local Cluster.
3. Upon power cycle, the RAM disk evaporates. The system remains permanently fresh. No bloat. No "Rinse."

## Folder Structure
* `/core` - The RAM Disk and hardware preservation logic.
* `/cloud_bridge` - The API handshake to the Sovereign Cloud Cluster.
* `/ui` - The Zero-Friction Kiosk launcher for the Enki-AI HUD.

**"The past is wiped. The future is coded. OUSH."**
