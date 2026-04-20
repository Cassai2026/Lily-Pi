# 🚀 Getting Started with Lily Pi

Welcome to **Lily Pi** — the open-source modular AR/AI smart helmet HUD.  
This guide will take you from a fresh clone to a working HUD display in under 30 minutes.

> ⚠️ Before building or wearing any hardware, please read [safety-and-legal.md](safety-and-legal.md).

---

## Prerequisites

### Hardware (minimum viable build)

| Component | Notes |
|-----------|-------|
| Raspberry Pi 4 (2 GB+) or Jetson Nano | Pi Zero 2W also works for display-only |
| SSD1306 0.96″ OLED (I²C) | 128×64 pixels |
| microSD ≥ 16 GB (Class 10) | For the OS |
| 5 V USB-C power source | 3 A minimum for Pi 4 |

See the full [Bill of Materials](../hardware/bom.md) for an advanced build.

### Software

- **Raspberry Pi OS Lite 64-bit** (recommended) or **Ubuntu 22.04 LTS** for Jetson
- Python 3.9 or later
- Git

---

## Step 1 — Flash the OS

1. Download [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
2. Flash **Raspberry Pi OS Lite (64-bit)** to your microSD
3. Before ejecting, click ⚙️ and:
   - Set hostname: `lily-pi`
   - Enable SSH
   - Set your Wi-Fi credentials
4. Insert the card and boot

---

## Step 2 — SSH into your Pi

```bash
ssh pi@lily-pi.local
```

Update the system:

```bash
sudo apt update && sudo apt upgrade -y
```

---

## Step 3 — Enable I²C

```bash
sudo raspi-config
# Navigate to: Interface Options → I2C → Enable
sudo reboot
```

Verify the OLED is detected (address `0x3C`):

```bash
sudo apt install -y i2c-tools
i2cdetect -y 1
```

You should see `3c` in the output grid.

---

## Step 4 — Clone Lily Pi

```bash
git clone https://github.com/Cassai2026/Lily-Pi.git
cd Lily-Pi
```

---

## Step 5 — Install Python Dependencies

```bash
pip install -r software/requirements.txt

# Install hardware libraries (Raspberry Pi)
pip install adafruit-blinka \
            adafruit-circuitpython-ssd1306 \
            adafruit-circuitpython-neopixel
```

For **NVIDIA Jetson**, replace the Adafruit Blinka install with:

```bash
pip install Jetson.GPIO
```

---

## Step 6 — Run the Display Demo

Test that your OLED and LED ring are wired correctly:

```bash
python software/display_example.py
```

You should see "Lily Pi / HUD v0.1 / Starting…" on the OLED and the LED ring
cycle through colours.

---

## Step 7 — Configure Enki AI

Lily Pi uses **[Enki AI](https://github.com/Cassai2026/Enki)** for on-device intelligence.

### Option A — Run Enki locally (recommended)

Follow the Enki AI setup guide in that repo, then:

```bash
# Start Enki on the Pi (or a connected machine)
# Enki listens on http://localhost:8080 by default
```

### Option B — Remote Enki instance

Create a `.env` file in the project root:

```bash
# .env
ENKI_API_URL=http://192.168.1.100:8080
ENKI_API_KEY=your_optional_api_key_here
```

Test the bridge:

```bash
python software/enki_bridge.py "Hello Enki, what hazards should I watch for?"
```

---

## Step 8 — Run the Full HUD

```bash
python software/hud_runner.py
```

The HUD will start at 10 Hz, reading sensors and rendering to the OLED.  
Press **Ctrl+C** to stop cleanly.

---

## Auto-start on Boot (optional)

Create a systemd service:

```bash
sudo tee /etc/systemd/system/lily-pi-hud.service > /dev/null << 'EOF'
[Unit]
Description=Lily Pi HUD
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/Lily-Pi/software/hud_runner.py
WorkingDirectory=/home/pi/Lily-Pi
Restart=always
User=pi
EnvironmentFile=/home/pi/Lily-Pi/.env

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable lily-pi-hud
sudo systemctl start lily-pi-hud
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: board` | Run `pip install adafruit-blinka` |
| OLED shows nothing | Check SDA/SCL wiring; run `i2cdetect -y 1` |
| Enki returns `[Enki offline]` | Check `ENKI_API_URL` and that Enki is running |
| NeoPixels not lighting | Check GPIO 18 wiring; add 330 Ω resistor on data line |
| Pi won't boot | Re-flash microSD with a fresh OS image |

---

## Next Steps

- 📡 Add GPS: see `hardware/wiring-diagrams/gps-uart.fzz`
- 🧩 Add IMU: see `hardware/wiring-diagrams/imu-mpu6050-i2c.fzz`
- 🪖 Mount into a helmet: see `hardware/helmet-integration-guide.md`
- 🤝 Contribute: see [contributing.md](contributing.md)
