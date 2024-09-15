# tasks/simple_task.py

from .task import Task

class SimpleTask(Task):
    def mark_complete(self):
        self.is_done = True
        print(f"Simple task '{self.name}' completed.")