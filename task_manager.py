# task_manager.py

class TaskManager:
    _instance = None  # Private class attribute to hold the single instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TaskManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.tasks = []
        return cls._instance

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.name}' added.")

    def list_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            status = 'Done' if task.is_done else 'Pending'
            print(f"{i}. {task.name} - {status}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print(f"Task '{self.tasks[index].name}' marked as complete.")
        else:
            print("Invalid task number.")