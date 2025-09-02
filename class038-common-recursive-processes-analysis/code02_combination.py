# // 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的组合
# // 答案 不能 包含重复的组合。返回的答案中，组合可以按 任意顺序 排列
# // 注意其实要求返回的不是子集，因为子集一定是不包含相同元素的，要返回的其实是不重复的组合
# // 比如输入：nums = [1,2,2]
# // 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
# // 测试链接 : https://leetcode.cn/problems/subsets-ii/
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的 子集（幂集）。
#
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans: List[List[int]] = list()
        path: List[int] = [0] * len(nums)
        self.recursive(nums, 0, path, 0, ans)
        return ans

    def recursive(self, nums: List[int], i: int, path: List[int], size: int, ans: List[List[int]]):
        if i == len(nums):  # 这里和27行也是相互关联的
            ans.append(path[:size])
        else:
            j = i
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            self.recursive(nums, j, path, size, ans)
            for k in range(j - i):  # 27行和29行是相互关联的
                path[size] = nums[i]
                size += 1
                self.recursive(nums, j, path, size, ans)

nums = [1, 1, 2]
ret = Solution().subsetsWithDup(nums)
print(ret)