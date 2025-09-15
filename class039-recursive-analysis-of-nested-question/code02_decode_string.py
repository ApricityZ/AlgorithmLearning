# // 含有嵌套的字符串解码
# // 测试链接 : https://leetcode.cn/problems/decode-string/

# 给定一个经过编码的字符串，返回它解码后的字符串。
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像3a或2[4]的输入。
# 测试用例保证输出的长度不会超过105。
# 示例 1：
# 输入：
# s = "3[a]2[bc]"
# 输出：
# "aaabcbc"

class Solution:
    def __init__(self):
        self.where = 0

    def decodeString(self, s: str) -> str:
        # path: list[str] = []  # path应为递归函数的局部变量
        return "".join(self.recursive(s, 0))

    def recursive(self, s: str, i: int):
        repeat_time = 0
        path: list[str] = list()
        while i < len(s) and s[i] != ']':
            if 'a' <= s[i] <= 'z':
                path.append(s[i])
                i += 1
            elif s[i] != '[':
                repeat_time = repeat_time * 10 + int(s[i])
                i += 1
            else:
                ret_path = self.recursive(s, i + 1)
                self.concat(path, ret_path, repeat_time)
                repeat_time = 0  # 这里一定要把重复次数清零，一旦处理完当前掉一个子调用，否则第二次重复次数变成了 32 ！
                i = self.where + 1

        # path.append(s[i])  # 我研究了一下，似乎不会发生最后一个元素没有被添加的情况
        self.where = i
        return path

    def concat(self, cur_path: list[str], ret_path: list[str], repeat_times: int):
        for _ in range(repeat_times):
            cur_path.extend(ret_path)

print(Solution().decodeString("3[a]2[bc]"))