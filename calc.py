#!/usr/bin/env python3

class Calc(dict):
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
                self.clean_stack()
                return
            if op in self.keys():
                arg1 = self.stack.pop(0)
                arg2 = self.stack.pop(0)
                self.stack.insert(0, self[op](arg1, arg2))
            else:
                self.stack.insert(0, op)
        result = self.stack[::]
        self.clean_stack()
        return result

if __name__ == '__main__':
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }
    calc = Calc('quit', ops)

    
    while True:
        raw_input = input(':')
        tokens = raw_input.split(' ')
        input_stack = []
        for token in tokens:
            if token == calc.quit:
                input_stack.append(token)
            elif token in calc.ops():
                input_stack.append(token)
            else:            
                try:
                    number = int(token)
                except ValueError:
                    try:
                        number = float(token)
                    except ValueError:
                        print('ValueError: invalid number: ' + token)
                        break
                input_stack.append(number)
        else:
            result = calc.solve(input_stack)
            if result is None:
                break
            else:
                print(result)
                                
            
            
        





    
        
