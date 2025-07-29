from typing import Optional


# // 给你一个链表的头节点 head 和一个特定值 x
# // 请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
# // 你应当 保留 两个分区中每个节点的初始相对位置
# // 测试链接 : https://leetcode.cn/problems/partition-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_head, left_tail = None, None
        right_head, right_tail = None, None
        # 3 4 2 5 6 4 8 x=5
        while head:
            next = head.next
            head.next = None
            if head.val < x:
                if not left_head:
                    left_head = head
                    left_tail = head
                else:
                    left_tail.next = head  # 这一行不要忘记，否则这些节点直接就没有连接起来
                    left_tail = head
            else:
                if not right_head:
                    right_head = head
                    right_tail = head
                else:
                    right_tail.next = head  # 这一行不要忘记，否则这些节点直接就没有连接起来
                    right_tail = head
            head = next

        if not left_head:
            return right_head

        left_tail.next = right_head  # 这里要通过.next来连接，而不是left_tail = right_head
        return left_head  # 这里应该返回left_head，不是left_tail
