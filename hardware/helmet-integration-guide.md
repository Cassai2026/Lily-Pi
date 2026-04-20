# 🔧 Lily Pi — Helmet Integration Guide

This guide walks you through mechanically and electrically integrating the Lily Pi
electronics into a helmet of your choice (bicycle, motorcycle, or industrial).

> ⚠️ Read [docs/safety-and-legal.md](../docs/safety-and-legal.md) **before** you start.

---

## Supported Helmet Types

| Type | Difficulty | Notes |
|------|-----------|-------|
| Bicycle (full-face) | ★★☆ Medium | Most room for electronics |
| Bicycle (open-face) | ★★★ Hard  | Limited space; use Pi Zero |
| Motorcycle (full-face) | ★★☆ Medium | Excellent for OLED + GPS |
| Industrial hard hat | ★☆☆ Easy  | Large brim — easy cable routing |

---

## Tools Required

- Phillips-head screwdriver (PH0, PH1)
- Soldering iron + solder (60/40 or lead-free)
- Hot-glue gun (low-temp)
- Dremel rotary tool or hand drill (for cutouts)
- 3-D printer (or order prints via a print service)
- Digital multimeter

---

## Step 1 — Plan the Layout

Sketch or print the inner liner of your helmet and mark:

1. **Visor / forehead area** — OLED display + camera position
2. **Crown area** — Raspberry Pi + battery (distribute weight symmetrically)
3. **Rear padding** — battery pack (counterweight to Pi at front)
4. **Side channels** — cable routing paths

**Weight budget:**
| Component | Weight |
|-----------|--------|
| Raspberry Pi 4 | ~46 g |
| 3000 mAh Li-Po | ~65 g |
| OLED + mount | ~15 g |
| Camera + bracket | ~12 g |
| Wires + connectors | ~20 g |
| **Total** | **~158 g** |

---

## Step 2 — Print and Test-Fit Mounts

1. Print the required models from `hardware/3d-models/` (PETG recommended)
2. Dry-fit each mount inside the helmet before gluing
3. Check that the OLED sits at the correct eye-level position in the visor

```
Front view (forehead area):
┌────────────────────────┐
│  [ Camera ]  [ OLED ]  │  ← both in printed visor-mount frame
│                        │
└────────────────────────┘
```

---

## Step 3 — Cut Visor Opening (if needed)

For full-face helmets:

1. Mark a 45 mm × 30 mm cutout on the inner visor
2. Cut carefully with a Dremel (wear eye protection)
3. Smooth edges with fine sandpaper
4. Test-fit the OLED bezel printed in Step 2

> **Do not** cut structural EPS foam or the outer shell in a way that compromises
> impact protection. Keep all cutouts to the inner plastic liner only.

---

## Step 4 — Mount and Secure Electronics

1. Attach the Pi mount to the crown area using M3 screws into printed inserts
2. Route the 40-pin ribbon or individual dupont wires through the side channels
3. Secure cables every 5–8 cm with hot-glue dots
4. Attach the OLED bezel to the visor opening with epoxy or M2 screws
5. Place the battery pack in the rear mount and connect the JST-PH connector

---

## Step 5 — Connect Wiring

Follow the diagrams in `hardware/wiring-diagrams/`. Summary:

| Component | Pi GPIO Pin |
|-----------|-------------|
| OLED SDA  | GPIO 2 (Pin 3) |
| OLED SCL  | GPIO 3 (Pin 5) |
| NeoPixel DATA | GPIO 18 (Pin 12) |
| GPS TX    | GPIO 15 / RXD (Pin 10) |
| GPS RX    | GPIO 14 / TXD (Pin 8) |
| IMU SDA   | GPIO 2 (shared I²C bus) |
| IMU SCL   | GPIO 3 (shared I²C bus) |

---

## Step 6 — Flash and Test Software

1. Install Raspberry Pi OS Lite (64-bit) on the microSD
2. Follow [docs/getting-started.md](../docs/getting-started.md) to install Lily Pi software
3. Boot the Pi while powered from the Li-Po pack
4. Run the display example to verify all connections:

```bash
python software/display_example.py
```

5. Run the full HUD:

```bash
python software/hud_runner.py
```

---

## Step 7 — Cable Management & Final Assembly

1. Tuck all cables into the side channels
2. Replace the inner liner padding on top of the electronics
3. Ensure no cables pass through pressure points or create hard spots
4. Close the helmet and do a final visual check

---

## Calibration

After assembly:

```bash
# Test I²C devices are detected
i2cdetect -y 1

# Expected output includes: 0x3C (OLED), 0x68 (IMU)
```

---

## Maintenance & Upgrades

- Recharge Li-Po via the USB-C port on the rear mount — **never** charge inside the helmet
- Check cable integrity monthly
- Re-calibrate IMU after any drop or impact
- See `hardware/bom.md` for replacement part numbers
