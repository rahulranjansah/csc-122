import unittest

from src.utilities.containers.doubly_linked_list import DoublyLinkedList, DNode, EmptyCollectionException

class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        """A new doublylinkedlist"""
        self.dll = DoublyLinkedList()

    def list_to_dll(self, arr: list) -> DoublyLinkedList:

        dll = DoublyLinkedList()
        current = dll._head

        for item in arr:

            new_node = DNode(item)

            next_node = current._next
            current._next = new_node

            new_node._next = next_node
            new_node._prev = current

            current = new_node

            dll._size += 1

        return dll

    def test_push_front(self):

        self.dll.push_front(10)
        self.dll.push_front(20)
        self.dll.push_front(30)

        # pushing in size
        self.assertEqual(len(self.dll), 3)

        # string check
        self.assertEqual(str(self.dll), "30 <-> 20 <-> 10")

    def test_push_back(self):

        self.dll.push_back(10)
        self.dll.push_back('a')
        self.dll.push_back('')

        # pushing back size
        self.assertEqual(len(self.dll), 3)

        # string check
        self.assertEqual(str(self.dll), "10 <-> a <-> ")

    def test_pop_front(self):

        arr = [10,20,30,'', 'a']

        dll = self.list_to_dll(arr)

        self.assertEqual(str(dll), "10 <-> 20 <-> 30 <->  <-> a")

        # poping front
        dll.pop_front()

        self.assertEqual(dll.pop_front(), 20)
        self.assertEqual(len(dll), 3)
        self.assertEqual(str(dll), '30 <->  <-> a')

    def test_front(self):

        arr = ['a', 20, 30]
        dll = self.list_to_dll(arr)

        self.assertEqual(dll.front(), 'a')

        dll.pop_front()
        self.assertEqual(dll.front(), 20)

        dll.push_back(30)
        self.assertEqual(dll.front(), 30)

        dll.pop_front()
        dll.pop_front()
        dll.pop_front()

        self.assertEqual(dll.front(), None)

    def test_back(self):

        arr = ['a', 20, 30]
        dll = self.list_to_dll(arr)

        self.assertEqual(dll.back(), None)

        dll.pop_front()
        dll.pop_front()
        dll.pop_front()

        self.assertEqual(dll.back(), None)


    def test_is_empty(self):
        arr = ['', '&', '<']
        dll = self.list_to_dll(arr)

        self.assertFalse(dll.is_empty())

        dll.clear()
        self.assertTrue(dll.is_empty())


    def test_remove_all(self):

        arr = ['', '', '', '']
        dll = self.list_to_dll(arr)
        self.assertFalse(dll.is_empty())
        self.assertEqual(dll.remove_all(''), 4)

        arr2 = [1,3,4,'5',3,3]
        dll = self.list_to_dll(arr2)
        self.assertFalse(dll.is_empty())
        self.assertEqual(dll.remove_all(''), 0)
        self.assertEqual(dll.remove_all(3), 3)

    def test_remove(self):

        arr = ['', '', '', '']
        dll = self.list_to_dll(arr)

        self.assertTrue(dll.remove(''))
        self.assertFalse(dll.remove("a"))

    def test_collect(self):
        arr = ['a', 'b', 'c', 'd']
        dll = self.list_to_dll(arr)

        self.assertEqual(dll.collect('k'), [])
        self.assertEqual(dll.collect('b'), ['b'])
        self.assertEqual(dll.collect('d'), ['d'])

        dll.push_front(5)

        self.assertEqual(dll.collect(5), [5])

        dll.push_back('b')
        self.assertEqual(dll.collect('b'), ['b', 'b'])

if __name__ == "__main__":
    unittest.main()