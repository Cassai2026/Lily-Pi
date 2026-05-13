# Lily-Pi Investor Brief (Prototype Stage)

## Product Position

Lily-Pi is a modular safety-assist HUD prototype for helmet use.
Current capability focuses on sensor ingest, low-latency alerting logic, and telemetry logging.

## Single Architecture View

**Inputs** (IMU, GPS, system telemetry, optional camera)  
→ **Decision Layer** (threshold/rule logic via Enki bridge)  
→ **HUD Output** (terminal/HUD stream) + **Telemetry Log** (`logs/audit.json`)

### Current maturity labels
- Production-ready foundation: runtime loop, config-driven thresholds, telemetry persistence, deterministic demo mode.
- Prototype-stage: advanced sensor fusion, large-scale field validation, certification-path hardware packaging.

## Demo Narrative (Under 3 Minutes)

1. Start deterministic demo: `python main.py --demo-seconds 20 --no-clear`
2. Show live ingest and HUD status output
3. Show deterministic alert emission
4. Open `logs/audit.json` and show persisted event trail

## Risks and Responsible Positioning

- Experimental prototype, not road-certified.
- Safety/legal constraints explicitly documented in `docs/safety-and-legal.md`.
- Staged deployment path: lab validation → controlled pilot → certification-oriented redesign.

## Pilot Plan (90-Day Outline)

- **Days 0–30:** instrumented prototype validation (latency + stability).
- **Days 31–60:** controlled pilot with selected users/partners.
- **Days 61–90:** certification-gap assessment and pilot outcome report.

## KPI Targets

- Alert precision
- End-to-end latency
- Uptime during session
- Battery/runtime duration under load

## Investment Use of Funds (high-level)

- Hardware iteration and test rigs
- Pilot execution and data collection
- Reliability hardening and certification-prep engineering
