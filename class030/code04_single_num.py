# // 数组中1种数出现了奇数次，其他的数都出现了偶数次
# // 返回出现了奇数次的数
# // 测试链接 : https://leetcode.cn/problems/single-number/
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        eor = 0
        for num in nums:
            eor ^= num
        return eor