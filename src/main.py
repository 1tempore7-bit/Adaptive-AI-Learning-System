from core.plm_store import PLMStore
from core.learning_memory import LearningMemory

from learner.learning_profile import LearningProfile

from analysis.adaptive_engine import AdaptiveEngine
from mentor.adaptive_mentor import AdaptiveMentor

from session_input import collect_learning_session


def main():

    print("MAIN STARTED")

    store = PLMStore()
    memory = LearningMemory()

    profile = LearningProfile("001")

    engine = AdaptiveEngine(
        memory,
        profile
    )

    mentor = AdaptiveMentor(
        store,
        memory
    )

    print("SYSTEMS LOADED")


    session = collect_learning_session()


    memory.add_event(
        "001",
        "learning_session",
        session
    )


    print("\nLEARNING SESSION SAVED:")
    print(session)


    analysis = engine.analyze_learner(
        "001",
        session["subject"]
    )


    print("\nANALYSIS:")
    print(analysis)


    print("\nLEARNING PROFILE:")
    print(profile.to_dict())


    advice = mentor.generate_advice(
        analysis,
        profile
    )


    print("\nADVICE:")
    print(advice)


    store.save_profile(profile)


if __name__ == "__main__":
    main()