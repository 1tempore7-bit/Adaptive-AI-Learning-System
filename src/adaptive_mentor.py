class AdaptiveMentor:

    def __init__(self, plm_store, memory):
        self.plm_store = plm_store
        self.memory = memory


    def generate_advice(self, analysis, profile=None):

        weak_topics = analysis.get(
            "weak_topics",
            []
        )

        progress_status = analysis.get(
            "progress_status",
            "needs_attention"
        )


        advice = []


        # تحليل نقاط الضعف
        if weak_topics:

            topics = ", ".join(weak_topics)

            advice.append(
                f"Your weak topics currently are: {topics}."
            )


            advice.append(
                "Focus on understanding the foundations before moving to harder problems."
            )


        # تحليل الأهداف
        if profile:

            active_goals = profile.get_active_goals()

            if active_goals:

                high_priority_goals = [
                    goal for goal in active_goals
                    if goal["priority"] == "high"
                ]


                if high_priority_goals:

                    goal = high_priority_goals[0]

                    advice.append(
                        f"Your highest priority goal is: {goal['name']}."
                    )


                else:

                    goal = active_goals[0]

                    advice.append(
                        f"Current learning goal: {goal['name']}."
                    )


        # تحليل التقدم

        if progress_status == "improving":

            advice.append(
                "Your progress is improving. Increase the difficulty gradually."
            )


        elif progress_status == "stable":

            advice.append(
                "Your progress is stable. Continue practicing and look for deeper understanding."
            )


        else:

            advice.append(
                "Spend time reviewing the basics and identifying the reason behind mistakes."
            )


        return " ".join(advice)