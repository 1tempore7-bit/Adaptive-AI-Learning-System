class AdaptiveMentor:

    def __init__(self, plm_store, memory):

        self.plm_store = plm_store
        self.memory = memory


    def generate_advice(self, analysis, profile=None, daily_state=None):

        weak_topics = analysis.get(
            "weak_topics",
            []
        )

        progress_status = analysis.get(
            "progress_status",
            "needs_attention"
        )


        advice = []


        # Weak topics analysis

        if weak_topics:

            topics = ", ".join(weak_topics)

            advice.append(
                f"Your weak topics currently are: {topics}."
            )


            advice.append(
                "Focus on understanding the foundations before moving to harder problems."
            )



        # Daily condition analysis

        if daily_state:

            condition = daily_state.get(
                "condition",
                "normal"
            )

            energy = daily_state.get(
                "energy",
                10
            )

            focus = daily_state.get(
                "focus",
                10
            )

            stress = daily_state.get(
                "stress",
                0
            )

            learning_mode = daily_state.get(
                "learning_mode",
                "normal"
            )


            if condition in ["tired", "sick"]:

                advice.append(
                    "Your energy is low today. Reduce the difficulty and focus on understanding and review instead of heavy problem solving."
                )


            if energy <= 3:

                advice.append(
                    "Because your energy level is very low, use a short focused session and avoid forcing long study periods."
                )


            if focus <= 4:

                advice.append(
                    "Your focus is limited today. Study in small blocks and remove distractions."
                )


            if stress >= 7:

                advice.append(
                    "Your stress level is high. Start with an easier task to build confidence before harder tasks."
                )


            if learning_mode == "light":

                advice.append(
                    "A light session is recommended today: review concepts, correct mistakes, and write summaries."
                )


            elif learning_mode == "deep":

                advice.append(
                    "You are ready for deeper learning. Try challenging problems and explain your reasoning."
                )



        # Profile analysis

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



            behavior = profile.learning_behavior


            if behavior.get("summary_required"):

                advice.append(
                    "Before moving to a new topic, write a short summary to strengthen your understanding."
                )


            methods = behavior.get(
                "preferred_methods",
                []
            )


            if "writing" in methods:

                advice.append(
                    "Use writing as a learning tool: explain concepts in your own words."
                )


            if behavior.get("thinking_style") == "analytical":

                advice.append(
                    "Your analytical thinking is useful, but first identify exactly what the question asks before exploring extra possibilities."
                )


            if behavior.get("learning_language") == "Arabic":

                advice.append(
                    "Keep learning mainly in Arabic while gradually building English technical vocabulary."
                )



        # Progress analysis

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