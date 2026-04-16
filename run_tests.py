"""
Fallback test runner using unittest (no pytest required).
Run:  python3 run_tests.py
"""
import sys
import unittest

sys.path.insert(0, "/Users/malik/se420-todo-project")

from refactored.task_manager import TaskManager


class TestAddTask(unittest.TestCase):
    def setUp(self):
        self.mgr = TaskManager()

    def test_assigns_sequential_ids(self):
        t1 = self.mgr.add_task("First")
        t2 = self.mgr.add_task("Second")
        t3 = self.mgr.add_task("Third")
        self.assertEqual(t1.id, 1)
        self.assertEqual(t2.id, 2)
        self.assertEqual(t3.id, 3)

    def test_stores_description_and_priority(self):
        task = self.mgr.add_task("Buy milk", "High")
        self.assertEqual(task.description, "Buy milk")
        self.assertEqual(task.priority, "High")

    def test_defaults_to_medium_priority(self):
        task = self.mgr.add_task("Walk the dog")
        self.assertEqual(task.priority, "Medium")


class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.mgr = TaskManager()
        self.mgr.add_task("Task A")
        self.mgr.add_task("Task B")

    def test_removes_the_task(self):
        self.mgr.delete_task(1)
        ids = [t.id for t in self.mgr.list_tasks()]
        self.assertNotIn(1, ids)
        self.assertIn(2, ids)

    def test_raises_on_unknown_id(self):
        with self.assertRaisesRegex(ValueError, "Task not found"):
            self.mgr.delete_task(999)


class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        self.mgr = TaskManager()
        self.mgr.add_task("Write report")

    def test_marks_done(self):
        self.mgr.complete_task(1)
        task = self.mgr.list_tasks()[0]
        self.assertEqual(task.status, "done")

    def test_raises_on_unknown_id(self):
        with self.assertRaisesRegex(ValueError, "Task not found"):
            self.mgr.complete_task(42)


class TestListTasks(unittest.TestCase):
    def test_returns_copy_not_internal_list(self):
        mgr = TaskManager()
        mgr.add_task("Alpha")
        snapshot = mgr.list_tasks()
        snapshot.clear()
        self.assertEqual(len(mgr.list_tasks()), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
