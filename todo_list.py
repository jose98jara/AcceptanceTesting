class Task:
    def __init__(self, name, status="Pending"):
        self.name = name
        self.status = status

    def __str__(self):
        return f"{self.name} ({self.status})"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        new_task = Task(task_name)
        self.tasks.append(new_task)

    def list_tasks(self):
        return [str(task) for task in self.tasks]

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.status = "Completed"

    def clear_tasks(self):
        self.tasks = []
