class AdaptiveMentor:
    def __init__(self, plm_store, learning_memory):
        self.plm_store = plm_store
        self.learning_memory = learning_memory

    def analyze_learner(self, learner_id):
        profile = self.plm_store.get_learner(learner_id)

        if profile:
            return {
                "learner_id": learner_id,
                "profile": profile,
                "status": "Analyzed"
            }

        return {
            "learner_id": learner_id,
            "status": "No profile found"
        }
