from datetime import datetime


class LearningMemory:
    def __init__(self):
        self.events = []

    def add_event(self, learner_id, event_type, data):
        event = {
            "learner_id": learner_id,
            "event_type": event_type,
            "data": data,
            "timestamp": datetime.now().isoformat()
        }

        self.events.append(event)
        return event

    def get_events(self, learner_id):
        return [
            event for event in self.events
            if event["learner_id"] == learner_id
        ]

    def get_all_events(self):
        return self.events

    def count_events(self):
        return len(self.events)
