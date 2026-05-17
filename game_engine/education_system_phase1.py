"""Phase-1 vertical slice for a Unity-aligned education system.

This module provides a deterministic four-loop educational runtime contract
that can be mirrored inside Unity while remaining executable in Python.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any

from game_engine.edu_scaffold import EducationalScaffolding
from game_engine.socratic_engine import SocraticTeacher
from game_engine.teacher_core import SovereignTeacher


@dataclass
class LearnerProfile:
    """Represents learner baseline and progression state."""

    learner_id: str
    age_band: str
    grade_band: str
    mastery_score: int = 0
    level: str = "Novice"


@dataclass
class LessonState:
    """Represents the active lesson context for one loop execution."""

    lesson_id: str
    topic: str
    objective: str
    complexity: int
    attempt_count: int = 0
    completed: bool = False


@dataclass
class SessionEvent:
    """Single event emitted by the education runtime."""

    event_type: str
    learner_id: str
    lesson_id: str
    metadata: dict[str, Any]
    event_ts: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


class EducationSystemPhaseOne:
    """Runs a deterministic four-loop educational session contract."""

    def __init__(self) -> None:
        self.scaffold = EducationalScaffolding()
        self.socratic = SocraticTeacher()
        self.teacher = SovereignTeacher()
        self.events: list[SessionEvent] = []

    def _emit(
        self,
        event_type: str,
        learner: LearnerProfile,
        lesson: LessonState,
        metadata: dict[str, Any],
    ) -> None:
        self.events.append(
            SessionEvent(
                event_type=event_type,
                learner_id=learner.learner_id,
                lesson_id=lesson.lesson_id,
                metadata=metadata,
            )
        )

    def learning_loop(self, learner: LearnerProfile, lesson: LessonState) -> list[str]:
        """Run lesson presentation and scaffolding decisions."""
        self._emit(
            "lesson_started",
            learner,
            lesson,
            {"topic": lesson.topic, "objective": lesson.objective},
        )
        self.teacher.deliver_lesson(lesson.topic, user_profile="Learner")

        guidance = self.scaffold.identify_learning_gap(lesson.complexity)
        if guidance != ["Proceed with Autonomy."]:
            self._emit("scaffold_applied", learner, lesson, {"guidance": guidance})
        return guidance

    def assessment_loop(
        self,
        learner: LearnerProfile,
        lesson: LessonState,
        response_keywords: list[str],
        expected_keywords: list[str],
    ) -> bool:
        """Run adaptive questioning and response evaluation."""
        question = self.socratic.ask_question(lesson.topic)
        self._emit("question_asked", learner, lesson, {"question": question})

        lesson.attempt_count += 1
        correct = self.socratic.evaluate_response(response_keywords, expected_keywords)
        self._emit(
            "response_evaluated",
            learner,
            lesson,
            {
                "attempt": lesson.attempt_count,
                "correct": correct,
                "response_keywords": response_keywords,
                "expected_keywords": expected_keywords,
            },
        )
        return correct

    def progression_loop(
        self,
        learner: LearnerProfile,
        lesson: LessonState,
        was_correct: bool,
    ) -> None:
        """Update mastery and completion state."""
        learner.mastery_score += 10 if was_correct else 2
        if learner.mastery_score >= 20:
            learner.level = "Developing"
        if learner.mastery_score >= 50:
            learner.level = "Confident"

        lesson.completed = was_correct
        self._emit(
            "progress_updated",
            learner,
            lesson,
            {
                "mastery_score": learner.mastery_score,
                "level": learner.level,
                "completed": lesson.completed,
            },
        )

    def feedback_loop(
        self,
        learner: LearnerProfile,
        lesson: LessonState,
        stress_level: int,
    ) -> str:
        """Provide immediate reflective feedback based on stress state."""
        mode = self.teacher.sense_frustration({"stress_level": stress_level})
        message = (
            "Take a breath. We can simplify this and try again."
            if mode == "Simplified_Mode"
            else "Great momentum. Ready for the next challenge?"
        )
        self._emit(
            "feedback_presented",
            learner,
            lesson,
            {"mode": mode, "message": message, "stress_level": stress_level},
        )
        return message

    def run_session(
        self,
        learner: LearnerProfile,
        lesson: LessonState,
        response_keywords: list[str],
        expected_keywords: list[str],
        stress_level: int,
    ) -> dict[str, Any]:
        """Execute the full four-loop phase-1 vertical slice."""
        guidance = self.learning_loop(learner, lesson)
        was_correct = self.assessment_loop(
            learner,
            lesson,
            response_keywords=response_keywords,
            expected_keywords=expected_keywords,
        )
        self.progression_loop(learner, lesson, was_correct)
        feedback = self.feedback_loop(learner, lesson, stress_level)

        self._emit(
            "lesson_completed",
            learner,
            lesson,
            {"completed": lesson.completed, "attempts": lesson.attempt_count},
        )

        return {
            "learner": asdict(learner),
            "lesson": asdict(lesson),
            "guidance": guidance,
            "feedback": feedback,
            "events": [asdict(event) for event in self.events],
        }


if __name__ == "__main__":
    runtime = EducationSystemPhaseOne()
    learner_profile = LearnerProfile(
        learner_id="learner-001",
        age_band="8-10",
        grade_band="3-5",
    )
    lesson_state = LessonState(
        lesson_id="lesson-material-001",
        topic="PET_Polymer",
        objective="Explain how heat can change bottle shape.",
        complexity=80,
    )

    session_result = runtime.run_session(
        learner=learner_profile,
        lesson=lesson_state,
        response_keywords=["heat", "shape"],
        expected_keywords=["heat", "deform", "shape"],
        stress_level=45,
    )

    print(
        "[EDU] Phase-1 session complete:",
        {
            "mastery_score": session_result["learner"]["mastery_score"],
            "level": session_result["learner"]["level"],
            "event_count": len(session_result["events"]),
        },
    )
