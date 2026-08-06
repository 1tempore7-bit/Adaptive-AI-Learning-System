from datetime import datetime


class AdaptiveEngine:

    def __init__(self, memory, profile, daily_state=None):

        self.memory = memory
        self.profile = profile
        self.daily_state = daily_state


    def analyze_learner(self, learner_id, subject="General"):

        events = self.memory.get_events(learner_id)

        errors = 0
        successes = 0
        weak_topics = []

        total_sessions = 0
        weighted_progress = 0
        total_weight = 0

        now = datetime.now()


        for event in events:

            data = event.get(
                "data",
                {}
            )

            event_type = event.get(
                "event_type"
            )


            weight = 1

            timestamp = event.get(
                "timestamp"
            )


            if timestamp:

                try:

                    event_date = datetime.fromisoformat(
                        timestamp
                    )

                    days_old = (
                        now - event_date
                    ).days


                    # الأحداث الحديثة لها وزن أكبر
                    weight = max(
                        0.2,
                        1 - (days_old * 0.05)
                    )


                except:

                    weight = 1



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


                    # جلسة بها أخطاء
                    score = (
                        understanding * 5
                        +
                        focus * 2
                    )


                else:

                    successes += 1


                    # جلسة ناجحة
                    score = 100



                weighted_progress += (
                    score * weight
                )

                total_weight += weight



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




        progress_rate = 0


        if total_weight > 0:

            progress_rate = round(
                weighted_progress / total_weight,
                2
            )



        # تأثير الحالة اليومية

        if self.daily_state:

            energy = self.daily_state.get(
                "energy",
                10
            )

            focus = self.daily_state.get(
                "focus",
                10
            )

            stress = self.daily_state.get(
                "stress",
                0
            )


            # طاقة منخفضة

            if energy <= 3:

                progress_rate -= 5



            # تركيز منخفض

            if focus <= 4:

                progress_rate -= 3



            # ضغط مرتفع

            if stress >= 8:

                progress_rate -= 5



            # حالة ممتازة

            if (
                energy >= 8
                and focus >= 8
                and stress <= 3
            ):

                progress_rate += 5



            progress_rate = max(
                0,
                min(
                    100,
                    round(progress_rate, 2)
                )
            )



        if progress_rate >= 70:

            progress_status = "improving"


        elif progress_rate >= 40:

            progress_status = "stable"


        else:

            progress_status = "needs_attention"




        # تحديث ملف المتعلم

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