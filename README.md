# Notion-Ticktick-Automation

Automation script to 2-way sync [Notion](https://www.notion.so) project and [TickTick](http://ticktick.com) project.

## Content

### [TickTick API](./ticktick/)

Unofficial TickTick V2 API implemented by Python with basic usage.

### Prerequisite

- Change your username and password in [constants.py](./ticktick/constants.py) before test.
- Simply run [api_test.ipynb](./ticktick/api_test.ipynb) to get familar with TickTick API and response object type.

### Usage

- `add_new_task`: `python3 main.py add_new_task --task_name {TASK_NAME} --project_id {PROJECT_ID} --section_id {SECTION_ID} --content {CONTENT}`
  - if no project section declared, task will be added into first section: `python3 main.py add_new_task --task_name {TASK_NAME} --project_id {PROJECT_ID}`
  - if no project section and project declared, task will be added into inbox: `python3 main.py add_new_task --task_name {TASK_NAME}`
- `update_task`: `python3 main.py update_task --task_id {TASK_ID} --task_name {TASK_NAME} --project_id {PROJECT_ID} --section_id {SECTION_ID} --content {CONTENT}`
  - only need to include the task field needed to be updated in the command
- `get_task_focus_duration`: get total focus time of given task and all its subtasks
  - `python3 main.py get_task_focus_duration --task_id {TASK_ID}`
- `add_new_project`: `python3 main.py add_new_project --project_name {PROJECT_NAME}`
- `update_project`: `python3 main.py update_project --project_id {PROJECT_ID} --project_name {PROJECT_NAME}`
- `add_new_project_section`: `python3 main.py add_new_project_section --section_name {SECTION_NAME} --project_id {PROJECT_ID}`
- `update_project_section_name`: `python3 main.py update_project_section_name --project_id {PROJECT_ID} --section_id {SECTION_ID} --section_name {SECTION_NAME}`
