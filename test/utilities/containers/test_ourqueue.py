import unittest
from src.utilities.containers.ourqueue import *
class TestOurQueue(unittest.TestCase):
    def setUp(self):

        self.dll = OurQueue()

    def list_to_dll(self, arr: list) -> OurQueue:
        """Convert a Python list to an OurQueue"""
        dll = OurQueue()
        for item in arr:
            dll.enqueue(item)
        return dll

    def test_enqueue(self):
        """Test adding elements to the queue"""
        self.dll.enqueue(10)
        self.dll.enqueue('a')
        self.dll.enqueue('')
        self.assertEqual(len(self.dll), 3)
        self.assertEqual(str(self.dll), "10 a ")

    def test_dequeue(self):
        """Test removing elements from the queue"""
        arr = [10, 20, 30, '', 'a']
        dll = self.list_to_dll(arr)
        self.assertEqual(str(dll), "10 20 30  a")
        self.assertEqual(dll.dequeue(), 10)
        self.assertEqual(dll.dequeue(), 20)
        self.assertEqual(len(dll), 3)
        self.assertEqual(str(dll), "30  a")

    def test_is_empty(self):
        """Test checking if the queue is empty"""
        arr = ['', '&', '<']
        dll = self.list_to_dll(arr)
        self.assertFalse(dll.is_empty())
        dll.clear()
        self.assertTrue(dll.is_empty())

    def test_contains(self):
        """Test element containment in the queue"""
        arr = [10, 20, 30]
        dll = self.list_to_dll(arr)
        self.assertTrue(10 in dll)
        self.assertFalse(40 in dll)

    def test_top(self):
        """Test retrieving the front element of the queue"""
        arr = [100, 200, 300]
        dll = self.list_to_dll(arr)
        self.assertEqual(dll.top(), 100)
        dll.dequeue()
        self.assertEqual(dll.top(), 200)

    def test_len_and_str(self):
        """Test length and string representation of the queue"""
        self.assertEqual(len(self.dll), 0)
        self.assertEqual(str(self.dll), "")
        arr = [1, 2, 3]
        dll = self.list_to_dll(arr)
        self.assertEqual(len(dll), 3)
        self.assertEqual(str(dll), "1 2 3")

if __name__ == '__main__':
    unittest.main()