# 反转对问题，使用分治算法
# 测试连接：https://leetcode.cn/problems/reverse-pairs/
import sys

max_len = 50001
help_arr = [0] * max_len


class Solution:

    def reversePairs(self, nums: list[int]) -> int:
        self.arr: list[int] = nums
        return self._count_reverse_pairs(0, len(self.arr) - 1)

    def _count_reverse_pairs(self, l: int, r: int) -> int:
        if l == r:
            return 0
        mid = (l + r) // 2
        return self._count_reverse_pairs(l, mid) + self._count_reverse_pairs(mid + 1, r) + self.merge(l, mid, r)

    def merge(self, l: int, mid: int, r: int) -> int:
        # 统计部分
        i = l
        j = mid + 1
        ans = 0
        for i in range(l, mid + 1):
            while j <= r and self.arr[i] > 2 * self.arr[j]:
                j += 1
            ans += (j - mid - 1)

        # merge part
        global help_arr
        help_arr[l: r + 1] = self.arr[l: r + 1]
        a = l
        b = mid + 1
        for k in range(l, r + 1):
            if a > mid:
                self.arr[k] = help_arr[b]
                b += 1
            elif b > r:
                self.arr[k] = help_arr[a]
                a += 1
            elif help_arr[a] <= help_arr[b]:
                self.arr[k] = help_arr[a]
                a += 1
            else:
                self.arr[k] = help_arr[b]
                b += 1
        return ans
