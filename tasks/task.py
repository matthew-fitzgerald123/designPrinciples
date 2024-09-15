# tasks/task.py

from abc import ABC, abstractmethod

class Task(ABC):
    def __init__(self, name):
        self.name = name
        self.is_done = False

    @abstractmethod
    def mark_complete(self):
        pass