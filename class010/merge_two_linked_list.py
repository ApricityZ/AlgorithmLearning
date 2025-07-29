# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


class Solution:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            return list1 if list1 is not None else list2  # 如果存在空链表，那么应当返回另一个链表作为head，否则空＋非空的组合结果错误

        head = list1 if list1.val <= list2.val else list2
        current1 = head.next
        current2 = list2 if head == list1 else list1
        pre = head
        while current1 and current2:
            if current1.val <= current2.val:
                pre.next = current1
                current1 = current1.next
            else:
                pre.next = current2
                current2 = current2.next
            pre = pre.next  # pre要定位串好的链表的最后一个，准备连接下一个节点

        pre.next = current2 if current1 is None else current1
        return head

    def mergeTwoLists_recursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 基本情况：如果 list1 或 list2 为空，直接返回非空的那个链表
        if not list1:
            return list2
        if not list2:
            return list1

        # 递归步骤：比较两个链表的头节点
        if list1.val <= list2.val:
            # list1 的头节点更小，它就是新链表的头
            # 它的 next 指针指向 list1.next 和 list2 合并后的结果
            list1.next = self.mergeTwoLists_recursive(list1.next, list2)
            return list1
        else:
            # list2 的头节点更小，它就是新链表的头
            # 它的 next 指针指向 list1 和 list2.next 合并后的结果
            list2.next = self.mergeTwoLists_recursive(list1, list2.next)
            return list2

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建虚拟头节点
        # 这样可以避免空链表判断，并减少额外的变量引入，真的优雅
        dummy = ListNode(0)
        current = dummy

        # 比较两个链表的节点值，依次连接较小的节点
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # 连接剩余节点
        current.next = list1 or list2

        # 返回合并后的链表
        return dummy.next

# 这一行代码 current.next = list1 or list2 确实是 Pythonic 写法中的一个绝佳典范，充分展现了语言的简洁之美。
#
# 它之所以优雅，核心在于巧妙地利用了 Python 中 or 运算符的短路求值（Short-circuit evaluation）和返回值特性。
#
# 深入解析 or 运算符
# 在很多语言中，逻辑运算符（如 or, and）返回的是布尔值 True 或 False。但在 Python 中，它们返回的是决定了整个表达式结果的那个对象本身。
#
# 对于 A or B 这个表达式：
#
# Python 会先评估 A。
#
# 如果 A 是一个“真值”（Truthy），or 表达式的结果就已经确定为真了，Python 会立即停止计算（即“短路”），并直接返回 A 的值。
#
# 如果 A 是一个“假值”（Falsy），Python 才会继续评估 B，并返回 B 的值（无论 B 是真是假）。
#
# 什么是“真值”和“假值”？
#
# 假值 (Falsy): None, False, 0 (所有数值零), [] (空列表), {} (空字典), () (空元组), "" (空字符串) 等。
#
# 真值 (Truthy): 除了上述假值以外的所有其他对象，包括非空的对象实例（比如我们的 ListNode 节点）。
#
# 应用于链表合并的场景
# 当 while list1 and list2: 循环结束时，必然意味着 list1 和 list2 中至少有一个已经变成了 None。这时会出现三种情况：
#
# list1 耗尽，list2 还有剩余节点：
#
# 此时 list1 是 None (Falsy)。
#
# 表达式为 None or list2。
#
# Python 评估 None，发现是假值，于是继续评估 list2。
#
# list2 是一个 ListNode 对象 (Truthy)，所以表达式返回 list2 对象本身。
#
# current.next = list2，完美地将 list2 的剩余部分连接到合并链表的末尾。
#
# list2 耗尽，list1 还有剩余节点：
#
# 此时 list1 是一个 ListNode 对象 (Truthy)。
#
# 表达式为 list1 or list2。
#
# Python 评估 list1，发现是真值，触发短路机制。
#
# 表达式直接返回 list1 对象本身。
#
# current.next = list1，同样完美地连接了 list1 的剩余部分。
#
# list1 和 list2 同时耗尽（原链表都为None，传入的两个head都为None）：
#
# 此时 list1 是 None，list2 也是 None。
#
# 表达式为 None or None。
#
# Python 评估第一个 None，是假值；继续评估第二个 None。
#
# 最终返回第二个 None。
#
# current.next = None，正确地为合并链表设置了结尾。
