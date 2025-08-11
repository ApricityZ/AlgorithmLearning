# // 堆结构和堆排序，填函数练习风格
# // 测试链接 : https://leetcode.cn/problems/sort-an-array/
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.arr = nums
        self.size = len(self.arr)
        self.heapsort1()
        self.heapsort2()
        return self.arr

    def swap(self, a, b):
        tmp = self.arr[a]
        self.arr[a] = self.arr[b]
        self.arr[b] = tmp

    def heap_insert(self, i):
        while (i - 1) // 2 >= 0 and (self.arr[i] > self.arr[(i - 1) // 2]):
            self.swap(i, (i - 1) // 2)
            i = (i - 1) // 2

    def heapify(self, i, size):
        l = 2 * i + 1
        while l < size:
            # best = (l + 1) if ((l + 1) < self.size) and (self.arr[l + 1] > self.arr[l]) else l
            best = (l + 1) if ((l + 1) < size) and (self.arr[l + 1] > self.arr[l]) else l
            best = i if self.arr[best] <= self.arr[i] else best
            if best == i:
                break
            self.swap(best, i)
            i = best
            l = 2 * i + 1

    def heapsort1(self):
        for i in range(self.size):
            self.heap_insert(i)

        size = self.size
        while size > 0:
            size -= 1
            self.swap(0, size)
            self.heapify(0, size)

    def heapsort2(self):
        for i in reversed(range(self.size)):
            self.heapify(i, self.size)

        size = self.size
        while size > 0:
            size -= 1
            self.swap(0, size)
            self.heapify(0, size)
