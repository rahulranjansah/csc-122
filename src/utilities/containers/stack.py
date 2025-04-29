from typing import TypeVar, Generic, List
from collections.abc import Collection, Iterator

T = TypeVar("T")

class Stack(Generic[T]):
    """A simple generic stack implementation."""

    def __init__(self):
        """Initialize an empty stack."""
        self._stack = []

    def push(self, val: T) -> None:
        """Add an element to the top of the stack."""
        self._stack.append(val)

    def pop(self) -> T:
        """Remove and return the top element of the stack."""
        return self._stack.pop()

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._stack) == 0

    def top(self) -> T:
        """Return the top element without removing it."""
        if self.is_empty():
            return "Stack is empty"
        return self._stack[-1]

    def __contains__(self, val: T) -> bool:
        """Check if an element is in the stack."""
        return val in self._stack

    def __len__(self) -> int:
        """Return the number of elements in the stack."""
        count = 0
        for _ in self._stack:
            count += 1
        return count

    def __str__(self) -> str:
        """Provide a string representation of the stack."""
        return f"The entire stack {self._stack}"
