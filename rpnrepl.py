#!/usr/bin/env python3
from collections import namedtuple


Operator = namedtuple('Operator', ['function', 'arity'])


class Stack(list):
    """Stack class."""
    def pop(self, n=1):
        result = self[-(n):]
        del self[-(n):]
        return result

    def push(self, value):
        self.append(value)

    def top(self):
        return self[-1]

    def size(self):
        return len(self)

    def empty(self):
        for i in range(self.size()):
            self.pop()


class RPNCalc(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stack = Stack()

    def ops(self):
        return self.keys()

    def solve(self, input_stack):
        return []

if __name__ == '__main__':
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '//': lambda x, y: x // y,
        '%': lambda x, y: x % y,
        '^': lambda x, y: x ** y
    }
    calc = RPNCalc(ops)
