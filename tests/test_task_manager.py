import pytest

from refactored.task_manager import TaskManager


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def manager() -> TaskManager:
    return TaskManager()


# ---------------------------------------------------------------------------
# add_task
# ---------------------------------------------------------------------------


def test_add_task_assigns_sequential_ids(manager: TaskManager) -> None:
    t1 = manager.add_task("First")
    t2 = manager.add_task("Second")
    t3 = manager.add_task("Third")
    assert t1.id == 1
    assert t2.id == 2
    assert t3.id == 3


def test_add_task_stores_description_and_priority(manager: TaskManager) -> None:
    task = manager.add_task("Buy milk", "High")
    assert task.description == "Buy milk"
    assert task.priority == "High"


def test_add_task_defaults_to_medium_priority(manager: TaskManager) -> None:
    task = manager.add_task("Walk the dog")
    assert task.priority == "Medium"


# ---------------------------------------------------------------------------
# delete_task
# ---------------------------------------------------------------------------


def test_delete_task_removes_the_task(manager: TaskManager) -> None:
    manager.add_task("Task A")
    manager.add_task("Task B")
    manager.delete_task(1)
    ids = [t.id for t in manager.list_tasks()]
    assert 1 not in ids
    assert 2 in ids


def test_delete_task_raises_on_unknown_id(manager: TaskManager) -> None:
    with pytest.raises(ValueError, match="Task not found"):
        manager.delete_task(999)


# ---------------------------------------------------------------------------
# complete_task
# ---------------------------------------------------------------------------


def test_complete_task_marks_done(manager: TaskManager) -> None:
    manager.add_task("Write report")
    manager.complete_task(1)
    task = manager.list_tasks()[0]
    assert task.status == "done"


def test_complete_task_raises_on_unknown_id(manager: TaskManager) -> None:
    with pytest.raises(ValueError, match="Task not found"):
        manager.complete_task(42)


# ---------------------------------------------------------------------------
# list_tasks
# ---------------------------------------------------------------------------


def test_list_tasks_returns_copy_not_internal_list(manager: TaskManager) -> None:
    manager.add_task("Alpha")
    snapshot = manager.list_tasks()
    snapshot.clear()
    assert len(manager.list_tasks()) == 1
