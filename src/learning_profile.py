class LearningProfile:
    def __init__(self, learner_id):
        self.learner_id = learner_id

        self.level = "Beginner"

        self.subjects = {}

        self.active_subjects = []

        self.future_subjects = []

        self.goals = []

        self.learning_behavior = {
            "consistency": 0,
            "focus": 0,
            "deep_analysis": 0
        }


    def add_subject(self, subject):

        if subject not in self.subjects:
            self.subjects[subject] = {
                "progress": 0,
                "weak_topics": [],
                "strong_topics": [],
                "mastered_topics": []
            }


    def set_active_subject(self, subject):

        self.add_subject(subject)

        if subject not in self.active_subjects:
            self.active_subjects.append(subject)


    def add_future_subject(self, subject):

        if subject not in self.future_subjects:
            self.future_subjects.append(subject)


    def update_progress(self, subject, progress):

        self.add_subject(subject)

        self.subjects[subject]["progress"] = progress


    def update_weak_topics(self, subject, topics):

        self.add_subject(subject)

        self.subjects[subject]["weak_topics"] = topics


    def update_strong_topics(self, subject, topics):

        self.add_subject(subject)

        self.subjects[subject]["strong_topics"] = topics


    def add_goal(self, goal):

        self.goals.append(goal)


    def update_behavior(self, key, value):

        if key in self.learning_behavior:
            self.learning_behavior[key] = value


    def to_dict(self):

        return {
            "learner_id": self.learner_id,
            "level": self.level,
            "subjects": self.subjects,
            "active_subjects": self.active_subjects,
            "future_subjects": self.future_subjects,
            "goals": self.goals,
            "learning_behavior": self.learning_behavior
        }