from typing import TypeVar
T = TypeVar("T")
class Node:
	def __init__(self, data: T, next: 'Node'):
		self.data = data
		self.next = next
		
class SinglyLinkedList:
	def __init__(self):
		self._head = None
		self._size = 0
		
	def __str__(self):
		output = []
		current = self._head
		while current is not None:
			output.append(current.data)
			current = current.next
		return ', '.join(output)
		
	def __get_prev(self, index: int) -> 'Node':
		current = self._head
		current_idx = 0
		while current_idx < index - 1:
			current = current.next
			current_idx += 1
		return current
		
	def __insert(self, data: T, prev: 'Node') -> None:
		if prev is None:
			n = Node(data, None)
			self._head = n
		else:
			n = Node(data, prev.next)
			prev.next = n
		self._size += 1
		
	def insert(self, data: T, index: int) -> None:
		self.__insert(data, self.__get_prev(index))
		
def main():
	l = SinglyLinkedList()
	l.insert('a', 0)
	l.insert('c', 1)
	l.insert('b', 0)
	print(l)
	
if __name__ == '__main__':
	main()