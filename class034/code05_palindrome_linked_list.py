# // 判断链表是否是回文结构
# // 测试链接 : https://leetcode.cn/problems/palindrome-linked-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # if head is None:  # 如果为空或者只有一个节点，也是为回文数
        #     return False
        if head is None or head.next is None:
            return True

        slow, fast = head, head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # 现在slow指向中点位置
        # 将slow后面的节点反转
        pre = slow
        cur = slow.next
        slow.next = None
        next_node = None
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node

        # l -> ... -> slow <- ... <- r
        #             slow -> None
        # 位置已经调整好，开始遍历左右开始对比

        l = head
        # r = fast  # 最右边的节点r其实是上边的pre节点
        # while r.next:  # 这里有问题，fast指向的节点的指向已经不是原来的链表了，r无法到达原链表的最右侧
        #     r = r.next
        r = pre

        ans = True
        while l:
            if l.val != r.val:
                ans = False
            l = l.next
            r = r.next

        # 不要忘记复原原链表
        cur = pre
        pre = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next_node

        return ans
