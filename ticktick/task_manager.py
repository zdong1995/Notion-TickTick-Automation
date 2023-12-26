from requests import Session
from constants import BASE_URL, API_ENDPOINTS
from utils import Utils
from typing import TypedDict, Optional
from enum import Enum, unique


@unique
class PriorityLevel(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    URGENT = 3


class TaskConfig(TypedDict):
    title: str
    id: Optional[str]
    projectId: Optional[str]
    columnId: Optional[str]  # project section id
    content: Optional[str]
    tags: Optional[list[str]]
    priority: Optional[PriorityLevel]
    startDate: Optional[str]  # "2023-12-21T05:00:00.000+0000"
    dueDate: Optional[str]  # "2023-12-21T05:00:00.000+0000"
    isAllDay: Optional[bool]


class TaskManager:
    def __init__(self, session: Session):
        self.session = session

    def add_new_task(self, task: TaskConfig) -> str:
        """Add new task based on configuration

        Args:
            task (TaskConfig): task configuration

        Returns:
            str: task id
        """
        if not task["title"]:
            raise ValueError("A task name title must be provided for creating a task.")
        url = f'{BASE_URL}{API_ENDPOINTS["AddTask"]}'
        result = self.session.post(url, json=task).json()
        return result["id"]

    def get_task_by_id(self, task_id) -> any:
        """Get task object by task id.

        Args:
            task_id (str): task id

        Returns:
            any: json object of task
        """
        url = f'{BASE_URL}{API_ENDPOINTS["GetTask"].replace("{task_id}", task_id)}'
        result = self.session.get(url).json()
        return result

    def get_task_focus_duration(self, task_id) -> int:
        """Get recorded task focus duration for task and all its sub-tasks

        Args:
            task_id (str): task id

        Returns:
            int: total focus duration of task and sub-tasks, unit seconds
        """
        task = self.get_task_by_id(task_id)
        if task is None or 'focusSummaries' not in task.keys():
            return 0
        cur_task_focus_history = [item for sublist in [i['focuses'] for i in task['focusSummaries']] for item in sublist]
        total_duration = sum(item[2] for item in cur_task_focus_history if len(item) > 2)
        if 'childIds' in task.keys():
            child_tasks = task['childIds']
            for child_task_id in child_tasks:
                total_duration += self.get_task_focus_duration(child_task_id)
        return total_duration

    def batch_add_tasks(self, tasks: list[TaskConfig]) -> list[str]:
        """Add list of new tasks based on configuration

        Args:
            tasks (list[TaskConfig]): list of task configuration

        Returns:
            list[str]: list of task id
        """
        url = f'{BASE_URL}{API_ENDPOINTS["BatchTask"]}'
        result = self.session.post(url, json={"add": tasks}).json()
        return result["id2etag"].keys()

    def update_task(self, task_id: str, task: TaskConfig) -> any:
        """Update task configuration for existing task.

        Raises:
            ValueError: A task_id must be provided for updating a task.
        """
        if not task_id:
            raise ValueError("A task_id must be provided for updating a task.")
        url = f'{BASE_URL}{API_ENDPOINTS["BatchTask"]}'
        original_task = self.get_task_by_id(task_id)
        for key, value in task.items():
            original_task[key] = value
        self.session.post(url, json={"update": [original_task]})
