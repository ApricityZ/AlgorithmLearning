import numpy as np
from torch.fx.experimental.graph_gradual_typechecker import element_wise_eq


class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Queue1:
    """使用单向链表实现队列"""

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        # 💡 优化建议 (Optimization Suggestion):
        # 虽然 `not self.head` 能正常工作，因为它依赖于 None 的布尔值为 False，
        # 但在Python中，更明确、更推荐的写法是 `self.head is None` 或 `self._size == 0`。
        # 这样能更清晰地表达你的意图：判断头指针是否为 None。
        # return not self.head
        return self._size == 0

    def offer(self, data):
        node = LinkNode(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def poll(self):
        # 💡 优化建议 (Optimization Suggestion):
        # 在数据结构中，当操作失败时（比如从空队列中取元素），
        # 直接打印错误信息并返回 None 是一种不太理想的做法。
        # 更好的方式是抛出一个异常（raise IndexError("poll from an empty queue")），
        # 让调用者自己决定如何处理这个错误。这使得你的类更通用、更灵活。
        if self.is_empty():
            # print('Error, the queue is empty')
            # return None
            raise IndexError("poll from an empty queue")

        node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1

        # 🐛 关键错误 (Critical Bug):
        # 这里缺少一个非常重要的步骤！
        # 想象一下，当队列中只剩最后一个元素时，执行完 `self.head = self.head.next` 后，
        # `self.head` 会变为 None，队列变空。但是，`self.tail` 仍然指向刚刚被移除的那个节点。
        # 这个被移除的节点就成了一个“悬挂指针”或“僵尸节点”。
        # 如果此时你再调用 offer() 添加新元素，程序就会在 `self.tail.next = node` 处尝试
        # 对一个不应该存在的节点进行操作，导致状态混乱。
        #
        # ✅ 修复方案 (The Fix):
        # 在这里需要添加一个检查，如果更新 self.head 后队列变空了，必须同时将 self.tail 也设为 None。
        # if self.head is None:
        #     self.tail = None

        return node

    def peek(self):
        # 💡 优化建议 (Optimization Suggestion):
        # 同 poll() 方法一样，这里也建议在队列为空时抛出异常（raise IndexError），
        # 而不是打印信息并返回 None。
        if self.is_empty():
            raise IndexError('Error, the queue is empty, no peek element')
            # print('Error, the queue is empty, no peek element')
            # return None
        return self.head

    def size(self):
        # ✅ 思考点 (Food for Thought):
        # 这个方法没有错。但在Python中，更地道的做法是实现 `__len__` 这个魔法方法。
        # def __len__(self):
        #     return self._size
        # 这样，你就可以直接使用 `len(queue1)` 来获取队列大小，代码更简洁。
        return self._size

    def __len__(self):
        return self._size

    def display(self):
        # ✅ 思考点 (Food for Thought):
        # 同样，这个方法本身没问题，但可以实现 `__str__` 魔法方法来提供更自然的打印支持。
        # def __str__(self):
        #     # ... 实现返回字符串的逻辑 ...
        # 这样，你可以直接用 `print(queue1)` 来显示队列内容。
        current = self.head
        elements = []
        if self._size > 0:
            while current:
                elements.append(str(current.val))
                current = current.next
            print(f"Queue: {' - '.join(elements)}")
        else:
            print('The queue is empty, no element to dispay')

    def __str__(self):
        current = self.head
        elements = []
        if self._size > 0:
            while current:
                elements.append(str(current.val))
                current = current.next
            return f"Queue: {' - '.join(elements)}"
        else:
            return None


# --- 下面的测试代码本身没有问题，可以正常运行，但它没有触发上面 poll() 方法中的 bug ---
queue1 = Queue1()
queue1.offer(1)
queue1.offer(2)
queue1.offer(3)
queue1.display()
print(queue1)

node = queue1.poll()
print(f"pool node: {node.val}")
queue1.display()

peek_node = queue1.peek()
print(f"peek node: {peek_node.val}")
queue1.display()

# --- 为了触发 poll() 的 bug，我们可以继续操作 ---
print("\n--- Triggering the bug ---")
queue1.poll()  # Polls 2, head becomes node 3, tail is node 3
queue1.poll()  # Polls 3, head becomes None, BUT tail still points to node 3! (BUG!)
print(f"Is queue empty after polling all? {queue1.is_empty()}")  # Will correctly print True
print(f"Head is: {queue1.head}")  # Will be None
print(f"Tail is: {queue1.tail.val if queue1.tail else None}")  # Will still be 3!

print("Offering a new element '4' to the broken queue...")
queue1.offer(4)  # This will not behave as expected. It attaches '4' to the old '3' node.
# The head will be correctly set to '4', but the linkage is broken.
queue1.display()

from typing import Any


class NonCircularQueue:
    """
    一个基于固定长度数组的“非循环队列”实现。

    特性:
    - 队列的容量是固定的。
    - 队尾指针 (r) 到达数组末端后，队列即为“满”，无法再添加新元素。
    - 队首指针 (l) 因出队操作而前进后，其经过的空间将无法被重新利用。

    适用场景:
    - 作为一个一次性的缓冲区 (one-shot buffer)。
    - 当入队操作的总次数确定不超过队列容量时。
    - 用于教学目的，作为学习“循环队列”的前置知识。
    """

    def __init__(self, n: int):
        """
        初始化队列
        :param n: 队列的容量 (capacity)
        """
        self.capacity = n
        self.arr = np.empty(self.capacity, dtype=object)  # 使用 dtype=object 更通用
        self.l = 0
        self.r = 0

    def is_empty(self) -> bool:
        """返回数组是否为空"""
        return self.l == self.r

    def offer(self, val: Any):  # 为 val 添加类型提示
        """
        将新元素添加到队尾。
        如果队尾指针已到达数组末端，则抛出异常。
        """
        if self.r == self.capacity:
            raise IndexError(
                "Queue is full; its underlying array cannot be reused in this non-circular implementation.")
        self.arr[self.r] = val
        self.r += 1

    def poll(self) -> Any:
        """
        从队首取出一个元素。
        注意：此操作会使队首指针前进，被“消耗”的数组空间无法重用。
        """
        if self.is_empty():
            raise IndexError("Error: Cannot poll from an empty queue.")
        val = self.arr[self.l]
        self.l += 1
        return val

    def peek(self) -> Any:
        """查看队首元素，不出队"""
        if self.is_empty():
            raise IndexError("Error: Cannot peek into an empty queue.")
        return self.arr[self.l]

    def __len__(self):
        """返回当前队列中的元素数量"""
        return self.r - self.l

    def __str__(self):
        if self.is_empty():
            return f"NonCircularQueue(capacity={self.capacity}): []"
        elements = ' -> '.join(str(ele) for ele in self.arr[self.l: self.r])
        return f"NonCircularQueue(capacity={self.capacity}): [{elements}]"


# 演示
print('=' * 20)
ncq = NonCircularQueue(3)
print(f"初始状态: {ncq}")
ncq.offer('A')
ncq.offer('B')
print(f"入队后: {ncq}")
ncq.poll()
print(f"出队后: {ncq}")
ncq.offer('C')  # r 指针到达数组末端，已满
print(f"再次入队后: {ncq}")
# ncq.offer('D')
# print(f"最后状态: {ncq}")
try:
    ncq.offer('E')
except IndexError as e:
    # 这个异常是该数据结构设计的预期行为
    print(f"尝试再次入队失败: {e}")

print("=======  python标准库中的队列实现 ========")
import queue

# 创建一个先进先出队列
q = queue.Queue()

# 入队
q.put('a')
q.put('b')
q.put('c')

print(f"当前队列大小: {q.qsize()}")  # 输出: 当前队列大小: 3

# 出队
print(q.get())  # 输出: a
print(q.get())  # 输出: b

print(f"队列是否为空: {q.empty()}")  # 输出: 队列是否为空: False
print(q.get())  # 输出: c
print(f"队列是否为空: {q.empty()}")  # 输出: 队列是否为空: True

print("deque实现队列")
import collections

dq = collections.deque(['a', 'b', 'c'])

dq.append('d')
dq.append('e')

print(f"queue: {dq}")

print(f"出队元素：{dq.popleft()}")
print(f"出队元素： {dq.popleft()}")

print(f"剩余元素：{dq}")

dq1 = collections.deque([1, 2, 3], 2)
print(dq1)

print('=' * 8 + "使用deuqe实现队列" + "=" * 8)
stack = collections.deque()

stack.append(1)
stack.append(2)
print(stack)

print(f"出栈：{stack.pop()}")

print("=" * 8 + "使用列表实现栈" + "=" * 8)


class Stack:
    """
    A stack implementation with a fixed capacity.
    """

    def __init__(self, n: int):
        self.capacity = n
        # Using dtype=object makes the array more flexible for different data types
        self.stack = np.empty(self.capacity, dtype=object)
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        """Helper method to check if the stack is full."""
        return self.size == self.capacity

    def push(self, val):
        """Pushes an element onto the top of the stack."""
        # 修复 (1): 添加栈溢出检查
        if self.is_full():
            raise IndexError("Stack Overflow: Cannot push to a full stack.")
        self.stack[self.size] = val
        self.size += 1

    def pop(self):
        """Pops an element from the top of the stack."""
        # 修复 (2): 添加栈下溢检查
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop from an empty stack.")
        self.size -= 1
        val = self.stack[self.size]
        return val

    def peek(self):
        """Returns the top element of the stack without removing it."""
        # 修复 (2): 添加栈下溢检查
        if self.is_empty():
            raise IndexError("Cannot peek into an empty stack.")
        return self.stack[self.size - 1]

    def __len__(self):
        """
        修复 (3): 使用 __len__ 而不是 __sizeof__ 来返回元素数量.
        这允许我们使用 len(stack_instance).
        """
        return self.size

    def __str__(self):
        """Returns a string representation of the stack."""
        if self.is_empty():
            return "bottom -> [] <- top"
        # 建议: 将 "button" 改为 "bottom"
        elements = ' | '.join(str(ele) for ele in self.stack[:self.size])
        return f"bottom -> [{elements}] <- top"


# --- 演示 ---
print("--- 正常操作 ---")
s1 = Stack(3)
s1.push(1)
s1.push('hello')
s1.push(True)
print(f"栈内容: {s1}")
print(f"栈大小: {len(s1)}")
print(f"栈顶元素: {s1.peek()}")

print("\n--- 溢出和下溢测试 ---")
# 1. 测试栈溢出
try:
    s1.push(99)
except IndexError as e:
    print(f"推送失败: {e}")

# 2. 正常弹出
print(f"弹出: {s1.pop()}")
print(f"弹出后: {s1}")

# 3. 测试栈下溢
s1.pop()
s1.pop()
print(f"全部弹出后: {s1}")
try:
    s1.pop()
except IndexError as e:
    print(f"弹出失败: {e}")

# ====================

print("=" * 8 + "循环队列的实现" + "=" * 8)

# // 设计循环队列
# // 测试链接 : https://leetcode.cn/problems/design-circular-queue/
class CircularQueue:
    def __init__(self, n):
        self.capacity = n
        self.arr = np.empty(self.capacity, dtype=object)
        # self.l = self.r = self.size = 0
        self.l = 0  # 队首 (head) 指针
        self.r = 0  # 队尾 (rear) 指针，指向下一个要插入的位置
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def offer(self, val):
        if self.is_full():
            raise IndexError("The queue is full")
        self.arr[self.r] = val
        self.size += 1
        # self.r = (self.r + 1) if not (self.r == self.capacity - 1) else 0
        # 优化点 1: 使用取模运算更新指针
        self.r = (self.r + 1) % self.capacity

    def poll(self):
        if self.is_empty():
            raise IndexError("The queue is empty")
        val = self.arr[self.l]
        self.size -= 1
        #self.l = 0 if (self.l == self.capacity - 1) else (self.l + 1)
        # 优化点 1: 使用取模运算更新指针
        self.l = (self.l + 1) % self.capacity
        return val

    def peek(self):
        """查看队首元素"""
        if self.is_empty():
            raise IndexError("The queue is empty")
        return self.arr[self.l]

    def rear(self):
        """查看队尾元素"""
        if self.is_empty():
            raise IndexError("The queue is empty")
        #rear_index = (self.capacity - 1) if (self.r == 0) else (self.r - 1)
        # 优化点 2: 使用取模运算计算队尾索引
        rear_index = (self.r - 1 + self.capacity) % self.capacity
        return self.arr[rear_index]

    def __len__(self):
        return self.size

    def __str__(self):
        # if self.is_empty():
        #     return "head -> " + "[]" + " <- rear"
        # if self.l < self.r:
        #     str_queue = " | ".join(self.arr[self.l: self.r])
        # else:
        #     part1 = self.arr[self.l: self.capacity]
        #     part2 = self.arr[0: self.r]
        #     elements = list(part1) + list(part2)
        #     str_queue = " | ".join(str(ele) for ele in elements)
        # return "head -> " + f"[{str_queue}]" + " <- rear"
        # 优化点 3: 简化字符串表示的逻辑
        if self.is_empty():
            return "head -> [] <- rear"

        elements = []
        for i in range(self.size):
            index = (self.l + i) % self.capacity
            elements.append(str(self.arr[index]))

        str_queue = " | ".join(elements)
        return f"head -> [{str_queue}] <- rear"

cir_queue = CircularQueue(3)
cir_queue.offer(1)
cir_queue.offer(2)
cir_queue.poll()
cir_queue.offer(3)
cir_queue.offer(4)
print(cir_queue)
print(cir_queue.is_full())
try:
    cir_queue.offer(5)
except IndexError as e:
    print(f"The queue can't add new entity: {e}")

print(cir_queue.poll())
print(cir_queue)
print(cir_queue.peek())
print(cir_queue.rear())
cir_queue.poll()
cir_queue.poll()
print(cir_queue.is_empty())
print(cir_queue)
try:
    cir_queue.poll()
except IndexError as e:
    print(f"No element in queue: {e}")
