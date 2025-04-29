from typing import TypeVar, Generic, Optional
from collections.abc import Collection, Iterator
from src.utilities.containers.doubly_linked_list import *

T = TypeVar("T")

class OurQueue(Collection, Generic[T]):
    """Queue class wrapper around DLLs"""
    def __init__(self) -> None:
        self._queue = DoublyLinkedList[T]()

    def enqueue(self, val: T) -> None:
        """Add an element to the back of the queue"""
        self._queue.push_back(val)

    def dequeue(self) -> T:
        """Remove and return the front element of the queue"""
        return self._queue.pop_front()

    def top(self) -> T:
        """Return the front element of the queue without removing it"""
        if self.is_empty():
            raise EmptyCollectionException("Queue is empty")
        return self._queue.front()

    def is_empty(self) -> bool:
        """Check if the queue is empty"""
        return self._queue.is_empty()

    def clear(self) -> None:
        """Remove all elements from the queue"""
        self._queue.clear()

    def __contains__(self, val: T) -> bool:
        """Contains in queue bool"""
        return val in self._queue

    def __len__(self) -> int:
        """Return the elements in the queue"""
        return len(self._queue)

    def __iter__(self):
        """Iterate over the elements of the queue"""
        return iter(self._queue)

    def __str__(self) -> str:
        """String separated representations"""
        return " ".join(str(item) for item in self._queue)