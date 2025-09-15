# // N皇后问题
# // 测试链接 : https://leetcode.cn/problems/n-queens-ii/
import time


class Solution:
    def totalNQueens1(self, n: int) -> int:
        path: list[int] = [0] * n
        return self.recursive_try1(0, path, n)

    def recursive_try1(self, i: int, path: list[int], n: int) -> int:
        """

        :param i: 来到第几行了
        :param path: 从 0 到 i - 1行，每个皇后放置的列位置
        :param n: 问题的规模，固定值，是几皇后问题
        :return: 在 0 到 i - 1 行放置好的情况下，从 i 到 n - 1行放置皇后的所有可能结果数量
        """
        # base case
        ans = 0
        if i == n:
            return 1
        for j in range(n):
            if self.check(path, i, j):
                path[i] = j
                # only one queen is put on one row, call recursive fun
                ans += self.recursive_try1(i + 1, path, n)
        return ans

    def check(self, path: list[int], i: int, j: int) -> bool:
        """

        :param path: list recorded 0 ~ i - 1 rows queen's column index
        :param i: current row index
        :param j: current column index
        :return: bool, whether the jth column idx is available
        """
        for x in range(i):
            if j == path[x] or abs(j - path[x]) == abs(i - x):
                return False
        return True

    def totalNQueens2(self, n: int) -> int:
        limit = (1 << n) - 1
        return self.recursive_try2(limit, 0, 0, 0)

    def recursive_try2(self, limit: int, col_ban: int, left_ban: int, right_ban: int):
        """

        :param limit: 问题规模限制，用位状态表示
        :param col_ban: 记录了从 0 到 i - 1 行的皇后放置的列索引，为 1 表示放置了皇后，其余行不能再放置皇后
        :param left_ban: 记录了 0 到 i - 1 行 从右上 -> 左下对角线方向上相关的禁止放置位置
        :param right_ban: 记录 0 到 i - 1 行 从 左上 -> 右下对角线方向上相关的进制放置位置
        :return: 在 0 到 i - 1 行已经放置好皇后的情况下，从 i 到 n - 1行能放置皇后的所有情况数量
        """
        # 遇事不决，递归中先写base case
        ans = 0
        if col_ban == limit:
            return 1
        # 所有的禁止放置皇后的位状态
        ban = col_ban | left_ban | right_ban
        # 通过取反，现在位状态含义为：1可以放置皇后，0不可以放置皇后
        candidate = ~ban & limit
        while candidate != 0:
            place = candidate & (-candidate)
            # 使最低位的1变成0
            candidate ^= place
            # 进入下一行，开始递归
            ans += self.recursive_try2(limit, col_ban | place, (left_ban | place) >> 1, (right_ban | place) << 1)
        return ans

def main():
    solution = Solution()
    test_n1 = 12
    start_time = time.time()
    solution.totalNQueens1(test_n1)
    end_time = time.time()
    print(f"list version time with n = {test_n1} is {end_time - start_time} s")

    start_time = time.time()
    solution.totalNQueens2(test_n1)
    end_time = time.time()
    print(f"bit version time with n = {test_n1} is {end_time - start_time} s")

    test_n2 = 15
    start_time = time.time()
    solution.totalNQueens1(test_n2)
    end_time = time.time()
    print(f"list version time with n = {test_n2} is {end_time - start_time} s")

if __name__ == '__main__':
    main()
    # list version time with n = 12 is 5.5908026695251465 s
    # bit version time with n = 12 is 0.3070485591888428 s
    # bit version time with n = 15 is 56.438337326049805 s
    # list version time with n = 15 is 1541.1964111328125 s = 26 min