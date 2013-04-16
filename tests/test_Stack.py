#!/usr/bin/env python3

import unittest
from rpnrepl import Stack


class TestStack(unittest.TestCase):
    """Test case for class Stack."""

    def setUp(self):
        self.N = 10
        self.NPOP = 3
        self.stack = Stack(range(self.N))

    def test_push(self):
        """push(value) adds values to the top of stack."""
        self.stack.push(self.N)
        self.assertSequenceEqual(self.stack, list(range(self.N + 1)))

    def test_pop_1(self):
        """pop() removes and returns the last pushed value."""
        self.assertEqual(self.stack.pop(), self.N - 1)

    def test_pop_n(self):
        """pop(n) removes and returns the last n (n > 1) pushed values."""
        poped = self.stack.pop(3)
        should_be_poped = list(range(self.N - 1, self.N - self.NPOP - 1, -1))
        self.assertSequenceEqual(poped, should_be_poped)

    def test_pop_0(self):
        """pop(0) returns a empty list."""
        self.assertEqual(self.stack.pop(0), [])

    def test_top(self):
        """top() returns the last pushed value, without removing it."""
        self.assertEqual(self.stack.top(), self.stack[-1])

    def test_size(self):
        """size() returns the stack's size."""
        self.assertEqual(self.stack.size(), len(self.stack))

    def test_empty(self):
        """empty() removes all values from the stack."""
        self.stack.empty()
        self.assertEqual(self.stack.size(), 0)


if __name__ == '__main__':
    unittest.main()
