import json
import requests
from constants import *


class Utils:
    @staticmethod
    def json_pretty_print(data):
        print(json.dumps(data, indent=4))

    @staticmethod
    def auth_and_build_session():
        """
        Authenticate adn build new session for subsequence request.
        """
        session = requests.session()
        # need use fake user-agent anx x-device to be able call API v2
        session.headers.update({
            'User-Agent': USER_AGENT,
            'x-device': X_DEVICE
        })
        result = session.post(
            f'{BASE_URL}{API_ENDPOINTS["Login"]}', json=PASSWORD)
        token = result.json()['token']
        session.headers.update({'Authorization': f'Bearer {token}'})
        return session
