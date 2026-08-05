class PLMStore:
    def __init__(self):
        self.learners = {}

    def create_learner(self, learner_id, profile):
        self.learners[learner_id] = profile
        return self.learners[learner_id]

    def get_learner(self, learner_id):
        return self.learners.get(learner_id)
