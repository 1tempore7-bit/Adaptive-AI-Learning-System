class AdaptiveEngine:
    def __init__(self, memory, profile):
        self.memory = memory
        self.profile = profile

    def analyze_learner(self, learner_id, subject="General"):

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


        # تحديث ملف المتعلم حسب المادة
        self.profile.add_subject(subject)

        self.profile.update_progress(
            subject,
            progress_rate
        )

        self.profile.update_weak_topics(
            subject,
            list(set(weak_topics))
        )


        analysis = {
            "learner_id": learner_id,
            "subject": subject,
            "total_events": len(events),
            "errors": errors,
            "successes": successes,
            "progress_rate": progress_rate,
            "progress_status": progress_status,
            "weak_topics": list(set(weak_topics)),
            "status": "active" if events else "new"
        }

        return analysis