# tasks/timed_task.py

import time
from .task import Task

class TimedTask(Task):
    def __init__(self, name, duration):
        super().__init__(name)
        self.duration = duration

    def mark_complete(self):
        print(f"Timed task '{self.name}' will take {self.duration} seconds to complete.")
        time.sleep(self.duration)
        self.is_done = True
        print(f"Timed task '{self.name}' completed after {self.duration} seconds.")