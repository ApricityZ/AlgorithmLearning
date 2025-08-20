# // 排序链表
# // 要求时间复杂度O(n*logn)，额外空间复杂度O(1)，还要求稳定性
# // 数组排序做不到，链表排序可以
# // 测试链接 : https://leetcode.cn/problems/sort-list/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        _len = 0
        cur = head
        while cur:
            _len += 1
            cur = cur.next

        # l1: the previous group start; l2: the previous group end
        # l2: the later group start; r2: the later gropu end
        # start: the merged group begin; end: the merged group end
        # merged_last_node: the end of the merged group
        step = 1
        while step < _len:
            # step <<= 1  # 如果循环遍历会在循环中使用，需要注意循环遍历先赋值是否会影响正常的逻辑，比如这里我们要用step=1，2，4，就不能先乘2

            l1 = head
            r1 = self.find_end_node(l1, step)
            l2 = r1.next
            # if l2 is None:  # 考虑[1,2]在step=2时的情况，l2为空  ----- 这里是不需要的
            #     step <<= 1
            #     continue
            # 代码的核心循环是 for (int step = 1; step < n; step <<= 1)。
            # 这意味着，只要程序能进入这个循环，step 的值就严格小于链表的总长度 n。
            r2 = self.find_end_node(l2, step)
            next_node = r2.next
            r1.next = None
            r2.next = None
            begin, end = self.merge(l1, r1, l2, r2)
            head = begin
            merged_last_node = end
            while next_node:
                l1 = next_node
                r1 = self.find_end_node(l1, step)
                l2 = r1.next
                if l2 is None:
                    merged_last_node.next = l1
                    break
                r2 = self.find_end_node(l2, step)
                next_node = r2.next
                r1.next = None  # 待排序的分组要将末尾切断，否则merge过程中链表越来越长
                r2.next = None  # 同上
                # next_node = r2.next  # 顺序错误，应该放在r2.next置空之前，现在这里切断了next node
                begin, end = self.merge(l1, r1, l2, r2)
                merged_last_node.next = begin
                merged_last_node = end
            step <<= 1

        return head

    def find_end_node(self, start: Optional[ListNode], step):
        # for _ in range(1, step):  要注意可能剩余的节点不足step长度
        #     start = start.next
        i = 0
        while start.next and i < step - 1:
            start = start.next
            i += 1
        return start

    def merge(self, l1: Optional[ListNode], r1, l2: Optional[ListNode], r2, begin=None, end=None):
        if l1.val <= l2.val:
            begin = l1
            pre = l1
            l1 = l1.next
        else:
            begin = l2
            pre = l2
            l2 = l2.next

        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                pre = l1
                l1 = l1.next
            else:
                pre.next = l2
                pre = l2
                l2 = l2.next

        if l1:
            pre.next = l1
            end = r1
        if l2:
            pre.next = l2
            end = r2

        return begin, end
