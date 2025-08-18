# // 位图的实现
# // Bitset(int size)
# // void add(int num)
# // void remove(int num)
# // void reverse(int num)
# // boolean contains(int num)
import random


class BitSet:
    def __init__(self, n):
        # n: 一共n个数， 位图需要记录【0，n-1】范围数字状态
        self.bit_arr = [0] * ((n + 31) // 32)

    def add(self, num):
        self.bit_arr[num // 32] |= 1 << (num % 32)

    def remove(self, num):
        self.bit_arr[num // 32] &= ~(1 << (num % 32))

    def reverse(self, num):
        self.bit_arr[num // 32] ^= 1 << (num % 32)

    def contains(self, num):
        return (self.bit_arr[num // 32] >> (num % 32)) & 1


def main():
    n = 10000
    test_times = 100000
    bitset = BitSet(n)
    # ref_dict = dict()  # 这里应该使用hashset对应的set，而不是hashmap对应的dict
    ref_set = set()
    print("测试开始")
    for _ in range(test_times):
        decision = random.random()
        num = random.randint(0, n - 1)
        if decision < 0.33:
            bitset.add(num)
            # ref_dict.update(num)
            ref_set.add(num)
        elif decision < 0.66:
            bitset.remove(num)
            ref_set.discard(num)
        else:
            bitset.reverse(num)
            ref_set ^= {num}

    for i in range(n):
        if bitset.contains(i) != (i in ref_set):
            print("出错了！")
    print("测试完成")


if __name__ == '__main__':
    main()
