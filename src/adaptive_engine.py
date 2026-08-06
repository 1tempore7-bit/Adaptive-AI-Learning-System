class AdaptiveEngine:
    def __init__(self, memory):
        self.memory = memory

    def analyze_learner(self, learner_id):
        events = self.memory.get_events(learner_id)

        errors = 0
        successes = 0
        weak_topics = []

        for event in events:
            if event["event_type"] == "concept_error":
                errors += 1

                topic = event["data"].get("topic")

                if topic:
                    weak_topics.append(topic)

            elif event["event_type"] == "successful_explanation":
                successes += 1

        status = "new"

        if len(events) > 0:
            status = "active"

        if errors > successes:
            recommendation = "Focus on reviewing weak concepts."

        elif successes > errors:
            recommendation = "Good progress. Increase difficulty."

        else:
            recommendation = "Continue learning and practice."

        return {
            "learner_id": learner_id,
            "total_events": len(events),
            "errors": errors,
            "successes": successes,
            "weak_topics": list(set(weak_topics)),
            "status": status,
            "recommendation": recommendation
        }