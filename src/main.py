from plm_store import PLMStore
from learning_memory import LearningMemory
from adaptive_engine import AdaptiveEngine
from adaptive_mentor import AdaptiveMentor


def main():

    # Initialize systems
    store = PLMStore()
    memory = LearningMemory()

    engine = AdaptiveEngine(memory)
    mentor = AdaptiveMentor(store, memory)

    # Create learner
    learner = {
        "name": "Learner",
        "level": "Beginner",
        "goals": [
            "AI",
            "Mathematics"
        ]
    }

    store.create_learner(
        "001",
        learner
    )

    # Add learning event
    memory.add_event(
        "001",
        "system_start",
        {
            "message": "Learning session started"
        }
    )

    # Analyze learner
    analysis = engine.analyze_learner(
        "001"
    )

    # Mentor response
    advice = mentor.generate_advice(
        analysis
    )

    print("\nLearning Memory:")
    print(
        memory.get_events("001")
    )

    print("\nAdaptive Analysis:")
    print(
        analysis
    )

    print("\nMentor Advice:")
    print(
        advice
    )


if __name__ == "__main__":
    main()