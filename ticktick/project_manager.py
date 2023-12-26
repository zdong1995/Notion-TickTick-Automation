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
        result = self.session.post(url, json=project).json()
        return result["id"]

    def get_project_by_id(self, project_id: str):
        """Get project object by project id

        Args:
            project_id (str): project id
        """
        url = f'{BASE_URL}{API_ENDPOINTS["GetAllProjects"]}'
        result = self.session.get(url).json()
        for project in result:
            if project["id"] == project_id:
                return project

    def update_project(self, project_id: str, project: ProjectConfig) -> str:
        """Update project configuration for existing project.

        Raises:
            ValueError: A project_id must be provided for updating a project.
        """
        if not project_id:
            raise ValueError("A project_id must be provided for updating a project.")
        url = f'{BASE_URL}{API_ENDPOINTS["BatchProject"]}'
        original_project = self.get_project_by_id(project_id)
        for key, value in project.items():
            original_project[key] = value
        self.session.post(url, json={"update": [original_project]})

    def get_all_project_sections(self, project_id: str) -> list[any]:
        """Get all project sections definitions for given project id.

        Args:
            project_id (str): project id

        Returns:
            list[any]: json array of project sections definition
        """
        url = f'{BASE_URL}{API_ENDPOINTS["GetProjectSections"].replace("{project_id}", project_id)}'
        result = self.session.get(url).json()
        return result

    def get_project_section(self, section_id: str, project_id: str) -> any:
        """Get specific project section definitions by project id and section id.

        Args:
            section_id (str): section id
            project_id (str): project id

        Returns:
            any: json object of project section definition
        """
        all_sections = self.get_all_project_sections(project_id)
        for section in all_sections:
            if section['id'] == section_id:
                return section
        raise ValueError("Section id doesn't exist for given project id.")

    def add_new_project_section(self, project_id: str, section_names: list[str]):
        """Add new sections to given project.

        Args:
            project_id (str): project id
            section_names (list[str]): new sections to be added to project
        """
        url = f'{BASE_URL}{API_ENDPOINTS["ProjectSection"]}'
        sections = [{"projectId": project_id, "name": section_name}
                    for section_name in section_names]
        result = self.session.post(url, json={"add": sections})
        project_section_id = list(result.json()['id2etag'].keys())[0]
        return project_section_id

    def update_project_section_name(self, section_id: str, project_id: str, section_name: str):
        """Update section name of existing project section.

        Args:
            section_id (str): section id
            project_id (str): project id
            section_names (str): new sections name to be updated
        """
        if not section_id or not project_id or not section_name:
            raise ValueError('Need define section_id, project_id, section_name.')
        url = f'{BASE_URL}{API_ENDPOINTS["ProjectSection"]}'
        section = self.get_project_section(section_id, project_id)
        section['name'] = section_name
        self.session.post(url, json={"update": [section]})
