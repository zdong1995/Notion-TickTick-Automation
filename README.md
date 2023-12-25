# Notion-Ticktick-Automation

Automation script to 2-way sync [Notion](https://www.notion.so) project and [TickTick](http://ticktick.com) project.

## Content

### [TickTick API](./ticktick/)

Unofficial TickTick V2 API implemented by Python with basic usage.

### Prerequisite

- Change your username and password in [constants.py](./ticktick/constants.py) before test.
- Simply run [api_test.ipynb](./ticktick/api_test.ipynb) to get familar with TickTick API and response object type.

### Usage

- `add_new_task`
  - Add task to defined project and project section: `python3 main.py add_new_task --new_task_name {TASK_NAME} --project_id {PROJECT_ID} --section_id {SECTION_ID}`
  - If no project section declared, task will be added into first section: `python3 main.py add_new_task --new_task_name {TASK_NAME} --project_id {PROJECT_ID}`
  - If no project section and project declared, task will be added into inbox: `python3 main.py add_new_task --new_task_name {TASK_NAME}`
- `add_new_project`
  - `python3 main.py add_new_project --new_project_name test_project`
- `add_new_project_section`
  - `python3 main.py add_new_project_section --new_section_name {SECTION_NAME} --project_id {PROJECT_ID}`
- `get_task_focus_duration`: get total focus time of given task and all its subtasks
  - `python3 main.py get_task_focus_duration --task_id {TASK_ID}`
