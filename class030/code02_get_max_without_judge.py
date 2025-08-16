# // 不用任何判断语句和比较操作，返回两个数的最大值
# // 测试链接 : https://www.nowcoder.com/practice/d2707eaf98124f1e8f1d9c18ad487f76

class Solution:
    def getMax(self, a, b):
        # self.limit = 0xffffffff
        # a &= self.limit
        # b &= self.limit
        a_sign = self.get_sign(a)
        b_sign = self.get_sign(b)
        c = a - b
        c_sign = self.get_sign(c)
        diff_sign_a_b = a_sign ^ b_sign
        same_sign_a_b = self.flip(diff_sign_a_b)
        a_return = same_sign_a_b * c_sign + diff_sign_a_b * a_sign
        b_return = self.flip(a_return)
        return a_return * a + b_return * b

    def get_sign(self, val: int):
        """
        if val is negative, return 0, else return 1
        :param val: input val
        :return: 0 or 1
        """
        # return (val >> 31) + 1  如果 c 溢出 那么这里结果不再是0/1，比如时 floor(val >> 31) + 1 = 2，当val溢出时
        # return ((val >> 31) & 1) ^ 1  # 考虑边界条件，val=2^32-1,那么此时 val >> 31 = 1, 结果错误
        # return (((val & 0xffffffff) >> 31) & 1) ^ 1  # 可以更加简洁
        return ((val & 0xffffffff) >> 31) ^ 1

    # 让我来确认并稍微展开一下您的几点总结：
    # 1. 我们不论这个值是否发生了溢出，而只关心寄存器中，这个值应该为正还是为负
    # 这句话是 100%正确的，是整个算法的灵魂。get_sign 函数的工作就是一个忠实的“32位符号解读器”。它不管传给它的数字 n 是怎么来的（是通过正常计算还是溢出得到的），它只做一件事：分析 n 的二进制位模式，并报告“如果这是一个32位寄存器，它的符号是什么”。
    # 2. 只是因为python并不使用真正的寄存器，不会溢出
    # 这也完全正确。这正是我们所有讨论的根源。因为Python为我们处理了所有复杂的数学，给了我们一个精确的、可能非常大的数字 c，我们才需要反过来自己动手，去“模拟”如果这个计算是在一个有限的、会溢出的寄存器里发生时，会是什么情况。
    # 3. 我们认为，(n & 0x80000000)之后的数，就是在模仿寄存器中真实的数字
    # 您的理解非常接近了，这里我做一个微小但重要的补充，让它更精确：
    # n & 0xffffffff 这个操作，是在模仿将一个数字存入 32位寄存器 后得到的 位模式。
    # 而 n & 0x80000000 这个操作，是模仿我们去 检查 那个寄存器的 最高位（符号位） 的这个动作。
    # 所以，完整的逻辑链是：
    # Python 给了我们一个精确的数学结果 n。
    # 我们不在乎 n 在Python世界里有多大，我们只在乎它的低32位二进制是什么样的。
    # 我们使用 (n & 0x80000000) 这个工具，就像用一个探针去检测 n 的第31位。
    # 如果第31位是 1，这个“探针”操作就会得到一个非零结果，我们就能断定，在32位世界里，它是个负数。反之亦然。
    # 您的理解已经完全到位了。 正是因为Python的这个特性，我们才需要写出这样一个看起来有点“绕”的函数，来精确地解决这个限制在“32位有符号整数”世界里的问题。
    def flip(self, sign: int):
        """
        reverse input, the input must be in {0, 1}
        :param sign: 0 or 1
        :return: 1 or 0
        """
        return sign ^ 1

    def getMax1(self, a, b):
        c = a - b
        a_return = self.get_sign(c)
        b_return = self.flip(a_return)
        return a_return * a + b_return * b


s = Solution()
print(s.getMax(1, 2))
