# Lily-Pi
## Modular Safety-Assist HUD Prototype for Helmet Use

Lily-Pi is an early-stage prototype focused on one product outcome:
**a modular, low-latency helmet HUD that ingests sensor signals, runs simple safety checks, and logs telemetry for review.**

> Prototype status: simulation-first with progressive hardware integration.

---

## Investor Demo (Deterministic, < 3 minutes)

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-minimal.txt
python main.py --demo-seconds 20 --no-clear
```

Demo flow:
1. Boot HUD loop
2. Sensor ingest (simulated IMU/GPS + system monitor)
3. Rule-based alert trigger
4. Telemetry persisted to `logs/audit.json`

---

## Golden Path Commands

Install:
```bash
pip install -r requirements-minimal.txt
```

Run:
```bash
python main.py
```

Demo:
```bash
python main.py --demo-seconds 20 --no-clear
```

---

## Project Scope (This Repository)

- `main.py` — runtime entrypoint
- `core/` — drivers, bridge logic, and monitoring
- `config.yaml` — runtime thresholds and telemetry settings
- `docs/` — setup, safety, and contribution guidance
- `hardware/` — BOM and integration documentation

`Genesis_Ecosystem/` contains broader ecosystem workstreams and is not required for the core Lily-Pi HUD demo path.

---

## Safety and Compliance

This project is experimental and not road-certified.
Read `/home/runner/work/Lily-Pi/Lily-Pi/docs/safety-and-legal.md` before building or operating hardware.

---

## Dependencies

- `requirements-minimal.txt` — minimal runtime dependencies for core HUD loop/demo.
- `requirements.txt` — legacy/full dependency snapshot (includes optional platform-specific packages).

