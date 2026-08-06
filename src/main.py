from src.core.plm_store import PLMStore
from src.core.learning_memory import LearningMemory
from src.core.database_manager import DatabaseManager

from src.learner.learning_profile import LearningProfile
from src.learner.daily_state import DailyState

from src.analysis.adaptive_engine import AdaptiveEngine
from src.mentor.adaptive_mentor import AdaptiveMentor

from src.tracking.learning_tracker import LearningTracker
from src.session_input import SessionInput



def load_profile(plm_store, learner_id):

    saved_profile = plm_store.get_learner(
        learner_id
    )

    profile = LearningProfile(
        learner_id
    )


    if saved_profile:

        profile.level = saved_profile.get(
            "level",
            "Beginner"
        )


        profile.subjects = saved_profile.get(
            "subjects",
            {}
        )


        profile.active_subjects = saved_profile.get(
            "active_subjects",
            []
        )


        profile.future_subjects = saved_profile.get(
            "future_subjects",
            []
        )


        profile.goals = saved_profile.get(
            "goals",
            []
        )


        profile.learning_behavior = saved_profile.get(
            "learning_behavior",
            profile.learning_behavior
        )


    return profile



def main():

    print("MAIN STARTED")


    db = DatabaseManager()


    plm_store = PLMStore()


    memory = LearningMemory()


    learner_id = "001"


    profile = load_profile(
        plm_store,
        learner_id
    )


    tracker = LearningTracker(
        memory
    )


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



    # Save event

    memory.add_event(
        learner_id,
        "learning_session",
        session
    )



    # Analyze

    analysis = engine.analyze_learner(
        learner_id,
        session["subject"]
    )


    print("\nANALYSIS:")
    print(analysis)



    # Save profile without deleting old subjects

    plm_store.save_profile(
        profile
    )



    print("\nLEARNING PROFILE:")
    print(profile.to_dict())



    # Advice

    advice = mentor.generate_advice(
        analysis,
        profile,
        state
    )


    print("\nADVICE:")
    print(advice)




if __name__ == "__main__":

    main()