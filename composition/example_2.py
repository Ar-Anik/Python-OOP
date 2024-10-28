from typing import List

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def execute(self):
        return f"Executing task: {self.name}."

class Worker:
    def __init__(self, name):
        self.name = name

    def work_on(self, task):
        return f'{self.name} is {task.execute()}'

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task):
        self.tasks.append(task)
        self.tasks.sort(key=lambda x: x.priority, reverse=True)

    def get_next_task(self):
        return self.tasks.pop(0) if self.tasks else None

class Project:
    def __init__(self, name):
        self.name = name
        self.task_manager = TaskManager()
        self.workers: List[Worker] = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def add_task(self, task):
        self.task_manager.add_task(task)

    def task_distribute(self):
        result = []
        for worker in self.workers:
            task = self.task_manager.get_next_task()
            if task:
                result.append(worker.work_on(task))
            else:
                result.append(f"{worker.name} is waiting for task.")

        return result

project = Project("Chat GPT Make")

project.add_worker(Worker("Anik"))
project.add_worker(Worker("Sourov"))
project.add_worker(Worker("Anika"))

project.add_task(Task("Design Neural Network", 10))
project.add_task(Task("Collect Data", 4))
project.add_task(Task("Train Model", 1))

results = project.task_distribute()

for each in results:
    print(each)