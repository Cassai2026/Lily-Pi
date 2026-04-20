# 🖨️ Lily Pi — 3-D Printable Models

This folder contains printable mounts, enclosures, and brackets for integrating
Lily Pi hardware into various helmet types.

## File Formats

| Format | Purpose |
|--------|---------|
| `.stl`  | Ready-to-slice mesh for FDM printers |
| `.step` | Parametric CAD for Fusion 360 / FreeCAD editing |
| `.3mf`  | Pre-configured print files (Bambu Studio / PrusaSlicer) |

## Available Models

> 🚧 Models are in development. Community-contributed files are welcome!

| Model | Description | Status |
|-------|-------------|--------|
| `raspberry-pi-visor-mount.stl`    | Pi Zero / Pi 4 slim visor clip       | Planned |
| `oled-bezel-visor.stl`            | SSD1306 OLED 0.96″ visor bezel        | Planned |
| `led-ring-helmet-band.stl`        | NeoPixel ring helmet-band holder      | Planned |
| `battery-rear-mount.stl`          | Li-Po battery mount for rear padding  | Planned |
| `camera-forehead-bracket.stl`     | Pi Camera v3 / ArduCam forehead mount | Planned |
| `full-enclosure-bike-helmet.stl`  | Full electronics bay for bike helmets | Planned |

## Recommended Print Settings

```
Material  : PETG (outdoor durability) or PLA for prototyping
Layer     : 0.2 mm
Infill    : 30–40 % Gyroid
Supports  : Enabled for overhangs > 45°
Perimeters: 3 (for mounting strength)
```

## Contributing Models

1. Export your model in both `.stl` and `.step`
2. Name files using `kebab-case-description.ext`
3. Add an entry to the table above
4. Open a PR — see [docs/contributing.md](../../docs/contributing.md)
