class LearningProfile:

    def __init__(self, learner_id):

        self.learner_id = learner_id

        self.level = "Beginner"


        self.subjects = {}

        self.active_subjects = []

        self.future_subjects = []


        self.goals = []


        # Learning behavior system
        self.learning_behavior = {

            "consistency": 0,

            "focus": 0,

            "deep_analysis": 0,

            "preferred_methods": [
                "writing",
                "deep_explanation"
            ],

            "summary_required": True,

            "review_style": "active_recall",

            "thinking_style": "analytical",

            "learning_language": "Arabic",

            "english_transition_level": 0
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



    # -------- Goals System --------

    def add_goal(
        self,
        name,
        goal_type="general",
        priority="medium"
    ):

        goal = {

            "name": name,

            "type": goal_type,

            "priority": priority,

            "progress": 0,

            "status": "active"

        }

        self.goals.append(goal)



    def update_goal_progress(self, name, progress):

        for goal in self.goals:

            if goal["name"] == name:

                goal["progress"] = progress



    def complete_goal(self, name):

        for goal in self.goals:

            if goal["name"] == name:

                goal["status"] = "completed"

                goal["progress"] = 100



    def get_active_goals(self):

        return [

            goal for goal in self.goals

            if goal["status"] == "active"

        ]



    # -------- Learning Behavior --------

    def update_behavior(self, key, value):

        if key in self.learning_behavior:

            self.learning_behavior[key] = value



    def add_learning_method(self, method):

        if method not in self.learning_behavior["preferred_methods"]:

            self.learning_behavior["preferred_methods"].append(method)



    def update_learning_language(self, language):

        self.learning_behavior["learning_language"] = language



    def update_english_level(self, level):

        self.learning_behavior["english_transition_level"] = level



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