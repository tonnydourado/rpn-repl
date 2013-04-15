#!/usr/bin/env python3


class RPNREPL(dict):
    def __init__(self, quit_command, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stack = []
        self.quit = quit_command

    def clean_stack(self):
        self.stack = []

    def ops(self):
        return self.keys()

    def solve(self, input_stack):
        while len(input_stack) > 0:
            op = input_stack.pop(0)
            if op == self.quit:
                self.stack.insert(0, self.quit)
                break
            if op in self.ops():
                arg1, arg2 = self.stack.pop(0), self.stack.pop(0)
                self.stack.insert(0, self[op](arg1, arg2))
            else:
                self.stack.insert(0, op)
        result = self.stack[::]
        self.clean_stack()
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
        input_stack = []
        for token in tokens:
            if is_op(token) or is_quit(token):
                input_stack.append(token)
            else:
                number = to_number(token)
                if number is not None:
                    input_stack.append(number)
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
