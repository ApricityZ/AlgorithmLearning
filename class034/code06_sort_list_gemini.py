# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 1. 计算链表长度
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # 2. 创建虚拟头节点，简化后续操作
        dummy = ListNode(0, head)

        step = 1
        while step < length:
            # tail 指向已排序部分的尾部，current 指向待处理部分的头部
            tail, current = dummy, dummy.next

            while current:
                # 3. 从 current 开始，分割出第一个子链表 l1
                l1 = current
                # split 函数会切断链表，并返回下一段的开头
                next_sublist = self.split(l1, step)

                # 4. 从 next_sublist 开始，分割出第二个子链表 l2
                l2 = next_sublist
                if l2:
                    # current 更新为再下一段的开头，用于下一次大循环
                    current = self.split(l2, step)
                else:
                    # 如果没有 l2，说明 l1 是最后剩下的部分，无需合并
                    current = None

                # 5. 合并 l1 和 l2
                merged_head, merged_tail = self.merge(l1, l2)

                # 6. 将合并后的结果连接到已排序部分的末尾
                tail.next = merged_head
                tail = merged_tail  # 更新 tail 到新的末尾

            # 步长翻倍，进入下一轮归并
            step *= 2

        return dummy.next

    def split(self, node: Optional[ListNode], size: int) -> Optional[ListNode]:
        """
        从 node 开始，前进 size-1 步找到子链表的结尾。
        然后切断链表，并返回下一段的开头。
        """
        if not node:
            return None

        for _ in range(size - 1):
            if not node.next:
                break
            node = node.next

        # 找到下一段的开头
        next_start = node.next
        # 切断链表
        node.next = None
        return next_start

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
        """
        合并两个已排序的链表，并返回新链表的头和尾。
        """
        if not l1: return l2, l2  # 如果 l1 为空，直接返回 l2
        if not l2: return l1, self.get_tail(l1)  # 如果 l2 为空，返回 l1 及其尾部

        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # 连接剩余的部分
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        # 找到并返回新的尾部
        while tail.next:
            tail = tail.next

        return dummy.next, tail

    def get_tail(self, node: Optional[ListNode]) -> Optional[ListNode]:
        """一个简单的辅助函数，用于找到链表的尾节点"""
        if not node:
            return None
        while node.next:
            node = node.next
        return node
