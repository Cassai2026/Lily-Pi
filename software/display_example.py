#!/usr/bin/env python3
"""
Lily Pi — Display Example
==========================
Demonstrates driving an SSD1306 OLED display and a NeoPixel (WS2812B) LED ring
from a Raspberry Pi or NVIDIA Jetson.

Hardware:
  • SSD1306 0.96″ 128×64 OLED via I²C (SDA=GPIO2, SCL=GPIO3)
  • NeoPixel 12-LED ring via GPIO 18

Install deps:
  pip install adafruit-circuitpython-ssd1306 adafruit-circuitpython-neopixel \
              pillow board busio

Compatible with: Raspberry Pi 4/5, NVIDIA Jetson Nano/Orin
Python   : 3.9+
License  : AGPL-3.0
"""

from __future__ import annotations

import logging
import time

log = logging.getLogger("lily-pi.display")

# ---------------------------------------------------------------------------
# Try importing hardware libraries; fall back to stubs for development
# ---------------------------------------------------------------------------
try:
    import board  # type: ignore
    import busio  # type: ignore
    import adafruit_ssd1306  # type: ignore
    import neopixel  # type: ignore
    from PIL import Image, ImageDraw, ImageFont  # type: ignore
    _HW = True
except ImportError:
    _HW = False
    log.warning(
        "Hardware display libraries not installed — using stub implementations. "
        "Run: pip install adafruit-circuitpython-ssd1306 "
        "adafruit-circuitpython-neopixel pillow board busio"
    )

# ---------------------------------------------------------------------------
# OLED Display
# ---------------------------------------------------------------------------

OLED_WIDTH = 128
OLED_HEIGHT = 64
OLED_I2C_ADDR = 0x3C
NEOPIXEL_PIN_NAME = "D18"   # GPIO 18
NEOPIXEL_COUNT = 12


class OLEDDisplay:
    """
    SSD1306 OLED 128×64 display wrapper.

    Falls back to a print-based stub when hardware libraries are unavailable.
    """

    def __init__(
        self,
        width: int = OLED_WIDTH,
        height: int = OLED_HEIGHT,
        i2c_addr: int = OLED_I2C_ADDR,
    ) -> None:
        self._width = width
        self._height = height
        self._addr = i2c_addr
        self._oled = None
        self._image: "Image.Image | None" = None
        self._draw: "ImageDraw.ImageDraw | None" = None

    def setup(self) -> None:
        """Initialise I²C bus and display."""
        if not _HW:
            log.info("[STUB] OLEDDisplay.setup() — no hardware")
            return

        i2c = busio.I2C(board.SCL, board.SDA)
        self._oled = adafruit_ssd1306.SSD1306_I2C(
            self._width, self._height, i2c, addr=self._addr
        )
        self._oled.fill(0)
        self._oled.show()

        self._image = Image.new("1", (self._width, self._height))
        self._draw = ImageDraw.Draw(self._image)
        log.info("OLED display initialised (%dx%d @ 0x%02X)", self._width, self._height, self._addr)

    def show_text(self, text: str, x: int = 0, y: int = 0, font_size: int = 12) -> None:
        """
        Render *text* to the OLED display.

        Multi-line text is supported: use ``\\n`` to separate lines.

        Parameters
        ----------
        text:
            String (or multi-line string) to display.
        x, y:
            Top-left pixel position for the first character.
        font_size:
            Font size in points (uses default bitmap font if PIL not available).
        """
        if not _HW:
            print(f"[OLED] {text!r}")
            return

        if self._draw is None or self._oled is None:
            log.error("OLEDDisplay not set up — call setup() first.")
            return

        # Clear
        self._draw.rectangle((0, 0, self._width, self._height), outline=0, fill=0)

        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)
        except (IOError, OSError):
            font = ImageFont.load_default()

        line_height = font_size + 2
        for idx, line in enumerate(text.split("\n")):
            self._draw.text((x, y + idx * line_height), line, font=font, fill=255)

        self._oled.image(self._image)
        self._oled.show()

    def clear(self) -> None:
        """Clear the OLED display."""
        if not _HW:
            print("[OLED] clear")
            return
        if self._oled:
            self._oled.fill(0)
            self._oled.show()


# ---------------------------------------------------------------------------
# NeoPixel LED Ring
# ---------------------------------------------------------------------------

class LEDRing:
    """
    WS2812B NeoPixel LED ring wrapper.

    Falls back to a print-based stub when hardware libraries are unavailable.
    """

    def __init__(
        self,
        pin_name: str = NEOPIXEL_PIN_NAME,
        num_pixels: int = NEOPIXEL_COUNT,
        brightness: float = 0.3,
    ) -> None:
        self._pin_name = pin_name
        self._num_pixels = num_pixels
        self._brightness = brightness
        self._pixels = None

    def setup(self) -> None:
        """Initialise NeoPixel strip."""
        if not _HW:
            log.info("[STUB] LEDRing.setup() — no hardware")
            return

        pin = getattr(board, self._pin_name)
        self._pixels = neopixel.NeoPixel(
            pin,
            self._num_pixels,
            brightness=self._brightness,
            auto_write=False,
        )
        self._pixels.fill((0, 0, 0))
        self._pixels.show()
        log.info("NeoPixel ring initialised (%d LEDs on %s)", self._num_pixels, self._pin_name)

    def set_color(self, r: int, g: int, b: int) -> None:
        """Set all LEDs to (r, g, b)."""
        if not _HW:
            print(f"[LED] set_color({r}, {g}, {b})")
            return
        if self._pixels:
            self._pixels.fill((r, g, b))
            self._pixels.show()

    def off(self) -> None:
        """Turn all LEDs off."""
        self.set_color(0, 0, 0)

    def pulse(self, r: int, g: int, b: int, steps: int = 20, delay: float = 0.03) -> None:
        """Simple fade-in / fade-out pulse effect."""
        if not _HW:
            print(f"[LED] pulse({r}, {g}, {b})")
            return
        if self._pixels is None:
            return
        for i in range(steps):
            factor = i / steps
            self._pixels.fill((int(r * factor), int(g * factor), int(b * factor)))
            self._pixels.show()
            time.sleep(delay)
        for i in range(steps, 0, -1):
            factor = i / steps
            self._pixels.fill((int(r * factor), int(g * factor), int(b * factor)))
            self._pixels.show()
            time.sleep(delay)


# ---------------------------------------------------------------------------
# Demo / standalone test
# ---------------------------------------------------------------------------

def demo() -> None:
    """Run a simple demo when this file is executed directly."""
    logging.basicConfig(level=logging.INFO)

    oled = OLEDDisplay()
    oled.setup()

    leds = LEDRing()
    leds.setup()

    print("=== Lily Pi Display Demo ===")

    # --- OLED test ---
    oled.show_text("Lily Pi\nHUD v0.1\nStarting…")
    time.sleep(1)

    oled.show_text("Speed: 0 km/h\nPitch:  0.0°\nAI: online")
    time.sleep(1)

    # --- LED ring colours ---
    colours = [
        ("Green  (normal)", (0, 255, 0)),
        ("Orange (caution)", (255, 165, 0)),
        ("Red    (alert)", (255, 0, 0)),
        ("Blue   (nav)", (0, 0, 255)),
    ]
    for label, (r, g, b) in colours:
        print(f"  LED → {label}")
        oled.show_text(f"LED Test:\n{label}")
        leds.set_color(r, g, b)
        time.sleep(0.8)

    # --- Pulse effect ---
    print("  LED → pulse effect")
    oled.show_text("LED Test:\nPulse effect")
    leds.pulse(0, 150, 255, steps=15)

    # --- Teardown ---
    oled.show_text("Demo done!\nLily Pi 🪖")
    time.sleep(1)
    oled.clear()
    leds.off()
    print("Demo finished.")


if __name__ == "__main__":
    demo()
