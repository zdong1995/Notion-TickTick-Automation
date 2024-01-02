import json
import yaml
from constants import *


class Utils:
    @staticmethod
    def json_pretty_print(data):
        print(json.dumps(data, indent=4))

    @staticmethod
    def read_auth_config():
        with open(AUTH_CONFIG_FILE, 'r') as file:
            config = yaml.safe_load(file)
        return {
            'username': config['ticktick']['username'],
            'password': config['ticktick']['password']
        }
