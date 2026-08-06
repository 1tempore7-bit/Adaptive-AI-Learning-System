class LearningProfile:
    def __init__(self, learner_id):
        self.learner_id = learner_id
        self.level = "Beginner"

        self.strong_topics = []
        self.weak_topics = []
        self.mastered_topics = []

        self.progress = 0

    def update_progress(self, progress):
        self.progress = progress

    def update_weak_topics(self, topics):
        self.weak_topics = topics

    def update_strong_topics(self, topics):
        self.strong_topics = topics

    def add_mastered_topic(self, topic):
        if topic not in self.mastered_topics:
            self.mastered_topics.append(topic)

    def to_dict(self):
        return {
            "learner_id": self.learner_id,
            "level": self.level,
            "strong_topics": self.strong_topics,
            "weak_topics": self.weak_topics,
            "mastered_topics": self.mastered_topics,
            "progress": self.progress,
        }