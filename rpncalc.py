#!/usr/bin/env python3
from collections import namedtuple
from stack import Stack


Operator = namedtuple('Operator', ['function', 'arity'])


class RPNCalc(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stack = Stack()

    def ops(self):
        return self.keys()

    def solve(self, input_stack):
        while input_stack.size() > 0:
            value = input_stack.pop()
            if value in self.ops():
                op = self[value].function
                args = self.stack.pop(self[value].arity)
                args = args if isinstance(args, list) else [args]
                self.stack.push(op(*args))
            else:
                self.stack.push(value)
        result = self.stack[::]
        self.stack.empty()
        return result


if __name__ == '__main__':
    import sys
    from math import sqrt

    ops = {
        '+': Operator(lambda x, y: x + y, 2),
        '-': Operator(lambda x, y: x - y, 2),
        '*': Operator(lambda x, y: x * y, 2),
        '/': Operator(lambda x, y: x / y, 2),
        'sqrt': Operator(lambda x: sqrt(x), 1),
        'if': Operator(
            lambda cond_value, if_value, else_value:
            if_value if cond_value >= 0 else else_value,
            3
        )
    }

    calc = RPNCalc(ops)
    input_stack = Stack()
    for v in ('if', '-', 2, 3, '+', 3, 3, 0):
        input_stack.push(v)
    print(input_stack)
    print(calc.solve(input_stack))
