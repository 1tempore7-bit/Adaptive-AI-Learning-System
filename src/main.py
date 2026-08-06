from plm_store import PLMStore
from learning_memory import LearningMemory
from adaptive_engine import AdaptiveEngine
from adaptive_mentor import AdaptiveMentor


def main():

    print("MAIN STARTED")

    store = PLMStore()
    memory = LearningMemory()

    engine = AdaptiveEngine(memory)
    mentor = AdaptiveMentor(store, memory)

    print("SYSTEMS LOADED")

    memory.add_event(
        "001",
        "concept_error",
        {
            "topic": "Derivatives",
            "problem": "Limits"
        }
    )

    memory.add_event(
        "001",
        "successful_explanation",
        {
            "topic": "Derivatives",
            "method": "Visual explanation"
        }
    )

    print("EVENTS SAVED")

    analysis = engine.analyze_learner("001")

    print("ANALYSIS:")
    print(analysis)

    advice = mentor.generate_advice(analysis)

    print("ADVICE:")
    print(advice)


if __name__ == "__main__":
    main()