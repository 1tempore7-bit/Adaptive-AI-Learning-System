class AdaptiveMentor:
    def __init__(self, plm_store, memory):
        self.plm_store = plm_store
        self.memory = memory

    def generate_advice(self, analysis):
        if analysis["status"] == "new":
            return "Start learning by building basic concepts."

        if analysis["total_events"] < 5:
            return "Continue practicing and collecting more learning data."

        return "Good progress. Keep improving your weak areas."