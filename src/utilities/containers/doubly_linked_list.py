from typing import TypeVar, Generic, List
from collections.abc import Collection, Iterator

T = TypeVar("T")

class EmptyCollectionException(Exception):
    pass

class DNode(Generic[T]):
    """Node class """
    def __init__(self, data: T = None, prev: 'DNode' = None, next: 'DNode' = None):
        self._data = data
        self._prev = prev
        self._next = next


class DoublyLinkedList(Collection, Iterator, Generic[T]):
    def __init__(self) -> None:
        self._head = DNode()
        self._tail = DNode()
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0


    def __insert(self, data: T, left: DNode) -> None:
        new_node = DNode(data, prev=left, next=left._next)
        left._next._prev = new_node
        left._next = new_node
        self._size += 1

    # node already have been referenced
    def __remove(self, node: DNode) -> None:
        node._prev._next = node._next
        node._next._prev = node._prev
        self._size -= 1


    def __get_node(self, value: T) -> DNode:
        current = self._head._next
        while current != self._tail:
            if current._data == value:
                return current
            current = current._next
        return None

    def __last(self) -> DNode:
        return self._tail._prev

    def __contains__(self, value: T) -> bool:
        return self.__get_node(value) is not None

    def __iter__(self) -> DoublyLinkedList:
        """Initialize the iterator and return the list itself. (Given sentinel)"""
        self._current = self._head._next
        return self

    def __next__(self):
        if self._head == self._tail:
            return StopIteration

        value = self._head._data
        self._head = self._head._next

        return value

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int) -> T:
        """Return the item located at the 0-based index."""
        if index <  0 and index >= self._size:
            raise IndexError("Index out of range")

        current = self._head._next
        for i in range(index):
            current = current._next

        return current._data

    def __setitem__(self, index: int, val: T) -> None:
        """Set the item located at the 0-based index."""
        if index <  0 and index >= self._size:
            raise IndexError("Index out of range")

        current = self._head._next
        for i in range(index):
            curent = current._next

        current._data = val

    def __delitem__(self, index: int) -> T:
        """Set the item located at the 0-based index."""
        if index <  0 and index >= self._size:
            raise IndexError("Index out of range")

        current = self._head._next
        for i in range(index):
            current = current._next

        current._prev._next = current._next
        current._next._next = current._prev

        self._size -= 1

        return current._data

    def __str__(self) -> str:
        values = []
        current = self._head._next
        while current != self._tail:
            values.append(str(current._data))
            current = current._next
        return " <-> ".join(values)

    def index(self, val: T) -> int:
        """Returns the 0-based index of the first occurrence of val."""
        count = 0
        current = self._head
        while current:
            if val == current._data:
                return count

            count += 1
            current = current._next

        return -(self._size + 1)


    def remove(self, value: T) -> bool:
        node = self.__get_node(value)
        if node is not None:
            self.__remove(node)
            return True
        return False

    def remove_all(self, value: T) -> int:
        count = 0
        current = self._head._next
        while current != self._tail:
            if current._data == value:
                next_node = current._next
                self.__remove(current)
                count += 1
                current = next_node
            else:
                current = current._next
        return count

    def front(self):
        return self._head._next._data

    def back(self):
        return self._tail._prev._data

    def push_front(self, value : T):
        self.__insert(value, self._head)

    def push_back(self, value : T):
        self.__insert(value, self._tail._prev)

    def pop_front(self):
        if self.is_empty():
            return EmptyCollectionException(Exception)
        node = self._head._next
        value = node._data

        self.__remove(node)
        return value

    def clear(self):
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def collect(self, value : T):
        matches = []
        current = self._head._next
        while current != self._tail:
            if current._data == value:
                matches.append(current._data)
            current = current._next

        return matches


