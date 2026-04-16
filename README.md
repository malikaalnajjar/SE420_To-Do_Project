# SE 420 — To-Do Project

A two-version CLI to-do list application built for SE 420 Software Maintenance
& Evolution. The project demonstrates software re-engineering by contrasting a
deliberately-bad legacy implementation with a cleanly-refactored modern one.

## Project structure

```
se420-todo-project/
├── legacy/
│   └── todo_legacy.py        # bad version — exhibits Fowler code smells
├── refactored/
│   ├── task.py               # Task dataclass + Literal type aliases
│   ├── task_manager.py       # TaskManager — all business logic
│   └── main.py               # thin CLI — I/O only
├── tests/
│   └── test_task_manager.py  # pytest suite (8 tests)
└── docs/
    └── class_diagram.md      # Mermaid class diagram
```

## Running the legacy version

```bash
python legacy/todo_legacy.py
```

## Running the refactored version

Run from the project root so that the `refactored` package is on the path:

```bash
python -m refactored.main
```

## Running the tests

```bash
pip install pytest          # once, if not already installed
pytest tests/               # run all 8 tests
```

All tests should report green with no warnings.

## How the refactored code maps to the four refactorings

The refactored version applies four named refactorings in sequence:

1. **Remove Duplication** — The legacy `add_task()` and `add_urgent_task()`
   functions were nearly identical. They are replaced by a single
   `TaskManager.add_task(description, priority)` method that accepts a
   `priority` parameter, eliminating the duplicated dict-building and
   list-appending code.

2. **Extract Method** — The legacy `do_everything()` function handled every
   operation inline inside one 50-line loop. Each operation is now its own
   method on `TaskManager` (`add_task`, `delete_task`, `complete_task`,
   `list_tasks`). `main.py` only reads input and prints output.

3. **Rename Variables** — Cryptic single-letter names (`c`, `d`, `i`, `x`,
   `t`) are replaced throughout with self-documenting names: `choice`,
   `description`, `task_id`, `task`. This makes every line of the refactored
   code readable without comments.

4. **Simplify Long Method** — `delete_task` and `complete_task` previously
   duplicated a linear search over the task list. A private helper
   `_find(task_id)` centralises that search and raises `ValueError` when the
   id is absent, keeping both public methods to exactly two lines each.
