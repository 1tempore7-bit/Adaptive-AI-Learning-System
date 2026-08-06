class AdaptiveEngine:
    def __init__(self, memory):
        self.memory = memory

    def analyze_learner(self, learner_id):
        events = self.memory.get_events(learner_id)

        errors = 0
        successes = 0

        for event in events:
            if event["event_type"] == "concept_error":
                errors += 1

            elif event["event_type"] == "successful_explanation":
                successes += 1

        status = "new"

        if len(events) > 0:
            status = "active"

        recommendation = "Continue learning."

        if errors > successes:
            recommendation = "Review weak concepts."

        elif successes > errors:
            recommendation = "Good progress. Increase difficulty."

        return {
            "learner_id": learner_id,
            "total_events": len(events),
            "errors": errors,
            "successes": successes,
            "status": status,
            "recommendation": recommendation
        }