#!/bin/bash
# Bypass Desktop Bloat - Launch Enki HUD Directly
xset -dpms
xset s off
openbox-session &
python3 game_engine/ACD_interface.py --kiosk
