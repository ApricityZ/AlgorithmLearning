# // 没有重复项数字的全排列
# // 测试链接 : https://leetcode.cn/problems/permutations/
from typing import List

# ============ #
# 本题中，我们使用nums列表本身作为路径，通过直接操作nums元素的交换，实现不同路径的遍历
# 我们通过让 j 索引位置元素不断放在 某类 组合结果的第一个位置，来实现全部遍历
# 递归总是 dfs 深度优先 的，所以我们最要从最基本的情况，一步一步网上推演，得到整体的复杂，看似混乱的结果
# ============ #


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = list()
        self.recursive_swap(nums, 0, ans)
        return ans

    def recursive_swap(self, num: List[int], i: int, ans: List[List[int]]):
        if i == len(num):
            ans.append(num.copy())
        else:
            j = i
            while j < len(num):
                self.swap(num, i, j)
                self.recursive_swap(num, i + 1, ans)
                self.swap(num, i, j)
                j += 1

    def swap(self, num, i, j):
        tmp = num[i]
        num[i] = num[j]
        num[j] = tmp
