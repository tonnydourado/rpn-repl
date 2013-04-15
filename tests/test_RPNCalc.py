#!/usr/bin/env python3

import unittest
from rpnrepl import RPNCalc, Operator, Stack
from math import sqrt


class TestRPNCalc(unittest.TestCase):
    """Test case for class RPNCalc."""
    def setUp(self):
        self.ops = {
            'q': Operator(lambda: None, 0),
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
        self.calc = RPNCalc(self.ops)

    def test_ops(self):
        """"Tests every operator except for the quit command."""
        ops = [op for op in self.calc.ops() if op != 'q']
        for op in ops:
            input_stack = Stack()

            input_stack.push(op)

            args = tuple(range(1, self.calc[op].arity + 1))
            for arg in args:
                input_stack.push(arg)

            result = self.calc.solve(input_stack)
            print('BUNDINHA', op, args, self.ops[op].function(*args))
            self.assertSequenceEqual(result, [self.ops[op].function(*args)])

    def test_quit_alone(self):
        """Tests the quit command alone"""
        input_stack = ['q']
        result = self.calc.solve(input_stack)
        self.assertEqual(result, [])

    def test_quit_in_expression(self):
        """Tests the quit command in the middle of a expression"""
        input_stack = [1, 2, '+', 3, 3, '-', 'q', '*']
        result = self.calc.solve(input_stack)
        self.assertEqual(result, [3, 6])
