class AdaptiveEngine:
    def __init__(self, memory):
        self.memory = memory

    def analyze_learner(self, learner_id):
        events = self.memory.get_events(learner_id)

        result = {
            "learner_id": learner_id,
            "total_events": len(events),
            "status": "new"
        }

        if len(events) > 0:
            result["status"] = "active"

        return result