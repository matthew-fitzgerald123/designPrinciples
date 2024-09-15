# tasks/__init__.py

from .simple_task import SimpleTask
from .timed_task import TimedTask

class TaskFactory:
    @staticmethod
    def create_task(task_type, name, *args):
        if task_type == 'simple':
            return SimpleTask(name)
        elif task_type == 'timed':
            return TimedTask(name, *args)
        else:
            raise ValueError(f"Unknown task type: {task_type}")