from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans, current = None, None
        carry = 0
        while l1 or l2:
            sum = ((l1.val if l1 else 0)
                   + (l2.val if l2 else 0)
                   + carry)
            val = sum % 10
            carry = sum // 10

            if not ans:
                ans = ListNode(val)
                current = ans
            else:
                current.next = ListNode(val)
                current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            current.next = ListNode(1)

        return ans
