# // 有装下8个苹果的袋子、装下6个苹果的袋子，一定要保证买苹果时所有使用的袋子都装满
# // 对于无法装满所有袋子的方案不予考虑，给定n个苹果，返回至少要多少个袋子
# // 如果不存在每个袋子都装满的方案返回-1

class AppleMinBags:
    def find(self, n):
        ans = self.recursive_fid(n)
        return ans if ans != 2 ** 31 - 1 else -1

    def recursive_fid(self, n):
        """
        还剩n个苹果，至少需要几个袋子装？
        :param n: 剩余的苹果数量
        :return: 需要的最少的袋子
        """
        max_val = 2 ** 31 - 1
        if n < 0:
            return max_val
        if n == 0:
            return 0
        p1 = self.recursive_fid(n - 8)
        p2 = self.recursive_fid(n - 6)
        p1 += 0 if p1 == max_val else 1
        p2 += 0 if p2 == max_val else 1
        return min(p1, p2)


def min_bags(n):
    if (n & 1) != 0:
        return -1
    if n <= 17:
        if n == 6 or n == 8:
            return 1
        elif n == 12 or n == 14 or n == 16:
            return 2
        elif n == 0:
            return 0
        else:
            return -1
    else:
        return (n - 18) // 8 + 3

def main():
    for i in range(100):
        print(str(i) + ': ' + str(AppleMinBags().find(i)) + ' | ' + str(min_bags(i)))

if __name__ == '__main__':
    main()