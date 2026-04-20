# ⚡ Lily Pi — Wiring Diagrams

This folder contains wiring schematics for every Lily Pi sensor and display module.

## Diagram Formats

| Format | Tool |
|--------|------|
| `.fzz` | Fritzing project (open source EDA) |
| `.pdf` | Exported PDF for printing |
| `.svg` | Vector schematic for documentation |

## Available Diagrams

> 🚧 Diagrams are in development. Community contributions are welcome!

| Diagram | Description | Status |
|---------|-------------|--------|
| `core-raspberry-pi.fzz`   | Raspberry Pi 4 pinout overview           | Planned |
| `oled-ssd1306-i2c.fzz`    | OLED display via I²C (SDA/SCL)           | Planned |
| `neopixel-ring.fzz`       | NeoPixel LED ring via GPIO 18            | Planned |
| `gps-uart.fzz`            | GPS module via UART (TX/RX)              | Planned |
| `imu-mpu6050-i2c.fzz`     | MPU-6050 IMU via I²C                     | Planned |
| `camera-csi.fzz`          | Raspberry Pi Camera via CSI ribbon       | Planned |
| `power-distribution.fzz`  | 5 V / 3.3 V power rail from Li-Po pack  | Planned |

## Core GPIO Pinout Reference (Raspberry Pi 4)

```
Raspberry Pi 4 — 40-pin GPIO Header
─────────────────────────────────────────
Pin  1  [ 3.3V ] ─── VCC for OLED, IMU
Pin  2  [ 5V   ] ─── NeoPixel, Camera
Pin  3  [ GPIO2 / SDA ] ─── I²C Data  (OLED, IMU)
Pin  5  [ GPIO3 / SCL ] ─── I²C Clock (OLED, IMU)
Pin  6  [ GND  ] ─── Common Ground
Pin  8  [ GPIO14 / TXD ] ─── GPS RX
Pin 10  [ GPIO15 / RXD ] ─── GPS TX
Pin 12  [ GPIO18      ] ─── NeoPixel DATA
Pin 39  [ GND  ] ─── NeoPixel GND
─────────────────────────────────────────
```

## Safety Notes

- Always check voltage levels before connecting (3.3 V vs 5 V logic)
- Use a 330 Ω resistor in series with the NeoPixel data line
- Power the Pi via a stable BEC / USB-C PD source — do not power from GPIO directly
- See [docs/safety-and-legal.md](../../docs/safety-and-legal.md) for full electrical safety guidance
