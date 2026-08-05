import json
import os


class PLMStore:
    def __init__(self, file_path="database/plm_data.json"):
        self.file_path = file_path
        self.learners = self.load_data()

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)

        return {}

    def save_data(self):
        with open(self.file_path, "w") as file:
            json.dump(
                self.learners,
                file,
                indent=4
            )

    def create_learner(self, learner_id, profile):
        self.learners[learner_id] = profile
        self.save_data()
        return self.learners[learner_id]

    def get_learner(self, learner_id):
        return self.learners.get(learner_id)

    def update_learner(self, learner_id, data):
        if learner_id in self.learners:
            self.learners[learner_id].update(data)
            self.save_data()
            return True

        return False

    def delete_learner(self, learner_id):
        if learner_id in self.learners:
            del self.learners[learner_id]
            self.save_data()
            return True

        return False
