from typing import TypeVar, Generic, List
from collections.abc import Collection, Iterator

T = TypeVar("T")

class Stack(Generic[T]):

    def __init__(self):
        self._stack = []

    def push(self, val: T) -> None:
        self._stack.append(val)

    def pop(self) -> T:
        return self._stack.pop()

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._stack) == 0

    def top(self) -> T:
        if self.is_empty():
            return "Stack is empty"
        return self._stack[-1]

    def __contains__(self, val: T) -> bool:
        return val in self._stack

    def __len__(self) -> int:
        count = 0
        for _ in self._stack:
            count += 1

        return count

    def __str__(self) -> str:
        return f"The entire stack {self._stack}"

# stack = Stack()
# stack.push(1)
# stack.push(1)
# stack.push(1)
# print(stack)
# print(3 in stack)
# print(1 in stack)
# print(is_empty(stack))