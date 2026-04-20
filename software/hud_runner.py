#!/usr/bin/env python3
"""
Lily Pi — Main HUD Runner
=========================
Entry-point for the Lily Pi smart helmet heads-up display.

Runs the main event loop that:
  1. Reads sensor data (GPS, IMU, etc.)
  2. Queries Enki AI for contextual intelligence
  3. Renders output to the display (OLED / LED ring)

Compatible with: Raspberry Pi 4/5, NVIDIA Jetson Nano/Orin
Python   : 3.9+
License  : MIT
"""

from __future__ import annotations

import logging
import os
import signal
import sys
import time
from typing import Any

# ---------------------------------------------------------------------------
# Optional hardware imports — gracefully degraded on non-Pi systems
# ---------------------------------------------------------------------------
try:
    import board  # type: ignore
    import busio  # type: ignore
    HARDWARE_AVAILABLE = True
except ImportError:
    HARDWARE_AVAILABLE = False
    logging.warning("Hardware libraries not found — running in simulation mode.")

from enki_bridge import EnkiBridge
from display_example import OLEDDisplay, LEDRing

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("lily-pi.hud")

# ---------------------------------------------------------------------------
# Configuration (override via environment variables)
# ---------------------------------------------------------------------------
ENKI_API_URL: str = os.getenv("ENKI_API_URL", "http://localhost:8080")
LOOP_HZ: float = float(os.getenv("HUD_LOOP_HZ", "10"))  # target frames per second
LOOP_INTERVAL: float = 1.0 / LOOP_HZ

_RUNNING = True


def _handle_signal(signum: int, _frame: Any) -> None:
    """Graceful shutdown on SIGINT / SIGTERM."""
    global _RUNNING
    log.info("Received signal %d — shutting down …", signum)
    _RUNNING = False


# ---------------------------------------------------------------------------
# Sensor stubs (replace with real driver calls)
# ---------------------------------------------------------------------------

def read_gps() -> dict[str, float]:
    """Return current GPS data.  Replace body with real GPS driver."""
    # Example: use gpsd or serial NMEA parser
    return {"lat": 0.0, "lon": 0.0, "speed_kmh": 0.0}


def read_imu() -> dict[str, float]:
    """Return IMU data (pitch / roll / yaw in degrees)."""
    # Example: use smbus2 to read MPU-6050 registers
    return {"pitch": 0.0, "roll": 0.0, "yaw": 0.0}


# ---------------------------------------------------------------------------
# HUD state machine
# ---------------------------------------------------------------------------

class HUDRunner:
    """Main HUD coordinator."""

    def __init__(self) -> None:
        self.enki = EnkiBridge(api_url=ENKI_API_URL)
        self.display = OLEDDisplay()
        self.leds = LEDRing()
        self._frame = 0

    def setup(self) -> None:
        log.info("Initialising Lily Pi HUD (loop @ %.1f Hz) …", LOOP_HZ)
        self.display.setup()
        self.leds.setup()
        self.display.show_text("Lily Pi\nBooting…")
        time.sleep(1)

    def step(self) -> None:
        """Execute one HUD frame."""
        self._frame += 1

        # 1. Read sensors
        gps = read_gps()
        imu = read_imu()

        # 2. Build context string
        context = (
            f"Speed: {gps['speed_kmh']:.0f} km/h | "
            f"Pitch: {imu['pitch']:.1f}° Roll: {imu['roll']:.1f}°"
        )

        # 3. Periodic AI query (every 50 frames ≈ 5 s at 10 Hz)
        ai_message = ""
        if self._frame % 50 == 0:
            try:
                ai_message = self.enki.query(
                    f"Helmet HUD status update. {context}. Any hazards?"
                )
                log.info("Enki: %s", ai_message)
            except Exception as exc:  # pylint: disable=broad-except
                log.warning("Enki query failed: %s", exc)

        # 4. Render to display
        lines = [context]
        if ai_message:
            # Truncate to fit OLED width
            lines.append(ai_message[:21])
        self.display.show_text("\n".join(lines))

        # 5. Update LED ring based on speed
        speed = gps["speed_kmh"]
        if speed > 80:
            self.leds.set_color(255, 0, 0)   # red — high speed alert
        elif speed > 40:
            self.leds.set_color(255, 165, 0)  # orange — moderate speed
        else:
            self.leds.set_color(0, 255, 0)    # green — normal

    def teardown(self) -> None:
        log.info("Tearing down HUD …")
        self.display.clear()
        self.leds.off()


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main() -> None:
    signal.signal(signal.SIGINT, _handle_signal)
    signal.signal(signal.SIGTERM, _handle_signal)

    hud = HUDRunner()
    hud.setup()

    log.info("HUD running. Press Ctrl+C to stop.")

    try:
        while _RUNNING:
            t_start = time.monotonic()
            hud.step()
            elapsed = time.monotonic() - t_start
            sleep_time = LOOP_INTERVAL - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)
    finally:
        hud.teardown()
        log.info("Lily Pi HUD stopped cleanly.")


if __name__ == "__main__":
    main()
