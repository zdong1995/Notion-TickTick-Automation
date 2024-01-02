# Notion-Ticktick-Automation

Automation script to 2-way sync [Notion](https://www.notion.so) project and [TickTick](http://ticktick.com) project.

## Content

### [TickTick API](./ticktick/)

Unofficial TickTick V2 API implemented by Python with basic usage.

### Prerequisite

- Create `config` folder under `ticktick` folder and create `auth_config.yml` file inside `config` folder.

```
# ticktick/config/auth_config.yml
ticktick:
  username: YOUR_TICKTICK_USERNAME
  password: YOUR_TICKTICK_PASSWORD
```

- Simply run [api_test.ipynb](./ticktick/api_test.ipynb) to get familar with TickTick API and response object type.

### Usage

- `refresh_token`: `python3 main.py refresh_token`
- `add_new_task`: `python3 main.py add_new_task --task_name {TASK_NAME} --project_id {PROJECT_ID} --section_id {SECTION_ID} --content {CONTENT} --start_date {START_DATE} --due_date {DUE_DATE}`
  - if no project section declared, task will be added into first section: `python3 main.py add_new_task --task_name {TASK_NAME} --project_id {PROJECT_ID}`
  - if no project section and project declared, task will be added into inbox: `python3 main.py add_new_task --task_name {TASK_NAME}`
  - start_date and due_date should be in UTC format, example: `2024-01-01T05:00:00.000+0000`
- `update_task`: `python3 main.py update_task --task_id {TASK_ID} --task_name {TASK_NAME} --project_id {PROJECT_ID} --section_id {SECTION_ID} --content {CONTENT}  --start_date {START_DATE} --due_date {DUE_DATE}`
  - only need to include the task field needed to be updated in the command
- `get_task_focus_duration`: get total focus time of given task and all its subtasks
  - `python3 main.py get_task_focus_duration --task_id {TASK_ID}`
- `add_new_project`: `python3 main.py add_new_project --project_name {PROJECT_NAME}`
- `update_project`: `python3 main.py update_project --project_id {PROJECT_ID} --project_name {PROJECT_NAME}`
- `add_new_project_section`: `python3 main.py add_new_project_section --section_name {SECTION_NAME} --project_id {PROJECT_ID}`
- `update_project_section_name`: `python3 main.py update_project_section_name --project_id {PROJECT_ID} --section_id {SECTION_ID} --section_name {SECTION_NAME}`
