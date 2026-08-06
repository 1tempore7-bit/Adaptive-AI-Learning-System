from datetime import datetime


class LearningTracker:

    def __init__(self, memory):

        self.memory = memory


    def record_session(
        self,
        learner_id,
        subject,
        topic,
        duration,
        focus,
        understanding,
        mistakes=None,
        summary_written=False
    ):

        if mistakes is None:
            mistakes = []


        event_data = {

            "subject": subject,

            "topic": topic,

            "duration": duration,

            "focus": focus,

            "understanding": understanding,

            "mistakes": mistakes,

            "summary_written": summary_written,

            "date": str(datetime.now())

        }


        self.memory.add_event(

            learner_id,

            "learning_session",

            event_data

        )


        return event_data



    def calculate_session_quality(
        self,
        focus,
        understanding
    ):

        quality = (
            (focus * 0.4)
            +
            (understanding * 0.6)
        )


        return round(
            quality * 10,
            2
        )