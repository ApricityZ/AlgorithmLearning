# // 可以用r、e、d三种字符拼接字符串，如果拼出来的字符串中
# // 有且仅有1个长度>=2的回文子串，那么这个字符串定义为"好串"
# // 返回长度为n的所有可能的字符串中，好串有多少个
# // 结果对 1000000007 取模， 1 <= n <= 10^9
# // 示例：
# // n = 1, 输出0
# // n = 2, 输出3
# // n = 3, 输出18

class RedPalindromeGoodString:
    def num(self, n: int):
        """
        逐函数，判断当r e d 组成n长度字符串时，有几个好串
        :param n: 需要拼成多长的字符串
        :return: 所有结果中好串的个数
        """
        path: list[str] = [""] * n
        ans = self.recursive_count(path, 0, n)
        return ans

    def recursive_count(self, path: list[str], i: int, n: int) -> int:
        """
        返回 0 到 i-1 位置上已经放好字符，从 i 到 n-1 所有可能结果中好串的数量
        :param path: 路径记录，记录 0 到 i-1 添加的字符
        :param i: 字符串来到 i 位置
        :param n: 字符串总长度
        :return: 好串的数量
        """
        # base case
        if i == n:
            cnt = 0
            for j in range(n):
                for k in range(j + 1, n):
                    # 判断是否回文
                    if self.is_palindrom(path[j: k + 1]):
                        cnt += 1
                        if cnt > 1:
                            return 0
            if cnt == 1:
                return 1
            else:
                return 0
        # recursion
        ans = 0
        path[i] = 'r'
        ans += self.recursive_count(path, i + 1, n)
        path[i] = 'e'
        ans += self.recursive_count(path, i + 1, n)
        path[i] = 'd'
        ans += self.recursive_count(path, i + 1, n)
        return ans

    def is_palindrom(self, s: list[str]) -> bool:
        """
        判断s是否为回文
        :param s: 输入的字符串
        :return: 是否为回文，True满足，False不满足
        """
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


def find_pattern():
    for i in range(11):
        print(f"{i} : {RedPalindromeGoodString().num(i)}")


find_pattern()


# 0 : 0
# 1 : 0
# 2 : 3
# 3 : 18
# 4 : 30
# 5 : 36
# 6 : 42
# 7 : 48
# 8 : 54
# 9 : 60
# 10 : 66

def num2(n):
    if n <= 3:
        if n == 0 or n == 1:
            return 0
        if n == 2:
            return 3
        if n == 3:
            return 18
    return (n - 4) * 6 + 30


def validate():
    for i in range(11):
        if RedPalindromeGoodString().num(i) != num2(i):
            print("Error" + f" in {i}")
    print("Finished")


validate()
