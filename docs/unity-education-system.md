# Unity Education System Migration Plan (Implemented Foundation)

Last updated: 2026-05-17

## 1) Product Scope

### Target users
- Primary: learners aged 8–14.
- Secondary: teachers/parents monitoring progression and engagement.

### Learning format
- Primary mode: single-player guided lessons with adaptive tutor prompts.
- Optional mode: guided tutor supervision using teacher/parent dashboards.

### Subject starter set (MVP)
- Scientific reasoning (cause/effect, material behavior, energy transfer).
- Computational reasoning (sequence, logic mapping, rule outcomes).
- Reflective communication (explain observations in plain language).

### Assessment style
- Formative micro-assessments embedded in lessons.
- Keyword and concept-match checks for short responses.
- Mastery progression tiers: Novice → Developing → Confident.

### Connectivity constraints
- Offline-first lesson execution and local save state.
- Online sync optional for analytics and classroom integrations.

---

## 2) Unity Architecture Boundaries

## Moves into Unity
- Core lesson gameplay scenes and interaction loops.
- On-screen adaptive scaffolding and emotional tone feedback UI.
- Session state machine for learning, assessment, progression, and reflection loops.

## Remains in Python/backend layer (this repository)
- Telemetry schema reference and local audit persistence conventions.
- Rule logic prototypes for tutoring/scaffolding behavior.
- Service adapters for external APIs (Google education services bridge).

## Boundary contract
- Unity is the player-facing runtime.
- Python services provide optional analytics, persistence, and integration endpoints.
- Communication contract is event-based JSON payloads.

---

## 3) Mapping Existing Modules to Unity Features

| Existing module | Current role | Unity feature mapping |
|---|---|---|
| `game_engine/teacher_core.py` | Step-by-step lesson prompting + frustration response | Guided lesson presenter + dynamic tone controller |
| `game_engine/edu_scaffold.py` | Learning gap detection + challenge pacing | Hint/scaffold manager with adaptive challenge ladder |
| `game_engine/socratic_engine.py` | Socratic questioning + response evaluation | Adaptive question engine + formative assessment checks |

---

## 4) Minimal MVP Spec (Four Loops)

1. **Learning loop**
   - Present one objective.
   - Ask learner to observe/act.
   - Provide scaffold step when complexity threshold is high.

2. **Assessment loop**
   - Ask one adaptive question tied to objective.
   - Evaluate response against expected concept tokens.
   - Record success/failure with confidence delta.

3. **Progression loop**
   - Update mastery score and level.
   - Unlock next challenge only after minimum mastery threshold.

4. **Feedback loop**
   - Surface immediate reflective coaching.
   - Capture learner sentiment and frustration indicators.
   - Emit telemetry events for downstream analytics.

---

## 5) Data Model and Telemetry Contract

## Core entities
- `LearnerProfile`: learner id, age band, grade band, current mastery score, level.
- `LessonState`: lesson id, objective, complexity, attempt count, completion status.
- `SessionEvent`: timestamp, learner id, event type, payload.

## Required session events
- `lesson_started`
- `scaffold_applied`
- `question_asked`
- `response_evaluated`
- `progress_updated`
- `feedback_presented`
- `lesson_completed`

## Minimum payload fields
- `session_id`, `learner_id`, `lesson_id`, `event_type`, `event_ts`, `metadata`.

---

## 6) Google Educational Integration Path

## Integration areas
- Authentication: Google Sign-In / OAuth for learner and educator identities.
- Classroom roster + assignment sync: Google Classroom APIs.
- Optional content links: Google Drive/Docs references for guided materials.

## Integration sequence
1. Add identity and consent flow.
2. Add roster/assignment read-only sync.
3. Add progress write-back for completed lesson artifacts.
4. Add admin controls for teacher-scoped classroom mappings.

## Safety and privacy requirements
- Least-privilege scopes only.
- Explicit guardian/administrator consent for minors.
- Pseudonymized analytics where possible.

---

## 7) Delivery Phases

### Phase 1 (implemented now)
- Unity-aligned vertical-slice logic added in Python for contract validation:
  - Learning loop
  - Assessment loop
  - Progression loop
  - Feedback loop
- Telemetry event contract implemented and test-covered in repo.

### Phase 2
- Expand adaptive mechanics and emotional-state-aware scaffolding.

### Phase 3
- Add backend/API bridge and persistent learner/session storage.

### Phase 4
- Add analytics views and teacher/parent monitoring surfaces.

---

## 8) Acceptance Criteria by Phase

### Phase 1
- One complete lesson cycle runs end-to-end.
- Mastery score updates deterministically from assessment results.
- Session events are emitted for all required event types.

### Phase 2
- Adaptive hinting changes based on complexity and stress indicators.
- Question selection adapts to prior learner responses.

### Phase 3
- Session save/load stable across restarts.
- API bridge handles success/error cases with schema validation.

### Phase 4
- Teacher/parent views show learner progression and session summaries.
- Integration tests validate dashboard metrics against raw telemetry.

---

## 9) Phase-1 Execution Notes

This repository now contains a phase-1 vertical-slice implementation in:
- `/home/runner/work/Lily-Pi/Lily-Pi/game_engine/education_system_phase1.py`

It operationalizes the four-loop MVP and emits JSON-ready telemetry events, providing the migration contract Unity can consume or mirror.
