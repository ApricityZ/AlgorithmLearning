# Definition for singly-linked list.
# // 返回两个无环链表相交的第一个节点
# // 测试链接 : https://leetcode.cn/problems/intersection-of-two-linked-lists/


from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if (headA is None) or (headB is None):
            return None

        diff = 0
        # a = None  # 这里a应该赋值位headA
        a = headA
        # while headA.next is not None:  # 对应这里应该是a.next, 循环变量一定是在变化的才能让循环终止
        while a.next is not None:
            # a = headA.next  # 这里应该是自循环
            a = a.next
            diff += 1

        # b = None  # 同上
        # while headB.next is not None:  # 同上
        b = headB
        while b.next is not None:
            # b = headB.next  # 同上
            b = b.next
            diff -= 1

        if a is not b:
            return None

        if diff >= 0:
            a = headA
            b = headB
        else:
            a = headB
            b = headA

        for _ in range(abs(diff)):
            a = a.next

        while a is not b:
            a = a.next
            b = b.next

        return a
