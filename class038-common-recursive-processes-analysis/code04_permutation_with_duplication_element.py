# // 有重复项数组的去重全排列
# // 测试链接 : https://leetcode.cn/problems/permutations-ii/
from typing import List


class Solution:
    def permuteUnique1(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = list()
        is_duplication_set: set[int] = set()  # 这里的的判重set应该是每个递归函数内部有一个，而不是全局的，set记录和当前[i]交换过的数字，防止重复交换
        self.recursive_swap_skip_dupli1(nums, 0, is_duplication_set, ans)
        return ans

    def recursive_swap_skip_dupli1(self, nums: List[int], i: int, is_dupli_set: set, ans: List[List[int]]):
        if i == len(nums):
            ans.append(nums.copy())
        else:
            j = i
            while j < len(nums):
                if not (nums[j] in is_dupli_set):
                    is_dupli_set.add(nums[j])  # 忘记添加这个元素了，否则这个分支就一直成立，无法避免重复
                    self.swap(nums, i, j)
                    self.recursive_swap_skip_dupli1(nums, i + 1, is_dupli_set, ans)
                    self.swap(nums, i, j)
                    j += 1
                j += 1  # j 的增加在这里应该放在判断条件的外面

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = list()
        self.recursive_swap_sd(nums, 0, ans)
        return ans

    def recursive_swap_sd(self, nums: List[int], i: int, ans: List[List[int]]):
        if i == len(nums):
            ans.append(nums.copy())
        else:
            j = i
            is_dupli_set = set()  # 这里要尤其注意，判重的set是在每个递归调用内部的，不是全局的
            while j < len(nums):
                if not (nums[j] in is_dupli_set):
                    is_dupli_set.add(nums[j])
                    self.swap(nums, i, j)
                    self.recursive_swap_sd(nums, i + 1, ans)
                    self.swap(nums, i, j)
                    j += 1
                else:
                    j += 1

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp


nums = [1, 1, 2]
ret = Solution().permuteUnique(nums)
