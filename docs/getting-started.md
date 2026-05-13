# Getting Started with Lily-Pi

This guide covers the core Lily-Pi HUD prototype path in this repository.

> Read `docs/safety-and-legal.md` before hardware use.

## 1) Clone and enter project

```bash
git clone https://github.com/Cassai2026/Lily-Pi.git
cd Lily-Pi
```

## 2) Create environment and install minimal dependencies

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-minimal.txt
```

## 3) Run deterministic demo (investor-safe flow)

```bash
python main.py --demo-seconds 20 --no-clear
```

Expected behavior:
- HUD loop boots
- Simulated telemetry streams in terminal
- A deterministic alert is emitted during the run
- Events are written to `logs/audit.json`

## 4) Run continuous prototype mode

```bash
python main.py
```

Press `Ctrl+C` to stop.

## Notes

- Core runtime files are in `main.py` and `core/`.
- The broader `Genesis_Ecosystem/` directories are separate workstreams and not required for core HUD execution.
