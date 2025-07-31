import collections


class Queue:
    def __init__(self, k):
        self.capacity = k
        self.arr = [None] * self.capacity
        self.l = 0
        self.r = 0

    def is_empty(self):
        return self.l == self.r

    def if_full(self):
        return self.r == self.capacity

    def push(self, val):
        if self.if_full():
            raise IndexError("The queue is full, can't push new element")
        self.arr[self.r] = val
        self.r += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("The queue is empty, no element to poll")
        val = self.arr[self.l]
        self.l += 1
        return val


    def peek(self):
        if self.is_empty():
            raise IndexError("The queue is empty, no peek element")


class Stack:
    def __init__(self, k):
        self.capacity = k
        self.size = 0
        self.arr = [None] * self.capacity

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.capacity

    def push(self, val):
        if self.full():
            raise IndexError("The stack is full")
        self.arr[self.size] = val
        self.size += 1

    def pop(self):
        if self.empty():
            raise IndexError("The stack is empty")
        val = self.arr[self.size - 1]
        self.size -= 1
        return val


class MyQueue:
    def __init__(self):
        self.in_stack = collections.deque()
        self.out_stack = collections.deque()

    def in_stack2out_stack(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def push(self, x):
        self.in_stack.append(x)
        self.in_stack2out_stack()

    def pop(self):
        self.in_stack2out_stack()
        return self.out_stack.pop()

    def peek(self):
        self.in_stack2out_stack()
        val = self.out_stack.pop()
        self.out_stack.append(val)
        return val

    def empty(self):
        if self.in_stack or self.out_stack:
            return False
        else:
            return True

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()



class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))  # 这里因为上一步循环已经改变了相对位置，我们想要的是把第一个放在最后，应该保持使用索引0

    def pop(self) -> int:
        return self.queue.pop(0)

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not len(self.queue)

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
# param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()