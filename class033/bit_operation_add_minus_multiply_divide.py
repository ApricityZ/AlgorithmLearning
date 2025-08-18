# // 不用任何算术运算，只用位运算实现加减乘除
# // 代码实现中你找不到任何一个算术运算符
# // 测试链接 : https://leetcode.cn/problems/divide-two-integers/

class Solution:
    def __init__(self):
        self._mask = 0xffffffff
        self._min_integer = -2 ** 31
        self._max_integer = 2 ** 31 - 1

    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor == self._min_integer:
            return 1
        if dividend != self._min_integer and divisor == self._min_integer:
            return 0
        if dividend == -1 and divisor == self._min_integer:
            return self._max_integer
        return self.div(self.add(dividend, divisor), divisor) - 1 if divisor > 0 \
            else self.div(self.minus(dividend, divisor), divisor) + 1

    def div(self, a, b):
        # 这个函数适用于a，b均不是32位整数最小值的情况
        a = a if a >= 0 else self.add(~a, 1)
        b = b if b >= 0 else self.add(~b, 1)
        ans = 0
        i = 30
        while i >= 0:
            if (a >> i) >= b:
                ans |= 1 << i
                a = self.minus(a, b << i)
            i = self.minus(i, 1)  # 记得赋值回去
        return self.add(~ans, 1) if (a ^ b) else ans

    def add(self, a, b):
        a &= self._mask
        b &= self._mask
        ans = a
        while b != 0:
            ans = a ^ b
            b = ((a & b) << 1) & self._mask
            a = ans
        return ~(ans ^ self._mask) if (ans >> 31) & 1 else ans

    def minus(self, a, b):
        a &= self._mask
        b &= self._mask
        # return self.add(a, self.add(~b, 1))
        return self.add(a, self.add((b ^ self._mask), 1))
    def multiply(self, a, b):
        ans = 0
        idx = 0
        a &= self._mask
        b &= self._mask
        while idx <= 31:
            if b & 1:
                ans = self.add(ans, a)  # 同样的，记得赋值回ans
            # b >>= 1  # 这里应该是逻辑右移
            b = (b & self._mask) >> 1  # 这样并不能实现
            a = (a << 1) & self._mask
            idx = self.add(idx, 1)  # 记得赋值回idx
        return ~(ans ^ 0xffffffff) if (ans >> 31) & 1 else ans  # 最高位为1应该转换成负数，否则python会按照无限长位正数解释


s = Solution()
print(s.add(1, 2))
print(s.add(-1, 2))
print(s.minus(1, 2))
print(s.multiply(2, -3))
print(s.multiply(-1, 3))
print(s.multiply(-1, -2))
