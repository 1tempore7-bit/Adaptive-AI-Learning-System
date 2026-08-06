from core.database_manager import DatabaseManager


class PLMStore:

    def __init__(self, file_path="database/plm_data.json"):

        self.file_path = file_path

        self.db = DatabaseManager()

        self.learners = self.db.load(
            self.file_path,
            {}
        )


    def create_learner(self, learner_id, profile):

        self.learners[learner_id] = profile.to_dict()

        self.save()

        return self.learners[learner_id]


    def get_learner(self, learner_id):

        return self.learners.get(learner_id)



    def update_learner(self, learner_id, data):

        if learner_id in self.learners:

            self.learners[learner_id].update(data)

            self.save()

            return True


        return False



    def save_profile(self, profile):

        self.learners[profile.learner_id] = profile.to_dict()

        self.save()

        return True



    def delete_learner(self, learner_id):

        if learner_id in self.learners:

            del self.learners[learner_id]

            self.save()

            return True


        return False



    def save(self):

        self.db.save(
            self.file_path,
            self.learners
        )