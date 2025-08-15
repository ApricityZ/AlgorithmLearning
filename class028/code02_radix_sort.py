# // 基数排序
# // 测试链接 : https://leetcode.cn/problems/sort-an-array/
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self._arr = nums
        self._len = len(self._arr)
        self.base = 10
        self.counts_arr = [0] * self.base  # 这里计数数量是base数量
        self.help_arr = [0] * self._len
        self.sort()
        return self._arr

    def sort(self):
        min_val = self._arr[0]
        for num in self._arr:
            min_val = min(min_val, num)

        max_val = self._arr[0]
        for i in range(self._len):
            self._arr[i] = self._arr[i] - min_val
            max_val = max(max_val, self._arr[i])  # 名字类似的变量要注意，这里将max_val写成了min_val

        # 获取位长度
        len_bit = self.bit_len(max_val)

        # 基数排序
        self.radix_sort(len_bit)

        # 复原数组
        for i in range(self._len):
            self._arr[i] += min_val

    def radix_sort(self, len_bit):
        offset = 1
        # for i in range(self._len):  # 位置放错了，应该放在循环内部啊！！！！！！ 并且应该是self.base而不是len
        #     self.counts_arr[i] = 0
        while len_bit > 0:
            for i in range(self.base):
                self.counts_arr[i] = 0

            for i in range(self._len):
                self.counts_arr[(self._arr[i] // offset) % self.base] += 1

            for i in range(1, self.base):
                self.counts_arr[i] += self.counts_arr[i - 1]

            for i in reversed(range(self._len)):  # 为了保持相对次序有序，应该从右往左遍历
                cnt_index = (self._arr[i] // offset) % self.base
                self.help_arr[self.counts_arr[cnt_index] - 1] = self._arr[i]
                self.counts_arr[cnt_index] -= 1

            self._arr[0:self._len] = self.help_arr[:]

            offset *= self.base  # 这里偏移量改变不要忘记了
            len_bit -= 1  # 这里使用while的话，要自己控制循环变量的变化

    def bit_len(self, val):
        bit_len = 0
        while val > 0:
            bit_len += 1
            val //= self.base
        return bit_len

if __name__ == '__main__':
    s = Solution()
    s.sortArray([-1, 2, -8, -10])
