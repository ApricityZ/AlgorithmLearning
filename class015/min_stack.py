import collections
import math


class MinStack1:
    def __init__(self):
        self.data_stack = collections.deque()
        self.min_stack = collections.deque()
        self.size = 0

    def push(self, val):
        self.data_stack.append(val)
        if self.size == 0:
            self.min_stack.append(val)
        else:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])
        self.size += 1

    def pop(self):
        self.min_stack.pop()
        self.size -= 1
        return self.data_stack.pop()

    def top(self):
        return self.data_stack[-1]

    def getMin(self):
        return self.min_stack[-1]


class MinStack:
    def __init__(self):
        self.size = 0
        num = 8001
        self.data_stack = [None] * num
        self.min_stack = [None] * num

    def push(self, val):
        self.data_stack[self.size] = val
        if self.size == 0:
            self.min_stack[self.size] = val
        else:
            if val <= self.min_stack[self.size - 1]:
                self.min_stack[self.size] = val
            else:
                self.min_stack[self.size] = self.min_stack[self.size - 1]

        self.size += 1

    def pop(self):
        self.size -= 1

    def top(self):
        return self.data_stack[self.size - 1]

    def getMin(self):
        return self.min_stack[self.size - 1]


class MinStack2:
    def __init__(self):
        self.data_stack = []
        self.min_stack = [math.inf]

    def push(self, val):
        self.data_stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        self.min_stack.pop()
        return self.data_stack.pop()

    def top(self):
        return self.data_stack[-1]

    def getMin(self):
        return self.min_stack[-1]
