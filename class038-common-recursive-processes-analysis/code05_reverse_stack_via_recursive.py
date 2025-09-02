# // 用递归函数逆序栈
from queue import LifoQueue


class ReverseStack:
    def reverse(self, stack: LifoQueue[int]):
        # if stack is None:
        if stack.qsize() == 0:
            return
        num = self.button_out(stack)
        self.reverse(stack)
        stack.put(num)

    def button_out(self, stack: LifoQueue[int]) -> int:
        ans = stack.get()
        # if stack is None:
        if stack.qsize() == 0:
            return ans

        last = self.button_out(stack)
        stack.put(ans)
        return last

stack = LifoQueue()
stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)
stack.put(5)
print("origin stack " + str(stack.queue))
rs = ReverseStack()
rs.reverse(stack)
print("reversed stack " + str(stack.queue))