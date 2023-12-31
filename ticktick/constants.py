import secrets

TOKEN_FILE = '/tmp/token.txt'

AUTH_CONFIG_FILE = './config/auth_config.yml'

BASE_URL = 'https://api.ticktick.com/api/v2'

API_ENDPOINTS = {
    'Login': '/user/signon?wc=true&remember=true',
    # task API
    'AddTask': '/task',
    'GetTask': '/task/{task_id}',
    'BatchTask': '/batch/task',
    # project API
    'AddProject': '/project',
    'GetAllProjects': '/projects',
    'BatchProject': '/batch/project',
    'ProjectSection': '/column',
    'GetProjectSections': '/column/project/{project_id}',
}

# Header info to simulate web browser for API access
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0"
X_DEVICE = '{"platform":"web","os":"OS X","device":"Firefox 95.0","name":"unofficial api!","version":4531, "id":"6490' + secrets.token_hex(10) + '","channel":"website","campaign":"","websocket":""}'
