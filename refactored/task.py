from dataclasses import dataclass
from typing import Literal

Priority = Literal["Low", "Medium", "High"]
Status = Literal["pending", "done"]


@dataclass
class Task:
    id: int
    description: str
    priority: Priority = "Medium"
    status: Status = "pending"

    def mark_done(self) -> None:
        """Mark this task as done."""
        self.status = "done"

    def __str__(self) -> str:
        return f"[{self.id}] ({self.priority}) {self.description} — {self.status}"
