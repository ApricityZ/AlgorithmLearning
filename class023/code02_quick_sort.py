# // 随机快速排序，填函数练习风格
# // 测试链接 : https://leetcode.cn/problems/sort-an-array/
import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.arr = nums
        self.n = len(self.arr)
        self.quick_sort2(0, self.n - 1)
        return self.arr

    def swap(self, a: int, b: int) -> None:
        tmp = self.arr[a]
        self.arr[a] = self.arr[b]
        self.arr[b] = tmp

    def partition1(self, l: int, r: int, x: int) -> int:
        a = l
        xi = 0
        for i in range(l, r + 1):
            if self.arr[i] <= x:
                self.swap(i, a)
                if self.arr[a] == x:
                    xi = a
                a += 1
        self.swap(xi, a - 1)
        return a - 1

    def quick_sort(self, l: int, r: int) -> None:
        if l >= r:
            return
        # x = random.choice(self.arr[l: r + 1])
        x = self.arr[random.randint(l, r)]
        mid = self.partition1(l, r, x)
        self.quick_sort(l, mid - 1)
        self.quick_sort(mid + 1, r)

    def partition2(self, l: int, r: int, x: int) -> tuple[int, int]:
        a = l
        b = r
        i = l
        while i <= b:
            if self.arr[i] < x:
                self.swap(a, i)
                i += 1
                a += 1
            elif self.arr[i] == x:
                i += 1
            else:
                self.swap(b, i)
                b -= 1
        return a, b

    def quick_sort2(self, l: int, r: int) -> None:
        if l >= r:
            return
        x = random.choice(self.arr[l: r + 1])
        first, last = self.partition2(l, r, x)
        self.quick_sort2(l, first - 1)
        self.quick_sort2(last + 1, r)
