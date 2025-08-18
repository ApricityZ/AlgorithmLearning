# // 给你两个整数 left 和 right ，表示区间 [left, right]
# // 返回此区间内所有数字 & 的结果
# // 包含 left 、right 端点
# // 测试链接 : https://leetcode.cn/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:  # 注意这里是 > 不是 <
            right &= (right - 1)
            # right &= ~(right & (-right))
        return right


s = Solution().rangeBitwiseAnd(4, 7)
print(s)
