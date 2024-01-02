from pathlib import Path
import requests
from constants import *
from utils import Utils
from task_manager import TaskManager
from project_manager import ProjectManager


class TicktickManager:
    def __init__(self):
        self.session = self.build_authorized_session()
        self.task_manager = TaskManager(session=self.session)
        self.project_manager = ProjectManager(session=self.session)

    def build_new_session(self):
        """Build new session with necessary header for API v2

        Returns:
            Session: new session
        """
        session = requests.session()
        # need use fake user-agent anx x-device to be able call API v2
        session.headers.update({
            'User-Agent': USER_AGENT,
            'x-device': X_DEVICE
        })
        return session

    def build_authorized_session(self):
        """Build authenticated session using refreshed token. If token not exist, will login and save token to local.

        Returns:
            Session: authenticated session for subsequent test
        """
        session = self.build_new_session()
        file_path = Path(TOKEN_FILE)
        if not file_path.exists():
            self.auth_and_refresh_token()
        with open(file_path, 'r', encoding='utf-8') as file:
            token = file.read().replace('\n', '')  # truncate potential character when save token file
        session.cookies['t'] = token
        return session

    def auth_and_refresh_token(self):
        """Authenticate and generate new token to refresh local toekn file
        """
        session = self.build_new_session()
        result = session.post(
            f'{BASE_URL}{API_ENDPOINTS["Login"]}', json=Utils.read_auth_config())
        with open(TOKEN_FILE, 'w', encoding='utf-8') as file:
            file.write(result.json()['token'])
        print(result.json()['token'])
