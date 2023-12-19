from requests import Session
from constants import BASE_URL, API_ENDPOINTS
from utils import Utils
from typing import TypedDict, Optional
from enum import Enum, unique


@unique
class ViewMode(Enum):
    LIST = 'list'
    KANBAN = 'kanban'
    TIMELINE = 'timeline'


class ProjectConfig(TypedDict):
    name: str
    viewMode: Optional[ViewMode]
    color: Optional[str]


class ProjectManager:
    def __init__(self, session: Session):
        self.session = session

    def add_new_project(self, project: ProjectConfig) -> str:
        """Add new project based on configuration

        Args:
            project (ProjectConfig): project configuration

        Returns:
            str: project id
        """
        url = f'{BASE_URL}{API_ENDPOINTS["AddProject"]}'
        print(url)
        result = self.session.post(url, json=project).json()
        Utils.json_pretty_print(result)
        return result["id"]

    def get_project_by_id(self, project_id: str):
        """Get project object by project id

        Args:
            project_id (str): project id
        """
        url = f'{BASE_URL}{API_ENDPOINTS["GetAllProjects"]}'
        print(url)
        result = self.session.get(url).json()
        for project in result:
            if project["id"] == project_id:
                Utils.json_pretty_print(project)

    def get_project_sections_by_project_id(self, project_id: str) -> list[any]:
        """Get all project sections definitions for given project id.

        Args:
            project_id (str): project id

        Returns:
            list[any]: json array of project sections definition
        """
        url = f'{BASE_URL}{API_ENDPOINTS["GetProjectSections"].replace("{project_id}", project_id)}'
        print(url)
        result = self.session.get(url).json()
        Utils.json_pretty_print(result)
        return result

    def add_new_project_section(self, project_id: str, section_names: list[str]):
        """Add new sections to given project.

        Args:
            project_id (str): project id
            section_names (list[str]): new sections to be added to project
        """
        url = f'{BASE_URL}{API_ENDPOINTS["ProjectSection"]}'
        print(url)
        sections = [{"projectId": project_id, "name": section_name}
                    for section_name in section_names]
        result = self.session.post(url, json={"add": sections})
        Utils.json_pretty_print(result.json())

    def get_project_to_id_mapping(self):
        url = f'{BASE_URL}{API_ENDPOINTS["GetAllProjects"]}'
        print(url)
        result = self.session.get(url)
        project_list = {}
        for project in result.json():
            project_list[project['name']] = project['id']
        for key, value in project_list.items():
            print(f"{key}: {value}")
        return project_list
