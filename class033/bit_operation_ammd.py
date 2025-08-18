class BitOperationBasicOperation:
    def __init__(self):
        # self._mask = (1 << 32) - 1  # 这里可以用下面定义
        self._mask = (~0) ^ ((~0) << 32)  # 0xFFFFFFFF, 32位掩码
        # A = ~0 = (-1)   = ...11111111 11111111 11111111 11111111 11111111
        # B = (~0) << 32  = ...11111111 00000000 00000000 00000000 00000000
        # ------------------------------------------------------------------
        # A ^ B (异或结果)  = ...00000000 11111111 11111111 11111111 11111111
        self._min_value = (1 << 31)
        self._max_value = self._min_value ^ self._mask

    def _add(self, a, b):
        a &= self._mask
        b &= self._mask
        ans = a
        while b != 0:
            ans = (a ^ b) & self._mask
            b = ((a & b) << 1) & self._mask
            a = ans
        return ans

    def _neg(self, a):
        return self._add(~a, 1)

    def _minus(self, a, b):
        return self._add(a, self._neg(b))

    def _multiply(self, a, b):
        a &= self._mask
        b &= self._mask
        ans = 0
        while b != 0:
            if b & 1:
                ans = self._add(ans, a)
            b >>= 1
            a = (a << 1) & self._mask
        return ans

    def _div(self, a, b):
        """只接受a，b均为正数"""
        a &= self._mask
        b &= self._mask
        ans = 0
        for i in range(30, -1, -1):
            if (self._add((a >> i), self._neg(b)) >> 31) & 1:
                continue
            ans |= 1 << i
            # 错误做法: a = a - (b * ans)。每次都从部分消耗的 a 中，减去一个不断变大的累积值 ans，逻辑上是矛盾的。
            #
            # 正确做法: a = a - (b << i)。每次只从 a 中，减去当前循环所对应的那个固定大小的块 (b * 2^i)。
            # a = self._minus(a, self._multiply(b, ans))  # 这里错误地减去了累计值
            a = self._minus(a, (b << i) & self._mask)  # 这里其实可以直接写b << i不用mask，因为这里都是正数，并且这一步的前提是 a >= b << i，不会溢出
        return ans

    def _to_signed_num(self, num):
        num &= self._mask
        if (num >> 31) & 1:
            return ~(num ^ self._mask)
        return num

    def add(self, a, b):
        ans = self._add(a, b)
        return self._to_signed_num(ans)

    def minus(self, a, b):
        ans = self._minus(a, b)
        return self._to_signed_num(ans)

    def multiply(self, a, b):
        ans = self._multiply(a, b)
        return self._to_signed_num(ans)

    def divide(self, dividend, divisor):
        if divisor == 0:
            raise ZeroDivisionError("divisor is zero")
        if dividend == 0:
            return 0

        dividend_pattern = dividend & self._mask
        divisor_pattern = divisor & self._mask

        if divisor_pattern == self._min_value:
            if dividend_pattern == self._min_value:
                return 1
            else:
                return 0

        if dividend_pattern == self._min_value:
            if divisor == -1:
                return self._max_value

        if dividend_pattern == self._min_value:
            quotient = self.divide(self.add(dividend, 1), divisor)

            reminder = self.minus(dividend, self.multiply(divisor, quotient))

            correction = self.divide(reminder, divisor)

            return self.add(quotient, correction)

        diff_sign = ((dividend >> 31) & 1) ^ ((divisor >> 31) & 1)  # 先判断符号，再统一为正数

        dividend = self._neg(dividend) if (dividend >> 31) & 1 else dividend
        divisor = self._neg(divisor) if (divisor >> 31) & 1 else divisor

        ans = self._div(dividend, divisor)
        ans = self._neg(ans) if diff_sign else ans
        return self._to_signed_num(ans)


bbo = BitOperationBasicOperation()
print("add")
print(bbo.add(1, 2))
print(bbo.add(-1, 2))
print(bbo.add(1, -2))
print("minus")
print(bbo.minus(1, 2))
print(bbo.minus(-1, 2))
print(bbo.minus(1, -2))
print(bbo.minus(-1, -2))
print("multiply")
print(bbo.multiply(1, 2))
print(bbo.multiply(-1, 2))
print(bbo.multiply(1, -2))
print(bbo.multiply(-1, -2))
print("divide")
print(bbo.divide(1, 2))
print(bbo.divide(-10, 5))
print(bbo.divide(12, -5))
print(bbo.divide(-2 ** 31, -2 ** 30))
print(bbo.divide(2147483647, 1))
