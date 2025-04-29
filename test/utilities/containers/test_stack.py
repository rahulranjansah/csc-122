import unittest
from src.utilities.containers.stack import *

class TestStack(unittest.TestCase):
    """Unit tests for the Stack data structure"""

    def setUp(self):
        """Initialize an empty Stack before each test"""
        self.stack = Stack()

    def list_to_stack(self, arr: list) -> Stack:
        """Convert a Python list to a Stack"""
        stack = Stack()
        for item in arr:
            stack.push(item)
        return stack

    def test_push(self):
        """Test adding elements to the stack"""
        self.stack.push(10)
        self.stack.push('a')
        self.stack.push('')
        self.assertEqual(len(self.stack), 3)
        self.assertEqual(str(self.stack), "The entire stack [10, 'a', '']")

    def test_pop(self):
        """Test removing elements from the stack"""
        arr = [10, 20, 30, '', 'a']
        stack = self.list_to_stack(arr)
        self.assertEqual(str(stack), "The entire stack [10, 20, 30, '', 'a']")
        self.assertEqual(stack.pop(), 'a')
        self.assertEqual(stack.pop(), '')
        self.assertEqual(len(stack), 3)
        self.assertEqual(str(stack), "The entire stack [10, 20, 30]")

    def test_is_empty(self):
        """Test checking if the stack is empty"""
        arr = ['', '&', '<']
        stack = self.list_to_stack(arr)
        self.assertFalse(stack.is_empty())
        while not stack.is_empty():
            stack.pop()
        self.assertTrue(stack.is_empty())

    def test_contains(self):
        """Test element containment in the stack"""
        arr = [10, 20, 30]
        stack = self.list_to_stack(arr)
        self.assertTrue(10 in stack)
        self.assertFalse(40 in stack)

    def test_top(self):
        """Test retrieving the top element of the stack"""
        arr = [100, 200, 300]
        stack = self.list_to_stack(arr)
        self.assertEqual(stack.top(), 300)
        stack.pop()
        self.assertEqual(stack.top(), 200)

    def test_len_and_str(self):
        """Test length and string representation of the stack"""
        self.assertEqual(len(self.stack), 0)
        self.assertEqual(str(self.stack), "The entire stack []")
        arr = [1, 2, 3]
        stack = self.list_to_stack(arr)
        self.assertEqual(len(stack), 3)
        self.assertEqual(str(stack), "The entire stack [1, 2, 3]")

if __name__ == '__main__':
    unittest.main()
