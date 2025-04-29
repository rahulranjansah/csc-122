import unittest
from src.utilities.containers.doubly_linked_list import DoublyLinkedList, EmptyCollectionException

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

    def list_to_dll(self, arr: list) -> DoublyLinkedList:
        """
        Utility: Build a DoublyLinkedList by pushing back all values.
        """
        dll = DoublyLinkedList()
        for item in arr:
            dll.push_back(item)
        return dll

    def test_len_and_str(self):
        # Empty list
        self.assertEqual(len(self.dll), 0)
        self.assertEqual(str(self.dll), "")
        # Non-empty
        arr = [1, 2, 3]
        dll = self.list_to_dll(arr)
        self.assertEqual(len(dll), 3)
        self.assertEqual(str(dll), "1 <-> 2 <-> 3")

    def test_contains(self):
        dll = self.list_to_dll([10, 20, 30])
        self.assertTrue(20 in dll)
        self.assertFalse(40 in dll)

    def test_iteration(self):
        arr = ["a", "b", "c"]
        dll = self.list_to_dll(arr)
        items = []
        for x in dll:
            items.append(x)
        self.assertEqual(items, arr)
        # Ensure that a new iterator resets
        items2 = []
        for x in dll:
            items2.append(x)
        self.assertEqual(items2, arr)

    def test_get_set_item(self):
        dll = self.list_to_dll([0, 0, 0])
        # getitem
        self.assertEqual(dll[1], 0)
        # setitem
        dll[1] = 99
        self.assertEqual(dll[1], 99)
        # out of range
        with self.assertRaises(IndexError):
            _ = dll[5]
        with self.assertRaises(IndexError):
            dll[5] = 5

    def test_del_item(self):
        dll = self.list_to_dll([1, 2, 3, 4])
        # delete middle
        del dll[2]
        self.assertEqual(len(dll), 3)
        self.assertEqual(str(dll), "1 <-> 2 <-> 4")
        # delete first
        del dll[0]
        self.assertEqual(str(dll), "2 <-> 4")
        # delete last
        del dll[len(dll)-1]
        self.assertEqual(str(dll), "2")
        # out of range
        with self.assertRaises(IndexError):
            del dll[5]

    def test_index(self):
        dll = self.list_to_dll(["x", "y", "z", "y"])
        self.assertEqual(dll.index("y"), 1)
        with self.assertRaises(ValueError):
            dll.index("not_present")

    def test_remove_at(self):
        dll = self.list_to_dll([1, 2, 3])
        # valid index
        self.assertTrue(dll.remove_at(1))
        self.assertEqual(str(dll), "1 <-> 3")
        # invalid index
        self.assertFalse(dll.remove_at(5))
        # negative index
        self.assertFalse(dll.remove_at(-1))

    def test_push_front_and_back(self):
        self.dll.push_front('a')
        self.dll.push_back('b')
        self.dll.push_front('start')
        self.assertEqual(str(self.dll), "start <-> a <-> b")

    def test_pop_front(self):
        dll = self.list_to_dll([10, 20, 30])
        self.assertEqual(dll.pop_front(), 10)
        self.assertEqual(dll.pop_front(), 20)
        self.assertEqual(len(dll), 1)
        # pop until empty
        self.assertEqual(dll.pop_front(), 30)
        self.assertTrue(dll.is_empty())
        with self.assertRaises(EmptyCollectionException):
            dll.pop_front()

    def test_clear_and_is_empty(self):
        dll = self.list_to_dll([1, 2])
        self.assertFalse(dll.is_empty())
        dll.clear()
        self.assertTrue(dll.is_empty())
        self.assertEqual(len(dll), 0)
        self.assertEqual(str(dll), "")

    def test_remove_and_remove_all(self):
        dll = self.list_to_dll([1, 2, 2, 3, 2])
        # remove first occurrence
        self.assertTrue(dll.remove(2))
        self.assertEqual(str(dll), "1 <-> 2 <-> 3 <-> 2")
        # remove non-existent
        self.assertFalse(dll.remove(42))
        # remove_all occurrences
        count = dll.remove_all(2)
        self.assertEqual(count, 2)
        self.assertEqual(str(dll), "1 <-> 3")
        # remove_all when none
        self.assertEqual(dll.remove_all(5), 0)

    def test_collect(self):
        dll = self.list_to_dll([5, 6, 5, 7, 5])
        self.assertEqual(dll.collect(5), [5, 5, 5])
        self.assertEqual(dll.collect(6), [6])
        self.assertEqual(dll.collect(42), [])

if __name__ == "__main__":
    unittest.main()