# Class Diagram — SE 420 To-Do List (Refactored)

Generated for Section 3 (Reverse Engineering) of the project report.

```mermaid
classDiagram
    class Task {
        +int id
        +str description
        +Priority priority
        +Status status
        +mark_done() None
        +__str__() str
    }

    class TaskManager {
        -list~Task~ _tasks
        -int _next_id
        +add_task(description: str, priority: Priority) Task
        +delete_task(task_id: int) None
        +complete_task(task_id: int) None
        +list_tasks() list~Task~
        -_find(task_id: int) Task
    }

    TaskManager "1" --> "0..*" Task : manages
```

## Type aliases

| Alias      | Definition                          |
|------------|-------------------------------------|
| `Priority` | `Literal["Low", "Medium", "High"]`  |
| `Status`   | `Literal["pending", "done"]`        |

## Notes

- `TaskManager._tasks` is private; callers receive a copy via `list_tasks()`.
- `TaskManager._find()` is a private helper used by `delete_task` and
  `complete_task` to keep those methods to two lines each (Refactoring 4).
- `Task` is a plain `@dataclass`; `TaskManager` owns the id-generation
  counter `_next_id` to avoid duplicate ids across its lifetime.
