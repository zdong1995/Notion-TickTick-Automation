from utils import Utils
from task_manager import TaskManager
from project_manager import ProjectManager


class TicktickManager:
    def __init__(self):
        self.session = Utils.build_authorized_session()
        self.task_manager = TaskManager(session=self.session)
        self.project_manager = ProjectManager(session=self.session)
