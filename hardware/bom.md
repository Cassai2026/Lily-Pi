# 📋 Lily Pi — Bill of Materials (BOM)

> Last updated: 2026-04
> Currency: USD (approximate retail pricing)

---

## Core Computing

| # | Component | Part Number / Model | Qty | Unit Price | Notes |
|---|-----------|---------------------|-----|------------|-------|
| 1 | Single-Board Computer | Raspberry Pi 4 Model B (4 GB) | 1 | ~$55 | Or Pi 5 / Jetson Nano |
| 2 | microSD Card | Samsung EVO Plus 64 GB | 1 | ~$12 | Class 10 / A2 speed class |
| 3 | USB-C Power Cable | Anker 3A USB-C | 1 | ~$8 | For bench testing |

---

## Display

| # | Component | Part Number / Model | Qty | Unit Price | Notes |
|---|-----------|---------------------|-----|------------|-------|
| 4 | OLED Display | SSD1306 0.96″ I²C 128×64 | 1 | ~$5 | Primary HUD display |
| 5 | LED Ring | NeoPixel 12-LED WS2812B | 1 | ~$8 | Status & alert ring |
| 6 | Transparent Visor Insert | 60 mm × 40 mm acrylic | 1 | ~$3 | DIY beam-splitter |

---

## Sensors

| # | Component | Part Number / Model | Qty | Unit Price | Notes |
|---|-----------|---------------------|-----|------------|-------|
| 7 | IMU | MPU-6050 6-axis | 1 | ~$4 | Head tilt / motion |
| 8 | GPS Module | u-blox NEO-M8N | 1 | ~$18 | Speed & position |
| 9 | Camera | Raspberry Pi Camera Module v3 | 1 | ~$25 | AI vision input |
| 10 | Microphone | I²S MEMS (INMP441) | 1 | ~$6 | Voice commands |

---

## Power

| # | Component | Part Number / Model | Qty | Unit Price | Notes |
|---|-----------|---------------------|-----|------------|-------|
| 11 | Li-Po Battery | 3.7 V 3000 mAh (flat pack) | 1 | ~$12 | Main power source |
| 12 | BEC / Boost Converter | 5 V 3 A USB-C boost module | 1 | ~$6 | Regulates Li-Po → 5 V |
| 13 | Power Switch | SPDT slide switch | 1 | ~$1 | Inline on battery + line |
| 14 | USB-C Port | Panel-mount USB-C receptacle | 1 | ~$4 | Charging port |

---

## Connectors & Passive Components

| # | Component | Spec | Qty | Unit Price |
|---|-----------|------|-----|------------|
| 15 | Dupont jumper wires | 15 cm F–F | 20 | ~$3 (pack) |
| 16 | Resistors | 330 Ω (NeoPixel data) | 2 | ~$0.10 each |
| 17 | JST-PH 2-pin | Battery connector | 2 | ~$0.50 each |
| 18 | Header pins | 2.54 mm 40-pin strip | 1 | ~$1 |

---

## 3-D Printing

| # | Item | Material | Mass (approx) | Notes |
|---|------|----------|---------------|-------|
| 19 | Pi visor mount | PETG | ~30 g | See `hardware/3d-models/` |
| 20 | OLED bezel | PETG | ~12 g | |
| 21 | Battery rear mount | PETG | ~20 g | |

---

## Estimated Total Cost

| Tier | Components | Est. Cost |
|------|-----------|-----------|
| Minimal (OLED only) | Items 1–4, 11–13, 15–18 | **~$110** |
| Standard build | All items above | **~$175** |
| Advanced (Jetson Nano) | Replace #1 with Jetson Nano | **~$220** |

> Prices are approximate and vary by region and supplier. Check Adafruit, SparkFun, Pimoroni, AliExpress, or Mouser for current pricing.

---

## Sourcing Links

- [Adafruit](https://www.adafruit.com)
- [SparkFun](https://www.sparkfun.com)
- [Pimoroni](https://shop.pimoroni.com)
- [AliExpress](https://www.aliexpress.com) *(longer shipping times)*
- [Mouser Electronics](https://www.mouser.com)
