import json
import requests
from constants import *
from pathlib import Path


class Utils:
    @staticmethod
    def json_pretty_print(data):
        print(json.dumps(data, indent=4))

    @staticmethod
    def build_authorized_session():
        """Build authenticated session using refreshed token. If token not exist, will login and save token to local.

        Returns:
            Session: authenticated session for subsequent test
        """
        session = requests.session()
        # need use fake user-agent anx x-device to be able call API v2
        session.headers.update({
            'User-Agent': USER_AGENT,
            'x-device': X_DEVICE
        })
        file_path = Path(TOKEN_FILE)
        if not file_path.exists():
            Utils.auth_and_refresh_token(session)
        with open(file_path, 'r', encoding='utf-8') as file:
            token = file.read().replace('\n', '')  # truncate potential character when save token file
        session.cookies['t'] = token
        return session

    @staticmethod
    def auth_and_refresh_token(session: requests.Session):
        """Authenticate and generate new token to refresh local toekn file
        """
        result = session.post(
            f'{BASE_URL}{API_ENDPOINTS["Login"]}', json=PASSWORD)
        with open(TOKEN_FILE, 'w', encoding='utf-8') as file:
            file.write(result.json()['token'])
