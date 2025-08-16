class Solution:
    def flip(self, n: int) -> int:
        """
        翻转0和1 (Flips 0 and 1).
        """
        return n ^ 1

    def get_sign(self, n: int) -> int:
        """
        [最稳健的实现]
        精确模拟32位整数，返回其符号。
        返回 1 如果 n 为非负数 (>= 0)。
        返回 0 如果 n 为负数 (< 0)。
        """
        # 步骤 1: 将Python的任意精度整数通过掩码强制转换为32位无符号数的等价物。
        # 0xffffffff 是 2**32 - 1，代表一个32位的全1掩码。
        # 这一步是关键，它模拟了值存入32位寄存器时的截断行为。
        val_32bit = n & 0xffffffff

        # 步骤 2: 对这个确定的32位数，检查其最高位(第31位)是否为1。
        # 右移31位会将符号位移动到最低位。
        # 如果原始符号位是1(负数)，结果为1；如果是0(非负数)，结果为0。
        is_negative = val_32bit >> 31

        # 步骤 3: 我们需要的结果是“非负为1，负为0”，所以翻转上一步的结果。
        return self.flip(is_negative)

    def getMax(self, a: int, b: int) -> int:
        """
        在模拟32位有符号整数行为下，返回a和b中的最大值。
        不用任何判断语句和比较操作。
        """
        # 计算 a-b 的差值c。
        # 注意：在Python中c的计算是精确的，可能会超过32位范围。
        c = a - b

        # 获取 a, b 的符号。因为输入保证在32位内，这里可以直接获取。
        sign_a = self.get_sign(a)
        sign_b = self.get_sign(b)

        # 获取 c 的符号。我们健壮的get_sign函数可以正确处理c溢出的情况。
        sign_c = self.get_sign(c)

        # 判断a和b的符号是否不同 (结果为1则不同, 0则相同)
        diff_sign = sign_a ^ sign_b
        # 判断a和b的符号是否相同 (结果为1则相同, 0则不同)
        same_sign = self.flip(diff_sign)

        # 核心决策逻辑：
        # use_a_factor为1则返回a，为0则返回b。
        # 情况1 (同号): same_sign=1, diff_sign=0。此时c的符号可靠，决策权交给sign_c。
        # 情况2 (异号): same_sign=0, diff_sign=1。此时c的符号不可靠，决策权交给sign_a (正数大)。
        use_a_factor = same_sign * sign_c + diff_sign * sign_a
        use_b_factor = self.flip(use_a_factor)

        # 根据决策因子返回a或b
        return a * use_a_factor + b * use_b_factor

# --- 测试代码 ---
if __name__ == "__main__":
    s = Solution()

    print("--- 常规测试 ---")
    print(f"Max of 1, 2 is: {s.getMax(1, 2)}")           # 预期: 2
    print(f"Max of 10, -5 is: {s.getMax(10, -5)}")      # 预期: 10
    print(f"Max of -10, -20 is: {s.getMax(-10, -20)}")  # 预期: -10

    print("\n--- 边界和溢出测试 ---")

    # 定义32位整数的最大值和最小值
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    # a-b 会发生正向溢出的情况
    # Python中 a-b = 2147483657，这是一个大于32位正数范围的值
    # 我们健壮的 get_sign(a-b) 会正确处理这种情况
    print(f"Max of {INT_MAX}, -10 is: {s.getMax(INT_MAX, -10)}") # 预期: 2147483647

    # a-b 会发生负向溢出的情况
    print(f"Max of {INT_MIN}, 10 is: {s.getMax(INT_MIN, 10)}")  # 预期: 10

    # 两个边界值比较
    print(f"Max of {INT_MAX}, {INT_MIN} is: {s.getMax(INT_MAX, INT_MIN)}") # 预期: 2147483647