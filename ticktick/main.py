import argparse
from ticktick_manager import TicktickManager


def main():
    parser = argparse.ArgumentParser()
    tt = TicktickManager()
    parser.add_argument('mode', help='command mode')

    parser.add_argument('--new_task_name', help='name of TickTick task to be created', default='default_value')
    parser.add_argument('--new_project_name', help='name of TickTick project to be created', default='default_value')
    parser.add_argument('--new_section_name', help='name of TickTick project section to be created', default='default_value')
    parser.add_argument('--task_id', help='TickTick task id', default='default_value')
    parser.add_argument('--project_id', help='TickTick project id', default='default_value')
    parser.add_argument('--section_id', help='TickTick section id', default='default_value')
    args = parser.parse_args()

    if args.mode == 'add_new_task' and args.new_task_name:
        tt.task_manager.add_new_task(task={
            'title': args.new_task_name,
            'projectId': args.project_id if args.project_id else None,
            'columnId': args.section_id if args.section_id else None,
            'tags': ['notion']
        })
    elif args.mode == 'get_task_focus_duration' and args.task_id:
        task_duration = tt.task_manager.get_task_focus_duration(args.task_id)
        print(task_duration / 3600)  # convert output to unit hour
    elif args.mode == 'add_new_project' and args.new_project_name:
        tt.project_manager.add_new_project(project={'name': args.new_project_name})
    elif args.mode == 'add_new_project_section' and args.new_section_name and args.project_id:
        tt.project_manager.add_new_project_section(project_id=args.project_id, section_names=[args.new_section_name])


if __name__ == '__main__':
    main()
