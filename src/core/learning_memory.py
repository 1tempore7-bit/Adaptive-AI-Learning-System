from core.database_manager import DatabaseManager


class LearningMemory:

    def __init__(self, file_path="database/memory_events.json"):

        self.file_path = file_path

        self.db = DatabaseManager()

        self.events = self.db.load(
            self.file_path,
            []
        )


    def add_event(
        self,
        learner_id,
        event_type,
        data
    ):

        event = {

            "learner_id": learner_id,

            "event_type": event_type,

            "data": data

        }


        self.events.append(event)

        self.save()

        return event



    def get_events(self, learner_id):

        return [

            event

            for event in self.events

            if event["learner_id"] == learner_id

        ]



    def save(self):

        self.db.save(
            self.file_path,
            self.events
        )