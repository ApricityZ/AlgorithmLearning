from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param lists ListNode类一维数组
# @return ListNode类
#
class MinHeap:
    def __init__(self):
        self._arr: list[None | ListNode] = [None] * 5001
        self._size = 0

    def add(self, node):
        self._arr[self._size] = node
        self._size += 1
        self.heap_insert(self._size - 1)

    def swap(self, a, b):
        tmp = self._arr[a]
        self._arr[a] = self._arr[b]
        self._arr[b] = tmp

    def heap_insert(self, i):
        while (i - 1) // 2 >= 0 and self._arr[i].val < self._arr[(i - 1) // 2].val:
            self.swap(i, (i - 1) // 2)
            i = (i - 1) // 2

    def pop(self)->ListNode:
        node = self._arr[0]
        self.swap(0, self._size - 1)
        self._size -= 1
        self.heapify(0, self._size)
        return node

    def heapify(self, i, size):
        l = 2 * i + 1
        while l < size:
            best = l + 1 if (l + 1) < size and self._arr[l + 1].val < self._arr[l].val else l  # 判断条件别混了，容易笔误
            best = best if self._arr[best].val < self._arr[i].val else i
            if best == i:
                break
            self.swap(i, best)
            i = best
            l = 2 * i + 1

    def is_empty(self):
        return self._size == 0

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_heap = MinHeap()
        for head in lists:
            if head is None:
                continue
            min_heap.add(head)
        if min_heap.is_empty():
            return None

        head = min_heap.pop()
        pre = head

        if pre.next is not None:
            min_heap.add(pre.next)

        while not min_heap.is_empty():
            cur = min_heap.pop()
            pre.next = cur
            pre = cur
            if pre.next is not None:
                min_heap.add(pre.next)

        return head

# [{-5},{-9,-8,-7,-5,1,1,1,3},{-10,-7,-6,-6,-6,0,1,3,3},{-10,-8,-7,-2,3,3},{-1,4},{-5,-4,-1}]
h1 = ListNode(-5)
h2 = ListNode(-9)
h2.next = ListNode(-8)
h2.next.next = ListNode(-7)
h2.next.next.next = ListNode(-5)
h2.next.next.next.next = ListNode(1)

h3 = ListNode(-10)
h3.next = ListNode(-7)
h3.next.next = ListNode(-6)

h4 = ListNode(-10)
h4.next = ListNode(-8)
h4.next.next = ListNode(-7)

h5 = ListNode(-1)
h5.next = ListNode(4)

h6 = ListNode(-5)
h6.next = ListNode(-4)
h6.next.next = ListNode(-1)

input = [h1, h2, h3, h4, h5, h6]
solution = Solution()
ans = solution.mergeKLists(input)