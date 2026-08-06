from plm_store import PLMStore
from learning_memory import LearningMemory
from learning_profile import LearningProfile
from adaptive_engine import AdaptiveEngine
from adaptive_mentor import AdaptiveMentor
from learning_tracker import LearningTracker
from session_input import SessionInput



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


    tracker = LearningTracker(
        memory
    )


    session_input = SessionInput()


    print("SYSTEMS LOADED")



    # إدخال جلسة تعلم من المستخدم

    session = session_input.collect_session()



    tracker.record_session(

        "001",

        session["subject"],

        session["topic"],

        session["duration"],

        session["focus"],

        session["understanding"],

        session["mistakes"],

        session["summary_written"]

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



if __name__ == "__main__":

    main()