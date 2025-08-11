from typing import List


# // 将数组和减半的最少操作次数
# // 测试链接 : https://leetcode.cn/problems/minimum-operations-to-halve-array-sum/

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        self._arr: List[int] = nums
        self._size = len(nums)
        sum = 0
        for i in reversed(range(self._size)):
            sum += self._arr[i]  # 这里求加和应当 放在heapify 之前，因为heapify会直接改变arr元素的位置，导致求和错误❌
            self.heapify(i, self._size)

        dec = 0
        count = 0
        while dec < sum / 2:
            self._arr[0] /= 2
            dec += self._arr[0]
            self.heapify(0, self._size)
            count += 1
        return count

    def heapify(self, i, size):
        l = 2 * i + 1
        while l < size:
            best = l + 1 if l + 1 < size and self._arr[l + 1] > self._arr[l] else l
            best = best if self._arr[best] > self._arr[i] else i
            if best == i:
                break
            self.swap(i, best)
            i = best
            l = 2 * i + 1

    def swap(self, a, b):
        tmp = self._arr[a]
        self._arr[a] = self._arr[b]
        self._arr[b] = tmp
