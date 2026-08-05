from plm_store import PLMStore
from learning_memory import LearningMemory
from adaptive_mentor import AdaptiveMentor


# Initialize core systems
plm = PLMStore()
memory = LearningMemory()

mentor = AdaptiveMentor(
    plm,
    memory
)


# Create learner profile
student_profile = {
    "name": "Learner",
    "level": "Beginner",
    "goals": [
        "Artificial Intelligence",
        "Mathematics"
    ]
}


# Store learner profile
plm.create_learner(
    "001",
    student_profile
)


# Record learning event
memory.add_event(
    "001",
    "system_start",
    {
        "message": "Learning session started"
    }
)


# Analyze learner
analysis = mentor.analyze_learner("001")


print("Mentor Analysis:")
print(analysis)

print("\nLearning Memory:")
print(memory.get_all_events())
