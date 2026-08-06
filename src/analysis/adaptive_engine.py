class AdaptiveEngine:

    def __init__(self, memory, profile):

        self.memory = memory
        self.profile = profile



    def analyze_learner(self, learner_id, subject="General"):

        events = self.memory.get_events(learner_id)


        errors = 0
        successes = 0
        weak_topics = []

        total_sessions = 0
        total_understanding = 0
        total_focus = 0



        for event in events:

            event_type = event.get(
                "event_type"
            )


            data = event.get(
                "data",
                {}
            )


            # Learning session analysis

            if event_type == "learning_session":

                total_sessions += 1


                understanding = data.get(
                    "understanding",
                    0
                )

                focus = data.get(
                    "focus",
                    0
                )


                total_understanding += understanding

                total_focus += focus



                mistakes = data.get(
                    "mistakes",
                    []
                )


                if mistakes:

                    errors += len(mistakes)


                    topic = data.get(
                        "topic"
                    )


                    if topic:

                        weak_topics.append(
                            topic
                        )


                else:

                    successes += 1



            # Previous concept events

            elif event_type == "concept_error":

                errors += 1


                topic = data.get(
                    "topic"
                )


                if topic:

                    weak_topics.append(
                        topic
                    )



            elif event_type == "successful_explanation":

                successes += 1




        total_attempts = errors + successes


        progress_rate = 0


        if total_attempts > 0:

            progress_rate = round(
                (successes / total_attempts) * 100,
                2
            )



        # Add understanding factor

        if total_sessions > 0:

            average_understanding = (
                total_understanding / total_sessions
            )


            average_focus = (
                total_focus / total_sessions
            )


            progress_rate = round(
                (
                    progress_rate * 0.5
                    +
                    average_understanding * 5
                    +
                    average_focus * 2
                ),
                2
            )



        if progress_rate >= 70:

            progress_status = "improving"


        elif progress_rate >= 40:

            progress_status = "stable"


        else:

            progress_status = "needs_attention"




        # Update learner profile

        self.profile.add_subject(
            subject
        )


        self.profile.update_progress(
            subject,
            progress_rate
        )


        self.profile.update_weak_topics(
            subject,
            list(set(weak_topics))
        )



        return {

            "learner_id": learner_id,

            "subject": subject,

            "total_events": len(events),

            "errors": errors,

            "successes": successes,

            "progress_rate": progress_rate,

            "progress_status": progress_status,

            "weak_topics": list(set(weak_topics)),

            "status": "active" if events else "new"

        }