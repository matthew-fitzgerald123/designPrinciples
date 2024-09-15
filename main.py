# main.py

from task_manager import TaskManager
from tasks import TaskFactory

def main():
    # Create a singleton instance of TaskManager
    manager = TaskManager()

    # Create tasks using the factory
    task1 = TaskFactory.create_task('simple', 'Buy groceries')
    task2 = TaskFactory.create_task('timed', 'Complete workout', 3)

    # Add tasks to the manager
    manager.add_task(task1)
    manager.add_task(task2)

    # List all tasks
    print("\nTasks List:")
    manager.list_tasks()

    # Complete a task
    manager.complete_task(1)  # Completing the 'Complete workout' task

    # List all tasks again to see the updated status
    print("\nUpdated Tasks List:")
    manager.list_tasks()

if __name__ == '__main__':
    main()