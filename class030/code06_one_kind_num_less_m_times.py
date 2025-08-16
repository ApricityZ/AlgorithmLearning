# // 数组中只有1种数出现次数少于m次，其他数都出现了m次
# // 返回出现次数小于m次的那种数
# // 测试链接 : https://leetcode.cn/problems/single-number-ii/
# // 注意 : 测试题目只是通用方法的一个特例，课上讲了更通用的情况
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return self.find(nums, 3)

    def find(self, nums: list[int], m: int) -> int:
        cnts = [0] * 32
        for bit_idx in range(32):
            for num in nums:
                if (num >> bit_idx) & 1:
                    cnts[bit_idx] += 1

        ans = 0
        for i, time in enumerate(cnts):
            if time % m != 0:
                ans |= (1 << i)

        # --- 问题修正 ---
        # LeetCode的题目限制数字是32位有符号整数。
        # 如果ans的第31位是1 (ans >= 2**31)，说明它在32位系统中是一个负数。
        # 需要将其从无符号表示转换为Python中的负数表示。
        if ans >= (1 << 31):
            ans -= (1 << 32)

        return ans
