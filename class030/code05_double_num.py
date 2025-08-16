# // 数组中有2种数出现了奇数次，其他的数都出现了偶数次
# // 返回这2种出现了奇数次的数
# // 测试链接 : https://leetcode.cn/problems/single-number-iii/
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        eor_all = 0
        eor_half = 0
        for num in nums:
            eor_all ^= num
        last_right_state = eor_all & (-eor_all)
        for num in nums:
            if last_right_state & num == 0:
                eor_half ^= num
        return [eor_half, eor_half ^ eor_all]