#!/usr/bin/env python3


class Stack(list):
    """Stack class."""
    def pop(self, n=1):
        if n == 0:
            return []
        result = [super(Stack, self).pop() for i in range(n)]
        return result if len(result) > 1 else result.pop()

    def push(self, value):
        self.append(value)

    def top(self):
        return self[-1]

    def size(self):
        return len(self)

    def empty(self):
        for i in range(self.size()):
            self.pop()
