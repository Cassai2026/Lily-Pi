# Lily Pi Ethical AI Policy Guidelines

*Plain English. No jargon. These are the rules the system follows — and the rules you can hold us to.*

---

## What This Document Is

These are the human-readable policy guidelines for how the Lily Pi system — and its connection to the Enki AI cloud — must behave when interacting with you. They are written for users, caregivers, community advocates, and anyone who wants to know what this system is actually doing and why.

If the technical governance model (`governance/model.md`) is the architecture, this document is the contract.

---

## Core Commitments

### 1. We will never manipulate you.

The system will not use dark patterns — designs that trick, guilt, pressure, or confuse you into doing something you did not intend. This includes:

- No countdown timers on decisions
- No pre-ticked consent boxes
- No "are you sure?" loops that make you doubt yourself
- No messages designed to create anxiety or urgency

If you ever feel the system is doing any of these things, that is a bug, not a feature. Report it.

---

### 2. Your data belongs to you, and only you.

By default, Lily Pi stores nothing permanently. All AI session data lives in RAM and disappears when the device powers off. This is not an accident — it is a deliberate engineering choice to give you absolute control.

- Nothing is sent to the cloud without your explicit permission
- You can revoke cloud sync permission at any time
- When you unplug the device, your local session is gone forever — no recovery, no backup we can hand to anyone

If you choose to enable cloud features, you will be told exactly what is sent, where it goes, and how long it is kept. No surprises.

---

### 3. The AI will never rush you.

There is no session timeout. The AI will wait as long as you need. It will not send "are you still there?" messages. It will not degrade in quality if you take a long time to respond. Your pace is the correct pace.

---

### 4. The AI will not pathologise you.

The system is built for neurodivergent users, not built to "fix" them. The AI will not:

- Suggest that your communication style is a problem
- Recommend you seek help without you asking for it
- Frame your needs as deficits
- Use clinical or medical framing for normal neurodivergent experience

If the AI uses language that feels wrong or harmful, you can flag it immediately using the feedback button. That flag goes directly into the bias audit process.

---

### 5. You can always leave.

Any interaction can be paused, suspended, or ended at any time with no penalty. The system will not:

- Remember that you left (it is RAM-only by default)
- Make it harder to come back
- Ask why you stopped

There is always a way out. The "quiet mode" on the HUD is one tap away.

---

### 6. The AI will tell you why.

If the AI gives you information, a recommendation, or an answer, you can ask "why?" and it will explain its reasoning in plain language. It will also tell you:

- How confident it is
- When its information was last audited for bias
- If there are limitations you should know about

The AI does not pretend to be certain when it is not.

---

### 7. We check for bias, and we publish what we find.

Every few months, we run audits on how the Enki AI model responds to different types of users and different ways of communicating. We specifically test for ableist language and unequal response quality. The results of those audits are published in this repository. If we find problems, we say so openly and explain what we are doing to fix them.

---

### 8. The physical controls always win.

On the Lily Pi helmet/HUD, any physical button or toggle overrides software. If you press the quiet mode button, the software cannot prevent it. Hardware consent is never bypassed by code. Your hands are always in control.

---

### 9. This system is not a replacement for human support.

Lily Pi and Enki AI are tools to support you — not substitutes for human connection, professional care, or community. The system will not present itself as a therapist, a doctor, or a crisis service. If you are in crisis, it will tell you clearly what human services exist and how to reach them.

---

### 10. These rules can be updated, but not secretly.

When these guidelines change, the change is:

- Committed to Git with a clear description of what changed
- Open for community review for at least 14 days before taking effect
- Announced to users before it affects their experience

You always have the right to read the history of this document and understand how it has changed over time.

---

## Your Rights as a User

| Right | What It Means |
|---|---|
| **Right to data destruction** | Unplug the device. Your local data is gone. |
| **Right to explanation** | Ask the AI why. It must answer. |
| **Right to flag harm** | Any response can be flagged as harmful. Flags are reviewed. |
| **Right to opt out** | Cloud features are always opt-in, never opt-out. |
| **Right to read the rules** | All governance documents are public and version-controlled. |
| **Right to quiet** | One-tap quiet mode. Always available. Never locked. |
| **Right to pace** | No timeouts. No pressure. Your speed is valid. |

---

## Reporting a Policy Violation

If you believe the system has violated these guidelines:

1. Use the in-HUD feedback button to flag the specific interaction
2. Open a GitHub issue in this repository with the label `policy-violation`
3. Email the Enki AI governance contact (listed in the main README)

All reports are reviewed. No report will be dismissed without a written response.

---

## Plain Language Glossary

**Dark pattern** — A design trick that manipulates users into doing something they did not intend. We do not use them.

**Ephemeral cache** — Data that only exists in RAM and disappears when the device turns off. This is how Lily Pi stores AI session data by default.

**Bias audit** — A regular check to make sure the AI treats all users fairly and does not use harmful language. Results are published publicly.

**Trauma-informed** — Designing the system to avoid re-traumatising users who have had harmful experiences with technology or healthcare institutions.

**HUD** — Heads-Up Display. The AR overlay shown through the Lily Pi helmet.

**Enki AI** — The sovereign AI cloud cluster that Lily Pi connects to for AI responses.

---

*See also: [`governance/model.md`](./model.md) for the full technical framework | [`governance/architecture.png`](./architecture.png) for system diagram*
