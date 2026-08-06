class AdaptiveMentor:
    def __init__(self, plm_store, memory):
        self.plm_store = plm_store
        self.memory = memory

    def generate_advice(self, analysis):

        weak_topics = analysis.get(
            "weak_topics",
            []
        )

        progress_status = analysis.get(
            "progress_status",
            "needs_attention"
        )

        if weak_topics:
            topics = ", ".join(weak_topics)

            return (
                f"Review these weak topics: {topics}. "
                "Keep practicing them."
            )

        if progress_status == "improving":
            return (
                "Your progress is improving. "
                "Try more advanced challenges."
            )

        elif progress_status == "stable":
            return (
                "Your progress is stable. "
                "More practice will help you improve."
            )

        return (
            "Focus on building your foundation."
        )