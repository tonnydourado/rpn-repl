#!/usr/bin/env python3
from cmd import Cmd
from stack import Stack


class RPNREPL(Cmd):
    """REPL (Read-Eval-Print Loop) for RPNCalc"""
    def __init__(self, calc):
        super(RPNREPL, self).__init__()
        self.calc = calc

    def do_quit(self, arg):
        return True

    def default(self, arg):
        if arg == 'EOF':
            return True
        else:
            # print()
            input_stack = Stack()
            tokens = parser(' '.join(reversed(arg.split())), self.calc.ops())
            try:
                for token in tokens:
                    input_stack.push(token)
            except ValueError as e:
                print(e)
            else:
                print(self.calc.solve(input_stack))


def parser(raw_input, ops):
    def to_number(str_n):
        try:
            return int(str_n)
        except ValueError:
            try:
                return float(str_n)
            except ValueError as e:
                e.args = ('invalid value "{}"'.format(str_n),)
                raise e

    tokens = raw_input.split()
    for token in tokens:
        if token in ops:
            yield token
        else:
            yield to_number(token)

if __name__ == '__main__':
    from math import sqrt
    from rpncalc import Operator, RPNCalc

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

    RPNREPL(RPNCalc(ops)).cmdloop()
