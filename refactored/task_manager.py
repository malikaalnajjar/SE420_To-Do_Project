from refactored.task import Priority, Task


class TaskManager:
    """Manages a collection of tasks. No global state."""

    def __init__(self) -> None:
        self._tasks: list[Task] = []
        self._next_id: int = 1

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def add_task(self, description: str, priority: Priority = "Medium") -> Task:
        """Create a new task and return it.

        Refactoring 1 (Remove Duplication): replaces add_task() and
        add_urgent_task() from the legacy version with a single method.
        Refactoring 2 (Extract Method): business rule lives here, not in main.
        """
        task = Task(id=self._next_id, description=description, priority=priority)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def delete_task(self, task_id: int) -> None:
        """Remove the task with the given id.

        Raises ValueError if the id is not found.
        Refactoring 4 (Simplify Long Method): delegates lookup to _find().
        """
        task = self._find(task_id)
        self._tasks.remove(task)

    def complete_task(self, task_id: int) -> None:
        """Mark the task with the given id as done.

        Raises ValueError if the id is not found.
        Refactoring 4 (Simplify Long Method): delegates lookup to _find().
        """
        task = self._find(task_id)
        task.mark_done()

    def list_tasks(self) -> list[Task]:
        """Return a copy of the task list so callers cannot mutate internal state."""
        return list(self._tasks)

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _find(self, task_id: int) -> Task:
        """Return the Task whose id matches task_id, or raise ValueError."""
        for task in self._tasks:
            if task.id == task_id:
                return task
        raise ValueError("Task not found")
