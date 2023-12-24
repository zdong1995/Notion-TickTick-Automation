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
        url = f'{BASE_URL}{API_ENDPOINTS["AddTask"]}'
        print(url)
        result = self.session.post(url, json=task).json()
        Utils.json_pretty_print(result)
        return result["id"]

    def get_task_by_id(self, task_id) -> any:
        """Get task object by task id.

        Args:
            task_id (str): task id

        Returns:
            any: json object of task
        """
        url = f'{BASE_URL}{API_ENDPOINTS["GetTask"].replace("{task_id}", task_id)}'
        print(url)
        result = self.session.get(url).json()
        Utils.json_pretty_print(result)
        return result

    def get_task_focus_duration(self, task_id) -> int:
        """Get recorded task focus duration for task and all its sub-tasks

        Args:
            task_id (str): task id

        Returns:
            int: total focus duration of task and sub-tasks
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
        url = f'{BASE_URL}{API_ENDPOINTS["BatchAddTask"]}'
        print(url)
        result = self.session.post(url, json={"add": tasks}).json()
        Utils.json_pretty_print(result)
        return result["id2etag"].keys()
