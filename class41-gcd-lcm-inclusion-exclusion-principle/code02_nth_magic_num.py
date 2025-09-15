# // 一个正整数如果能被 a 或 b 整除，那么它是神奇的。
# // 给定三个整数 n , a , b ，返回第 n 个神奇的数字。
# // 因为答案可能很大，所以返回答案 对 1000000007 取模
# // 测试链接 : https://leetcode.cn/problems/nth-magical-number/

# 一个正整数如果能被 a 或 b 整除，那么它是神奇的。
#
# 给定三个整数 n , a , b ，返回第 n 个神奇的数字。因为答案可能很大，所以返回答案 对 109 + 7 取模 后的值。

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lcm = self.lcm(a, b)
        l = 0
        r = n * min(a, b)
        ans = 0
        # 使用二分法，注意边界条件，返回时其实 ans = l，但是r应该是要 小于 ans的
        while l <= r:  # 等于的时候应该可以进入，否则 m 无法取到 l = r 时候的值
            m = l + (r - l) // 2
            if m / a + m / b - m / lcm >= n:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans % 1000000007  # 不要忘记题目结果要求取模

    def gcd(self, a, b) -> int:
        return a if b == 0 else self.gcd(b, a % b)

    def lcm(self, a, b):
        return (a / self.gcd(a, b)) * b


print(Solution().nthMagicalNumber(1, 2, 3))
