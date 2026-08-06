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

        total_attempts = errors + successes

        progress_rate = 0

        if total_attempts > 0:
            progress_rate = round(
                (successes / total_attempts) * 100,
                2
            )

        if progress_rate >= 70:
            progress_status = "improving"

        elif progress_rate >= 40:
            progress_status = "stable"

        else:
            progress_status = "needs_attention"

        return {
            "learner_id": learner_id,
            "total_events": len(events),
            "errors": errors,
            "successes": successes,
            "progress_rate": progress_rate,
            "progress_status": progress_status,
            "weak_topics": list(set(weak_topics)),
            "status": "active" if events else "new"
        }