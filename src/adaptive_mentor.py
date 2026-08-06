class AdaptiveMentor:
    def __init__(self, plm_store, memory):
        self.plm_store = plm_store
        self.memory = memory

    def generate_advice(self, analysis):

        weak_topics = analysis.get(
            "weak_topics",
            []
        )

        if weak_topics:
            topics = ", ".join(weak_topics)

            return (
                "You should review these weak topics: "
                + topics
            )

        if analysis["status"] == "active":
            return (
                "Good progress. Try more advanced challenges."
            )

        return (
            "Start learning and build your foundation."
        )