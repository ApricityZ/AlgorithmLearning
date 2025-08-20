# // 返回链表的第一个入环节点
# // 测试链接 : https://leetcode.cn/problems/linked-list-cycle-ii/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is None or head.next is None:  # 这里的特例判断条件不足，我们要保证fast存在，那么呢，还要判断head.next.next 存在与否
        if head is None or head.next is None or head.next.next is None:
            return None

        slow = head.next
        fast = head.next.next

        while slow is not fast:
            if fast.next is None or fast.next.next is None:
                return None
            slow = slow.next
            fast = fast.next.next

        fast = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next

        return slow
