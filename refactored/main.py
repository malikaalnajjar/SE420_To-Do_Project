from refactored.task_manager import TaskManager

MENU = """
1. Add task
2. Delete task
3. Complete task
4. List tasks
5. Quit"""


def _read_priority() -> str:
    """Prompt for priority and return 'Medium' if the user presses Enter."""
    raw = input("Priority [Low / Medium / High] (default Medium): ").strip()
    if raw in ("Low", "High"):
        return raw
    return "Medium"


def run() -> None:
    """Main CLI loop. Handles only I/O; all business logic is in TaskManager."""
    manager = TaskManager()

    while True:
        print(MENU)
        choice = input("Choice: ").strip()

        if choice == "1":
            description = input("Description: ").strip()
            priority = _read_priority()
            task = manager.add_task(description, priority)  # type: ignore[arg-type]
            print(f"Added: {task}")

        elif choice == "2":
            try:
                task_id = int(input("Task ID to delete: "))
                manager.delete_task(task_id)
                print("Task deleted.")
            except ValueError as exc:
                print(f"Error: {exc}")

        elif choice == "3":
            try:
                task_id = int(input("Task ID to complete: "))
                manager.complete_task(task_id)
                print("Task marked as done.")
            except ValueError as exc:
                print(f"Error: {exc}")

        elif choice == "4":
            tasks = manager.list_tasks()
            if not tasks:
                print("No tasks.")
            else:
                for task in tasks:
                    print(task)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Enter 1-5.")


if __name__ == "__main__":
    run()
