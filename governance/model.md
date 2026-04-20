# Lily Pi Dimensional AI Governance Framework

> *Adapted from the Enki AI Thesis — a living framework for neurodivergent-first, sovereign AI design.*

---

## 1. Overview

The Lily Pi governance model is grounded in a **dimensional AI governance framework** — a multi-layered approach to designing and operating AI systems that centre the needs of neurodivergent, marginalised, and adaptive users. Rather than treating governance as a set of static compliance checkboxes, this framework treats it as a **living architecture** that evolves alongside its community.

Lily Pi is the edge-node implementation of the Enki AI sovereign cloud cluster. Every design decision — from how data is cached in RAM and never written to persistent storage, to how the HUD presents information — is an expression of this governance model.

---

## 2. The Dimensional Model

The framework operates across **five interconnected governance dimensions**:

### Dimension 1 — Sovereignty & Data Autonomy
Users own their data absolutely. The ephemeral-cache design (tmpfs RAM disk, no persistent write) is a direct technical implementation of this principle. No usage profile is built without active, informed consent. The system cannot be coerced into surveillance by default hardware configurations.

| Principle | Implementation |
|---|---|
| Zero persistent logging | RAM-only AI cache, wiped on power cycle |
| Consent-first telemetry | All cloud sync requires explicit user opt-in |
| Right to erasure | Power cycle = full local data erasure |

### Dimension 2 — Neurodivergent-First Design
Standard interface paradigms are designed for neurotypical users. Lily Pi inverts this assumption. The HUD and kiosk launcher are tuned for:

- **Reduced cognitive load** — minimal UI chrome, high-contrast modes, single-focus task framing
- **Sensory regulation** — adjustable display brightness, haptic feedback profiles, noise-cancellation defaults
- **Non-linear navigation** — users can move through information in any order without penalty or confusion states
- **Patience-oriented AI responses** — Enki AI is instructed to never rush, truncate, or time-out a user session

### Dimension 3 — Bias Auditing & Fairness
The Enki AI language model pipeline includes periodic bias audits across protected characteristics. For Lily Pi specifically:

- Response quality is tested against simulated neurodivergent query patterns (echolalic phrasing, non-standard grammar, emotion-first communication)
- Outputs are reviewed for ableist language markers
- The community of the 47,000 (the target user base) has a formal feedback pathway into audit cycles
- Bias findings are published openly in this repository under `governance/`

### Dimension 4 — Trauma-Informed Interaction
AI systems interacting with neurodivergent users must acknowledge that many have histories of institutional harm from technology and healthcare. The trauma-informed dimension mandates:

- **No dark patterns** — the system never manipulates, guilts, or nudges users against their stated preferences
- **Predictability** — the system behaves consistently; surprises are announced in advance
- **Soft exits** — users can pause, suspend, or leave any interaction at any time with no negative consequence
- **Non-pathologising language** — the AI does not frame neurodivergence as a problem to be solved

### Dimension 5 — Transparency & Explainability
The AR/HUD layer surfaces AI reasoning where it is useful. Users can ask "why did you say that?" and receive a plain-English explanation of the model's logic and confidence level. All governance documents (including this file) are versioned in Git and publicly readable.

---

## 3. The Enki AI Connection

Lily Pi is not a standalone device — it is an **edge node in the Enki AI sovereign cloud cluster**. The governance framework applies at both layers:

```
┌─────────────────────────────────────────────────────┐
│              ENKI AI SOVEREIGN CLUSTER               │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  │
│  │ Bias Audit  │  │ Policy Engine│  │ Consent DB │  │
│  └─────────────┘  └──────────────┘  └────────────┘  │
└────────────────────────┬────────────────────────────┘
                         │  Encrypted API Bridge
                         │  (cloud_bridge/)
┌────────────────────────▼────────────────────────────┐
│                  LILY PI EDGE NODE                   │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  │
│  │  RAM Cache  │  │  HUD / Kiosk │  │ Local Auth │  │
│  │  (tmpfs)    │  │  (ui/)       │  │            │  │
│  └─────────────┘  └──────────────┘  └────────────┘  │
└─────────────────────────────────────────────────────┘
```

The Policy Engine in the Enki cluster enforces the dimensional model for every API response. The Lily Pi edge node enforces it at the hardware and UX layer. Together they form a **closed governance loop**.

---

## 4. User Autonomy Guarantees

The framework makes the following binding commitments to every Lily Pi user:

1. **You control your data.** It lives in RAM. You can destroy it instantly by unplugging the device.
2. **You control the pace.** No session timeout. No "are you still there?" prompts.
3. **You control the interface.** Display, audio, haptic, and cognitive-load settings are user-editable and persist only if the user explicitly saves them.
4. **You control the model's voice.** Users can flag uncomfortable responses and those flags feed back into the bias audit cycle.
5. **You can read the rules.** All governance documents are open, versioned, and written in plain English (see `governance/policy.md`).

---

## 5. Fairness Metrics

The following metrics are tracked and published per audit cycle:

| Metric | Target | Audit Frequency |
|---|---|---|
| Response parity across neurotype profiles | ≥ 95% equivalent quality | Quarterly |
| Ableist language incidence rate | < 0.5% of sampled responses | Quarterly |
| User-reported discomfort incidents | Trending downward | Continuous |
| Dark-pattern audit findings | Zero tolerance | Per release |
| Consent flow completion rate | ≥ 99% | Per release |

---

## 6. Living Document Commitment

This model is not frozen. It will be updated as:

- The user community provides feedback
- Bias audits reveal new findings
- The Enki AI thesis is revised
- Regulatory or ethical best practices evolve

All changes are tracked in Git history. Major revisions trigger a community review period of at least 14 days before merging.

---

## 7. Cross-Reference: Helmet / HUD Platform

The physical Lily Pi helmet/HUD implementation benefits from this governance framework in the following specific ways:

- **Fairness:** The HUD renders information equivalently regardless of the user's neurotype profile stored in session
- **User Autonomy:** Physical controls (buttons, toggles) always override software-driven UI states — hardware consent is never bypassed by code
- **Bias Check:** AR overlays sourced from Enki AI are tagged with confidence scores and audit-cycle dates, so users know how fresh and reviewed the information is
- **Transparency:** A persistent "governance indicator" in the HUD corner shows the current policy version and last audit date
- **Trauma Safety:** The HUD supports a one-touch "quiet mode" that dims all AI-generated content and surfaces only the user's pre-configured safe defaults

---

*See also: [`governance/policy.md`](./policy.md) for human-readable guidelines | [`governance/architecture.png`](./architecture.png) for system diagram*
