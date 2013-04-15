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


class RPNREPL(dict):
    def __init__(self, quit_command, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stack = Stack()
        self.quit = quit_command

    def ops(self):
        return self.keys()

    def solve(self, input_stack):
        while len(input_stack) > 0:
            op = input_stack.pop()
            if op == self.quit:
                self.stack.push(self.quit)
                break
            if op in self.ops():
                print(self.stack.pop(2))
                self.stack.push(op)
            else:
                self.stack.push(op)
        result = self.stack[::]
        self.stack.empty()
        return result

    def parse(self, raw_input):
        def to_number(token):
            try:
                return int(token)
            except ValueError:
                try:
                    return float(token)
                except ValueError:
                    return None

        is_op = lambda token: token in self.ops()
        is_quit = lambda token: token == self.quit

        tokens = raw_input.split(' ')
        input_stack = Stack()
        for token in tokens:
            if is_op(token) or is_quit(token):
                input_stack.push(token)
            else:
                number = to_number(token)
                if number is not None:
                    input_stack.push(number)
                else:
                    raise ValueError('Invalid number: ' + token)
        return input_stack

    def run(self):
        while True:
            raw_input = input(': ')
            try:
                result = self.solve(self.parse(raw_input))
            except ValueError as e:
                print(e)
                raise e
                continue
            except IndexError:
                print('Mal formed expression')
                continue
            if self.quit in result:
                result.pop(result.index(calc.quit))
                break
            print(result)
        print(result)


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
    calc = RPNREPL('quit', ops)
    calc.run()
