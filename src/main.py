from plm_store import PLMStore
from learning_memory import LearningMemory
from learning_profile import LearningProfile
from adaptive_engine import AdaptiveEngine
from adaptive_mentor import AdaptiveMentor


def main():

    print("MAIN STARTED")

    store = PLMStore()
    memory = LearningMemory()

    profile = LearningProfile("001")


    # Learning goals
    profile.add_goal(
        "Master Mathematics",
        "deep_learning",
        "high"
    )

    profile.add_goal(
        "Learn Python",
        "skill",
        "medium"
    )

    profile.add_goal(
        "Learn Chinese",
        "language",
        "low"
    )


    engine = AdaptiveEngine(memory, profile)
    mentor = AdaptiveMentor(store, memory)

    print("SYSTEMS LOADED")


    memory.add_event(
        "001",
        "concept_error",
        {
            "subject": "Mathematics",
            "topic": "Derivatives",
            "problem": "Limits"
        }
    )


    memory.add_event(
        "001",
        "successful_explanation",
        {
            "subject": "Mathematics",
            "topic": "Derivatives",
            "method": "Visual explanation"
        }
    )


    print("EVENTS SAVED")


    analysis = engine.analyze_learner(
        "001",
        "Mathematics"
    )


    print("ANALYSIS:")
    print(analysis)


    print("LEARNING PROFILE:")
    print(profile.to_dict())


    store.save_profile(profile)

    print("PROFILE SAVED")


    print("ACTIVE GOALS:")
    print(profile.get_active_goals())


    advice = mentor.generate_advice(
        analysis,
        profile
    )


    print("ADVICE:")
    print(advice)



if __name__ == "__main__":
    main()