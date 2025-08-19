# // 复制带随机指针的链表
# // 测试链接 : https://leetcode.cn/problems/copy-list-with-random-pointer/
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        # a   b   c   d   e   None
        # cur
        cur = head
        while cur:
            next_node = cur.next
            cur.next = Node(cur.val, next_node)
            cur = next_node  # cur应该跳到原链表的next节点

        cur = head
        while cur:
            next_node = cur.next.next
            copy = cur.next
            # copy.next = cur.random.next if cur.random else None
            # 这部分代码有 致命错误。它本应设置 copy.random，但却错误地修改了 copy.next。
            #
            # copy.next 本来应该指向下一个原始节点（例如，A' 的 next 应该指向 B），这是维持整个交错链表结构的关键。修改它会破坏这个结构，甚至可能 创建出一个环。
            copy.random = cur.random.next if cur.random else None
            cur = next_node

        ans = head.next
        cur = head
        while cur:
            next_node = cur.next.next
            copy = cur.next
            cur.next = next_node
            copy.next = next_node.next if next_node else None
            cur = next_node

        return ans
# 举例说明
# 假设原始链表是 A -> B -> null，并且 B.random = A。
#
# 第一步后：链表结构为 A -> A' -> B -> B' -> null。
#
# 第二步（错误操作）：
#
# 当处理到节点 B 时，cur 是 B，copy 是 B'。
#
# 代码执行 copy.next = cur.random.next，即 B'.next = B.random.next。
#
# 因为 B.random 是 A，所以 B.random.next 就是 A'。
#
# 于是，B'.next 就指向了 A'，形成了一个 A' -> B' -> A' 的环。
#
# 第三步：当 cur 指针在遍历过程中进入这个 A' -> B' 的环时，它将永远无法退出，while cur: 条件永远为真，程序卡死。
