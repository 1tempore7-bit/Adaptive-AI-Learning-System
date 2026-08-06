from plm_store import PLMStore
from learning_memory import LearningMemory
from learning_profile import LearningProfile
from adaptive_engine import AdaptiveEngine
from adaptive_mentor import AdaptiveMentor
from learning_tracker import LearningTracker



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


    print("SYSTEMS LOADED")



    # تسجيل جلسة تعلم تجريبية

    session = tracker.record_session(

        "001",

        "Mathematics",

        "Derivatives",

        duration=90,

        focus=8,

        understanding=7,

        mistakes=[
            "Limits confusion"
        ],

        summary_written=True

    )


    print("LEARNING SESSION SAVED:")

    print(session)



    # تحليل المتعلم

    analysis = engine.analyze_learner(

        "001",

        "Mathematics"

    )


    print("ANALYSIS:")

    print(analysis)



    print("LEARNING PROFILE:")

    print(profile.to_dict())



    advice = mentor.generate_advice(

        analysis,

        profile

    )


    print("ADVICE:")

    print(advice)



if __name__ == "__main__":

    main()