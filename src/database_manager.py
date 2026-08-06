import json
import os


class DatabaseManager:
    def __init__(self):
        self.ensure_database_folder()

    def ensure_database_folder(self):
        if not os.path.exists("database"):
            os.makedirs("database")

    def load(self, file_path, default):
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                return json.load(file)

        return default

    def save(self, file_path, data):
        with open(file_path, "w") as file:
            json.dump(
                data,
                file,
                indent=4
            )