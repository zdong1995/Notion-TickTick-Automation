import argparse
from ticktick_manager import TicktickManager


def main():
    parser = argparse.ArgumentParser()
    tt = TicktickManager()
    parser.add_argument("mode", help="command mode")

    parser.add_argument("--task_id", help="TickTick task id", default="default_value")
    parser.add_argument("--title_name", help="TickTick task name", default="default_value")
    args = parser.parse_args()

    if args.mode == 'add_new_task' and args.title_name:
        tt.task_manager.add_new_task(task={"title": args.title_name})
    if args.mode == 'get_task_focus_duration' and args.task_id:
        task_duration = tt.task_manager.get_task_focus_duration(args.task_id)
        print(task_duration)


if __name__ == "__main__":
    main()
