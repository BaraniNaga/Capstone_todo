from datetime import datetime

class TaskModel:
    def __init__(self, id: int, title: str, description: str, completed: bool, created_at: datetime, updated_at: datetime):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at
        self.updated_at = updated_at
