# // 每k个节点一组翻转链表
# // 测试链接：https://leetcode.cn/problems/reverse-nodes-in-k-group/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # start: group start node; end: group end node; last_group_end: the reversed previous group end node
        # head: head node of whole linkedlist
        start = head
        end = self.group_end_node(start, k)
        if end is None:
            return start

        head = end
        self.reverse(start, end)

        last_group_end = start
        while last_group_end.next:
            start = last_group_end.next
            end = self.group_end_node(start, k)
            if end is None:
                return head

            self.reverse(start, end)
            last_group_end.next = end  # 如果这一组进行了reverse，那么上一组的reversed后的尾节点 last_group_end需要指向这一组的end节点，原来是指向start节点的
            last_group_end = start

        return head

    def group_end_node(self, start_node, k):
        while start_node is not None and k - 1 > 0:
            start_node = start_node.next
            k -= 1
        return start_node

    def reverse(self, start, end):
        end = end.next
        pre, next_node = None, None
        cur = start  # 需要一个指针指向当前处理的节点，不是一直更新start
        while cur is not end:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        start.next = end  # 这里也很关键，不可忽视   开头指向原链表end节点的下一个节点，即下一组的start节点
