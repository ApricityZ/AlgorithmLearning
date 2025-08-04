# 归并排序，填函数风格
# 测试链接 : https://leetcode.cn/problems/sort-an-array/

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.arr = nums
        self.n = len(self.arr)
        self.help = [0] * self.n
        self.merge_sort_iter()
        self.merge_sort_r(0, self.n - 1)
        return self.arr

    def merge(self, l, mid, r):
        self.help[l: r + 1] = self.arr[l: r + 1]

        a = l
        b = mid + 1

        for i in range(l, r + 1):
            if a > mid:
                self.arr[i] = self.help[b]
                b += 1
            elif b > r:
                self.arr[i] = self.help[a]
                a += 1
            elif self.help[a] <= self.help[b]:
                self.arr[i] = self.help[a]
                a += 1
            else:
                self.arr[i] = self.help[b]
                b += 1

    def merge_sort_r(self, l, r):
        if l == r:
            return
        mid = (l + r) // 2
        self.merge_sort_r(l, mid)
        self.merge_sort_r(mid + 1, r)
        self.merge(l, mid, r)

    def merge_sort_iter(self):
        if self.n <= 1:
            return
        step = 1
        while step < self.n:
            l = 0
            while l < self.n:
                m = l + step - 1
                if m >= self.n - 1:
                    break
                r = min(m + step, self.n - 1)
                self.merge(l, m, r)
                l = r + 1
            step *= 2
