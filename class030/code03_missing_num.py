# // 找到缺失的数字
# // 测试链接 : https://leetcode.cn/problems/missing-number/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        eor_idx = 0
        eor_arr = 0
        for i, num in enumerate(nums):
            eor_idx ^= i
            eor_arr ^= num
        eor_idx ^= len(nums)
        return eor_idx ^ eor_arr
