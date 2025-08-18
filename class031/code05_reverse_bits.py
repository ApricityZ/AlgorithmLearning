# // 逆序二进制的状态
# // 测试链接 : https://leetcode.cn/problems/reverse-bits/
# 颠倒给定的 32 位无符号整数的二进制位。


class Solution:
    def reverseBits(self, n: int) -> int:
        n = ((n << 1) & 0xaaaaaaaa) | ((n >> 1) & 0x55555555)  # 注意应该同时左移 右移，才能达到交换位置的目的
        n = ((n << 2) & 0xcccccccc) | ((n >> 2) & 0x33333333)
        n = ((n << 4) & 0xf0f0f0f0) | ((n >> 4) & 0x0f0f0f0f)
        n = ((n << 8) & 0xff00ff00) | ((n >> 8) & 0x00ff00ff)
        n = ((n << 16) & 0xffff0000) | ((n >> 16) & 0x0000ffff)
        return n
