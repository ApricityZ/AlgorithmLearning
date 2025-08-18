# // 不用任何算术运算，只用位运算实现加减乘除
# // 代码实现中你找不到任何一个算术运算符
# // 测试链接 : https://leetcode.cn/problems/divide-two-integers/
# 最终的黄金法则
# 您可以将我们的整个对话浓缩为这条黄金法则：
#
# 当用 Python 模拟定长整数运算时，你必须主动、持续地通过 & mask 操作来“丢弃”那些在定长世界中本应丢失的信息。这是从 Python 的“无限”数学世界，通往“有限”硬件世界的唯一路径，也是保证算法正确性的不二法门。

class Solution:
    def __init__(self):
        # 完全使用位运算来定义常量
        self._mask = (~0) ^ ((~0) << 32)  # 0xFFFFFFFF, 32位掩码
        # MIN_VALUE: 100...00 (32位), 即符号位为1, 其余为0
        self._min_integer = 1 << 31
        # MAX_VALUE: 011...11 (32位), 即对MIN_VALUE取反
        # self._max_integer = ~self._min_integer
        # MAX_VALUE: 011...11 (32位).
        # 正确的【32位取反】操作是与32位掩码进行异或
        self._max_integer = self._min_integer ^ self._mask

    # ===================================================================
    # 辅助函数 (internal helpers)
    # 这些函数接收Python整数，但将它们当作32位模式处理,
    # 并且返回的也是代表结果的32位模式 (一个0到mask之间的Python正整数)
    # ===================================================================

    def _add(self, a, b):
        """核心加法器：返回 a+b 的32位模式"""
        a &= self._mask
        b &= self._mask
        while b != 0:
            # 异或：无进位加法
            sum_val = (a ^ b) & self._mask
            # 与后左移：计算进位
            b = ((a & b) << 1) & self._mask
            a = sum_val
        return a

    def _neg(self, n):
        """核心取反器：返回 -n 的32位模式"""
        # 一个数的相反数的补码等于对这个数取反再加一
        return self._add(~n, 1)

    def _minus(self, a, b):
        """核心减法器：返回 a-b 的32位模式"""
        return self._add(a, self._neg(b))

    def _multiply(self, a, b):
        """核心乘法器：返回 a*b 的32位模式"""
        a &= self._mask
        b &= self._mask
        ans = 0
        while b != 0:
            if b & 1:
                ans = self._add(ans, a)
            a = (a << 1) & self._mask
            # 因为b已经被mask成正数, >>就是无符号右移
            b >>= 1
        return ans

    # def _div(self, a, b):
    #     """核心除法器：只处理正数，返回 a/b 的32位模式"""
    #     a &= self._mask
    #     b &= self._mask
    #     ans = 0
    #     # 从最高位开始尝试减去除数
    #     for i in range(30, -1, -1):
    #         # 判断 a 是否大于等于 (b << i)
    #         # a >> i >= b  等价于 a >= (b << i)
    #         # 我们用 a - (b << i) >= 0 来判断
    #         # 一个数 x >= 0 等价于其符号位为0, 即 (x >> 31) & 1 == 0
    #         shifted_b = (b << i) & self._mask
    #         if not ((self._minus(a, shifted_b) >> 31) & 1):
    #             ans |= (1 << i)
    #             a = self._minus(a, shifted_b)
    #     return ans
    def _div(self, a, b):
        """核心除法器：只处理正数，返回 a/b 的32位模式"""
        a &= self._mask
        b &= self._mask
        ans = 0
        # 从最高位开始尝试减去除数
        for i in range(30, -1, -1):
            # 【采纳您的建议进行优化】
            # 判断 a 是否大于等于 (b << i)，我们使用更稳健的 a >> i >= b
            # 一个数 x >= y 等价于 x - y >= 0
            # 一个数 z >= 0 等价于其符号位为0, 即 (z >> 31) & 1 == 0

            # 1. 先计算 a >> i
            a_shifted = a >> i

            # 2. 再判断 a_shifted 是否大于等于 b
            if not ((self._minus(a_shifted, b) >> 31) & 1):
                # 如果条件成立，说明 a 至少包含一个 (b << i)
                ans |= (1 << i)
                # a 减去这个 (b << i)
                a = self._minus(a, (b << i) & self._mask)
        return ans

    # ===================================================================
    # 公共接口 (public APIs)
    # 这些函数调用辅助函数，并负责将最终的32位模式结果
    # 转换回标准的Python带符号整数 (正数或负数)
    # ===================================================================

    def _to_signed_int(self, n):
        """将32位模式转换为Python的带符号整数"""
        n &= self._mask
        # 如果最高位(第31位)是1, 说明是负数
        if (n >> 31) & 1:
            # 用 n - 2^32 将其“环绕”到负数域
            return n - (1 << 32)
        return n

    def add(self, a, b):
        res = self._add(a, b)
        return self._to_signed_int(res)

    def minus(self, a, b):
        res = self._minus(a, b)
        return self._to_signed_int(res)

    def multiply(self, a, b):
        res = self._multiply(a, b)
        return self._to_signed_int(res)

    # def divide(self, dividend: int, divisor: int) -> int:
    #     # 1. 处理所有边界情况
    #     if divisor == 0:
    #         # LeetCode上未定义除以0的行为，通常会抛出异常
    #         raise ZeroDivisionError("division by zero")
    #     if dividend == self._min_integer and divisor == -1:
    #         return self._max_integer
    #     if divisor == self._min_integer:
    #         return 1 if dividend == self._min_integer else 0
    #     if dividend == self._min_integer:
    #         # a是最小值, b不是-1也不是最小值
    #         # (a+1)/b - (a-(a+1))/b
    #         # 这里需要非常技巧性的处理来防止溢出
    #         # a/b = (a+1)/b + (a-(a+1))/b / b
    #         res = self._div(self._add(dividend,1), divisor)
    #         offset = self._div(self._minus(dividend, self._add(dividend,1)), divisor)
    #         return self._to_signed_int(self._add(res, offset))
    #
    #     # 2. 正常情况：先确定符号，再在正数上做除法
    #     # 判断符号是否相同: a < 0 和 b < 0 的结果是否一致
    #     # (a >> 31) == (b >> 31)
    #     same_sign = not (((dividend >> 31) & 1) ^ ((divisor >> 31) & 1))
    #
    #     # 转换为正数进行计算
    #     pos_dividend = self._neg(dividend) if ((dividend >> 31) & 1) else dividend
    #     pos_divisor = self._neg(divisor) if ((divisor >> 31) & 1) else divisor
    #
    #     ans = self._div(pos_dividend, pos_divisor)
    #
    #     return self._neg(ans) if not same_sign else ans

    # def divide(self, dividend: int, divisor: int) -> int:
    #     # 1. 处理最极端的边界情况
    #     if divisor == 0:
    #         raise ZeroDivisionError("division by zero")
    #     if dividend == 0:
    #         return 0
    #     if divisor == self._min_integer:
    #         return 1 if dividend == self._min_integer else 0
    #     # MIN_INTEGER / -1 是唯一会溢出的情况
    #     if dividend == self._min_integer and divisor == -1:
    #         return self._max_integer
    #
    #     # 2. 处理被除数是 MIN_INTEGER 的一般情况
    #     # 此时除数不是0, MIN_INTEGER, 或 -1
    #     # 我们不能直接对 dividend 取反，因为它会溢出。
    #     # 这里使用一个技巧: a/b = (a+1)/b (向下取整)
    #     # 这样可以将问题转化为一个不会溢出的数的除法
    #     if dividend == self._min_integer:
    #         # 先计算 (dividend + 1) / divisor
    #         res = self.divide(self._to_signed_int(self._add(dividend, 1)), divisor)
    #         # 再计算余数部分的除法 (dividend - (dividend+1)*divisor) / divisor
    #         # a - (a+1) = -1.  c = a - b*q
    #         # remainder_part = dividend - res * divisor = -1
    #         # a = q*b+r -> (a-r)/b = q
    #         # 我们需要计算 (dividend - (res*divisor)) / divisor
    #         # a - bq = r
    #         correction = self.divide(self.minus(dividend, self.multiply(res, divisor)), divisor)
    #         return self.add(res, correction)
    #
    #     # 3. 所有其他正常情况
    #     # 确定最终结果的符号
    #     # a和b的符号位不同，则结果为负
    #     is_negative = ((dividend >> 31) & 1) ^ ((divisor >> 31) & 1)
    #
    #     # 将被除数和除数都转为正数进行计算
    #     pos_dividend = self._neg(dividend) if ((dividend >> 31) & 1) else dividend
    #     pos_divisor = self._neg(divisor) if ((divisor >> 31) & 1) else divisor
    #
    #     # 调用核心除法器
    #     ans_pattern = self._div(pos_dividend, pos_divisor)
    #
    #     # 根据之前确定的符号，决定是否对结果取反
    #     result_pattern = self._neg(ans_pattern) if is_negative else ans_pattern
    #
    #     # 【关键修复】: 对最终的位模式进行转换后再返回
    #     return self._to_signed_int(result_pattern)
    def divide(self, dividend: int, divisor: int) -> int:
        # 1. 处理最极端的边界情况
        if divisor == 0:
            raise ZeroDivisionError("division by zero")
        if dividend == 0:
            return 0

        # 【关键修正】: 比较时，将被除数和除数都转换为32位模式
        dividend_pattern = dividend & self._mask

        divisor_pattern = divisor & self._mask

        if divisor_pattern == self._min_integer:
            return 1 if dividend_pattern == self._min_integer else 0

        # MIN_INTEGER / -1 是唯一会溢出的情况
        if dividend_pattern == self._min_integer and divisor == -1:
            return self._max_integer

        # 2. 处理被除数是 MIN_INTEGER 的一般情况
        if dividend_pattern == self._min_integer:
            # 此时除数不是0, MIN_INTEGER, 或 -1
            # 使用递归技巧: a/b = (a+1)/b + (a-(a+1)*q)/b
            # 这可以将问题分解为两个更小的、不会溢出的数的除法
            res = self.divide(self._to_signed_int(self._add(dividend, 1)), divisor)
            correction = self.divide(self.minus(dividend, self.multiply(res, divisor)), divisor)
            return self.add(res, correction)

        # 3. 所有其他正常情况
        # 确定最终结果的符号
        is_negative = ((dividend >> 31) & 1) ^ ((divisor >> 31) & 1)

        # 将被除数和除数都转为正数进行计算
        pos_dividend = self._neg(dividend) if ((dividend >> 31) & 1) else dividend
        pos_divisor = self._neg(divisor) if ((divisor >> 31) & 1) else divisor

        # 调用核心除法器
        ans_pattern = self._div(pos_dividend, pos_divisor)

        # 根据之前确定的符号，决定是否对结果取反
        result_pattern = self._neg(ans_pattern) if is_negative else ans_pattern

        # 对最终的位模式进行转换后再返回
        return self._to_signed_int(result_pattern)

    def floor_divide(self, dividend: int, divisor: int) -> int:
        """
        使用位运算实现向负无穷取整的除法 (Python's // operator)。
        """
        # 步骤 1: 先计算出向零取整的结果
        q_trunc = self.divide(dividend, divisor)

        # 步骤 2: 判断是否需要修正

        # 条件 a: 符号是否不同
        signs_are_different = (((dividend >> 31) & 1) ^ ((divisor >> 31) & 1)) != 0

        # 条件 b: 是否存在余数 (余数 r = a - q * b)
        remainder = self.minus(dividend, self.multiply(q_trunc, divisor))
        remainder_is_not_zero = (remainder != 0)

        # 步骤 3 & 4: 如果同时满足两个条件，则减1；否则返回原结果
        if signs_are_different and remainder_is_not_zero:
            return self.minus(q_trunc, 1)
        else:
            return q_trunc

# --- 测试 ---
s = Solution()

print("向零取整 (Truncation):")
print(f" 7 /  3 = {s.divide(7, 3)}")
print(f"-7 /  3 = {s.divide(-7, 3)}")
print(f" 7 / -3 = {s.divide(7, -3)}")
print(f"-7 / -3 = {s.divide(-7, -3)}")
print(f"-10/  2 = {s.divide(-10, 2)}") # 能整除

print("\n向负无穷取整 (Floor Division):")
print(f" 7 //  3 = {s.floor_divide(7, 3)}")
print(f"-7 //  3 = {s.floor_divide(-7, 3)}") # <-- 结果不同
print(f" 7 // -3 = {s.floor_divide(7, -3)}") # <-- 结果不同
print(f"-7 // -3 = {s.floor_divide(-7, -3)}")
print(f"-10//  2 = {s.floor_divide(-10, 2)}") # 能整除


s = Solution()
print("加法")
print(s.add(1, 2))
print(s.add(-1, 2))
print(s.add(1, -2))
print("minus")
print(s.minus(1, 2))
print("multiply")
print(s.multiply(1, 2))
print(s.multiply(-1, 2))
print(s.multiply(1, -2))
print("divide")
print(s.divide(5, -1))
print(s.divide(-10, 2))
