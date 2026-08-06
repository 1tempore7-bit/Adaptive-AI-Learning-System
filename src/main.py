from src.core.plm_store import PLMStore
from src.core.learning_memory import LearningMemory
from src.core.database_manager import DatabaseManager

from src.learner.learning_profile import LearningProfile
from src.learner.daily_state import DailyState

from src.analysis.adaptive_engine import AdaptiveEngine
from src.mentor.adaptive_mentor import AdaptiveMentor

from src.tracking.learning_tracker import LearningTracker
from src.session_input import SessionInput


def main():

    print("MAIN STARTED")

    db = DatabaseManager()

    plm_store = PLMStore()

    memory = LearningMemory()

    profile = LearningProfile("001")

    tracker = LearningTracker(memory)

    session_input = SessionInput()

    daily_state = DailyState()

    engine = AdaptiveEngine(
        memory,
        profile
    )

    mentor = AdaptiveMentor(
        plm_store,
        memory
    )

    print("SYSTEMS LOADED")

    # Daily condition

    state = daily_state.collect_state()

    print("\nDAILY STATE:")
    print(state)

    # Learning session

    session = session_input.collect_session()

    print("\nLEARNING SESSION SAVED:")
    print(session)

    # Save learning event

    memory.add_event(
        "001",
        "learning_session",
        session
    )

    # Analyze learner

    analysis = engine.analyze_learner(
        "001",
        session["subject"]
    )

    # Save updated learner profile
    plm_store.save_profile(profile)

    print("\nANALYSIS:")
    print(analysis)

    # Profile

    print("\nLEARNING PROFILE:")
    print(profile.to_dict())

    # Adaptive advice

    advice = mentor.generate_advice(
        analysis,
        profile,
        state
    )

    print("\nADVICE:")
    print(advice)


if __name__ == "__main__":
    main()