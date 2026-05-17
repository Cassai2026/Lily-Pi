from game_engine.education_system_phase1 import (
    EducationSystemPhaseOne,
    LearnerProfile,
    LessonState,
)


def test_phase_one_session_emits_required_events() -> None:
    runtime = EducationSystemPhaseOne()
    learner = LearnerProfile(
        learner_id="learner-test",
        age_band="11-12",
        grade_band="6-7",
    )
    lesson = LessonState(
        lesson_id="lesson-test",
        topic="PET_Polymer",
        objective="Connect heat with material deformation.",
        complexity=90,
    )

    result = runtime.run_session(
        learner=learner,
        lesson=lesson,
        response_keywords=["heat", "shape"],
        expected_keywords=["heat", "shape", "deform"],
        stress_level=25,
    )

    event_types = [event["event_type"] for event in result["events"]]
    for required in {
        "lesson_started",
        "scaffold_applied",
        "question_asked",
        "response_evaluated",
        "progress_updated",
        "feedback_presented",
        "lesson_completed",
    }:
        assert required in event_types

    assert result["learner"]["mastery_score"] >= 10
    assert result["lesson"]["attempt_count"] == 1


def test_feedback_loop_uses_simplified_mode_when_stressed() -> None:
    runtime = EducationSystemPhaseOne()
    learner = LearnerProfile(
        learner_id="learner-stress",
        age_band="8-10",
        grade_band="3-5",
    )
    lesson = LessonState(
        lesson_id="lesson-stress",
        topic="Sovereign_Logic",
        objective="Describe memory reset behavior.",
        complexity=50,
    )

    runtime.learning_loop(learner, lesson)
    runtime.assessment_loop(
        learner,
        lesson,
        response_keywords=["memory"],
        expected_keywords=["cache", "memory"],
    )
    runtime.progression_loop(learner, lesson, was_correct=True)
    feedback = runtime.feedback_loop(learner, lesson, stress_level=85)

    assert "simplify" in feedback.lower()
