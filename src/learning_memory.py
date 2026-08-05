import json
import os
from datetime import datetime


class LearningMemory:
    def __init__(self, file_path="database/memory_events.json"):
        self.file_path = file_path
        self.events = self.load_events()

    def load_events(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)

        return []

    def save_events(self):
        with open(self.file_path, "w") as file:
            json.dump(
                self.events,
                file,
                indent=4
            )

    def add_event(self, learner_id, event_type, data):
        event = {
            "learner_id": learner_id,
            "event_type": event_type,
            "data": data,
            "timestamp": datetime.now().isoformat()
        }

        self.events.append(event)
        self.save_events()

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