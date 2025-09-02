# 描述
# 给定一个字符串s，长度为n，求s的所有子序列
# 1.子序列: 指一个字符串删掉部分字符（也可以不删）形成的字符串，可以是不连续的，比如"abcde"的子序列可以有"ace","ad"等等
# 2.将所有的子序列的结果返回为一个字符串数组
# 3.字符串里面可能有重复字符，但是返回的子序列不能有重复的子序列，比如"aab"的子序列只有"","a","aa","aab","ab","b"，不能存在2个相同的"ab"
# 4.返回字符串数组里面的顺序可以不唯一
from typing import List


# // 字符串的全部子序列
# // 子序列本身是可以有重复的，只是这个题目要求去重
# // 测试链接 : https://www.nowcoder.com/practice/92e6247998294f2c933906fdedbc6e6a

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return string字符串一维数组
#
class Solution:
    def generatePermutation1(self, s: str) -> List[str]:
        # list_s: list[str] = s.strip().split()  # 错误，split默认根据空格分割，应使用list(s)直接转换成list[str]
        list_s = list(s)
        set_ans: set[str] = set()
        path: str = ""
        # recursive function
        self.recursive_process1(list_s, 0, path, set_ans)
        # collect the unrepeatable str ans
        list_ans = []
        for str_ans in set_ans:
            list_ans.append(str_ans)
        return list_ans

    def recursive_process1(self, list_s: list[str], i: int, path: str, ans_set: set[str]):
        # base case
        if i == len(list_s):
            ans_set.add(path)
        # main recursion
        else:
            # 好像没错，path在这里虽然不是全局变量，按引用传递，但是和下面直接更改传递参数的效果是一样的
            path += list_s[i]  # -错误-，我们这里实际上使用的是 str 类型，不会按照引用传递，而是按值传递，所以path不能一直复用并记录更改
            self.recursive_process1(list_s, i + 1, path, ans_set)
            path = path[:-1]  # 同上
            self.recursive_process1(list_s, i + 1, path, ans_set)

    def generatePermutation2(self, s: str) -> List[str]:
        chars = list(s)  # 更简洁的写法
        ans_set = set()
        self.recursive_process2(chars, 0, "", ans_set)
        return list(ans_set)  # 更简洁的写法

    def recursive_process2(self, chars: List[str], i: int, path: str, ans_set: set[str]):
        if i == len(chars):
            ans_set.add(path)

        else:
            self.recursive_process2(chars, i + 1, path + chars[i], ans_set)  # 由于 str 类型不能按引用传递，可以直接更改传入参数

            self.recursive_process2(chars, i + 1, path, ans_set)

    def generatePermutation3(self, s: str) -> List[str]:
        chars = list(s)
        ans_set = set()
        path = [0] * len(chars)
        self.recursive_process3(chars, 0, path, 0, ans_set)
        return list(ans_set)

    def recursive_process3(self, chars, i, path, size, ans_set: set[str]):
        if i == len(chars):
            ans_set.add("".join(path[:size]))
        else:
            path[size] = chars[i]
            self.recursive_process3(chars, i + 1, path, size + 1, ans_set)
            self.recursive_process3(chars, i + 1, path, size, ans_set)


obj = Solution()
s = "abc"
ans = obj.generatePermutation2(s)
print(ans)
