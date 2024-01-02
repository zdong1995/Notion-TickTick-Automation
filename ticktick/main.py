import argparse

import requests
from task_manager import TaskConfig
from ticktick_manager import TicktickManager
from utils import Utils


def build_task_config(args: argparse.Namespace, is_new_task: bool = False) -> TaskConfig:
    """Build task config from arg parser

    Args:
        args (argparse.Namespace): args from argparser
        is_new_task (bool, optional): flag to differentiate new task and existing task. Defaults to False.

    Returns:
        TaskConfig: task configuration used to add task or update task
    """
    config_props = {
        'title': 'task_name',
        'projectId': 'project_id',
        'columnId': 'section_id',
        'id': 'task_id',
        'content': 'content',
        'startDate': 'start_date',
        'dueDate': 'due_date'
    }
    task_config: TaskConfig = {key: getattr(args, value) for key, value in config_props.items() if getattr(args, value)}
    if is_new_task:
        task_config.update({'tags': ['notion']})
    return task_config


def main():
    parser = argparse.ArgumentParser()
    tt = TicktickManager()
    parser.add_argument('mode', help='command mode')
    parser.add_argument('--task_name', help='name of TickTick task')
    parser.add_argument('--project_name', help='name of TickTick project to be created')
    parser.add_argument('--section_name', help='name of TickTick project section to be created')
    parser.add_argument('--project_id', help='TickTick project id')
    parser.add_argument('--section_id', help='TickTick section id')
    parser.add_argument('--task_id', help='TickTick task id')
    parser.add_argument('--content', help='content of the task')
    parser.add_argument('--start_date', help='start date of the task, in format yyyy-MM-dd')
    parser.add_argument('--due_date', help='due date of the task, in format yyyy-MM-dd')
    args = parser.parse_args()

    mode_actions = {
        'refresh_token': lambda: tt.auth_and_refresh_token(),
        'add_new_task': lambda: print(tt.task_manager.add_new_task(task=build_task_config(args, True))),
        'update_task': lambda: tt.task_manager.update_task(args.task_id, build_task_config(args)),
        'get_task_focus_duration': lambda: print(tt.task_manager.get_task_focus_duration(args.task_id) / 3600),
        'add_new_project': lambda: print(tt.project_manager.add_new_project(project={'name': args.project_name})),
        'update_project': lambda: tt.project_manager.update_project(args.project_id, project={'name': args.project_name}),
        'add_new_project_section': lambda: print(tt.project_manager.add_new_project_section(args.project_id, section_names=[args.section_name])),
        'update_project_section_name': lambda: tt.project_manager.update_project_section_name(args.section_id, args.project_id, args.section_name)
    }

    mode_actions.get(args.mode)()


if __name__ == '__main__':
    main()
