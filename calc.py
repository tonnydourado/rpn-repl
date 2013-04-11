#!/usr/bin/env python3
if __name__ == '__main__':
    while True:
        stack = []
        raw_input = input(':')
        if raw_input == 'quit':
            break
        else:
            tokens = raw_input.split(' ')
            while len(tokens) > 0:
                token = tokens.pop(0)
                if token == '+':
                    arg1 = stack.pop(0)
                    arg2 = stack.pop(0)
                    stack.insert(0, arg1 + arg2)
                elif token == '-':
                    arg1 = stack.pop(0)
                    arg2 = stack.pop(0)
                    stack.insert(0, arg1 - arg2)
                elif token == '*':
                    arg1 = stack.pop(0)
                    arg2 = stack.pop(0)
                    stack.insert(0, arg1 * arg2)
                elif token == '/':
                    arg1 = stack.pop(0)
                    arg2 = stack.pop(0)
                    stack.insert(0, arg1 / arg2)
                else:
                    try:
                        number = int(token)
                    except ValueError:
                        try:
                            number = float(token)
                        except ValueError:
                            print('ValueError: invalid number: ' + token)
                            break
                    stack.insert(0, number)
            else:
                print(stack)
            
            
        





    
        
