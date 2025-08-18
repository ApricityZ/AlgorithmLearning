# // 位图的实现
# // Bitset是一种能以紧凑形式存储位的数据结构
# // Bitset(int n) : 初始化n个位，所有位都是0
# // void fix(int i) : 将下标i的位上的值更新为1
# // void unfix(int i) : 将下标i的位上的值更新为0
# // void flip() : 翻转所有位的值
# // boolean all() : 是否所有位都是1
# // boolean one() : 是否至少有一位是1
# // int count() : 返回所有位中1的数量
# // String toString() : 返回所有位的状态
# 	// 测试链接 : https://leetcode-cn.com/problems/design-bitset/

class Bitset:

    def __init__(self, size: int):
        self.bit_arr = [0] * ((size + 31) // 32)
        self.num_ones = 0
        self.num_zeros = size
        self.size = size
        self.reversed = False

    def fix(self, idx: int) -> None:
        if not self.reversed:
            if (((self.bit_arr[idx // 32] >> (idx % 32))) & 1) == 0:
                self.num_ones += 1
                self.num_zeros -= 1
                self.bit_arr[idx // 32] |= 1 << (idx % 32)
        else:
            if ((self.bit_arr[idx // 32]) >> (idx % 32)) & 1 == 1:
                self.num_ones += 1
                self.num_zeros -= 1
                self.bit_arr[idx // 32] &= ~(1 << (idx % 32))

    def unfix(self, idx: int) -> None:
        if not self.reversed:
            if (((self.bit_arr[idx // 32] >> (idx % 32))) & 1) == 1:
                self.num_ones -= 1
                self.num_zeros += 1
                self.bit_arr[idx // 32] &= ~(1 << (idx % 32))
        else:
            if ((self.bit_arr[idx // 32]) >> (idx % 32)) & 1 == 0:
                self.num_ones -= 1
                self.num_zeros += 1
                self.bit_arr[idx // 32] |= 1 << (idx % 32)

    def flip(self) -> None:
        self.reversed ^= 1
        self.num_ones, self.num_zeros = self.num_zeros, self.num_ones

    def all(self) -> bool:
        return self.num_ones == self.size

    def one(self) -> bool:
        return self.num_ones > 0

    def count(self) -> int:
        return self.num_ones

    def toString(self) -> str:
        result_arr = [0] * self.size
        for i in range(self.size):
            # if not reversed:  # 这里应该是self.reversed
            if not self.reversed:
                result_arr[i] = (self.bit_arr[i // 32] >> (i % 32)) & 1
            else:
                # result_arr[i] = ~((self.bit_arr[i // 32] >> (i % 32)) & 1)  # 想要反转0和1，应该使用异或运算，取反 ~x = -x -1，是按每一位取反得到补码
                # 操作 (Operation)	目标 (Goal)	示例	                        结果
                # ~ x (按位取反)	    翻转一个数在内存中的所有二进制位，并按补码解释	~0	-1
                # x ^ 1 (与1异或)	仅在整数 0 和 1 之间切换	                0 ^ 1	1
                #                                                           1 ^ 1	0
                result_arr[i] = ((self.bit_arr[i // 32] >> (i % 32)) & 1) ^ 1
        return ''.join(map(str, result_arr))


# Your Bitset object will be instantiated and called as such:
obj = Bitset(size=5)
obj.fix(idx=3)
obj.fix(idx=1)
obj.flip()
param_4 = obj.all()
obj.unfix(0)
obj.flip()
param_5 = obj.one()
obj.unfix(0)
param_6 = obj.count()
param_7 = obj.toString()
pass
