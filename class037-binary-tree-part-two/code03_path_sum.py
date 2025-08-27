# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
# 叶子节点 是指没有子节点的节点。
# // 收集累加和等于aim的所有路径
# // 测试链接 : https://leetcode.cn/problems/path-sum-ii/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ================================ #
# 采用递归的方法，每进入一个非叶节点，我们都要先将节点添加到路径中，因为只有到叶节点我们才能知道这条路径是否满足条件
# 当进入叶节点时，我们需要先判断这条路径是否满足累加和为目标和，满足的话添加到path中，并且将整条path添加到ans中
# 注意，由于我们希望path在同一个节点的状态相同，也就是意味着每当退出一个节点，该节点就需要从path中移除，此为 递归中的现场恢复
# 最后总结一下递归条件： base case: 遇到叶节点  返回值：什么都不返回，只需要退出；不写return语句其实意味着返回None
# ================================ #

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # ans: Optional[List[List[int]]] = None  # 初始化不应该是None，否则遇到append会直接报错，应该初始化为空列表 []
        ans: List[List[int]] = []
        if root:
            # path: Optional[List[int]] = None  # 同上
            path: List[int] = []
            self.precess_recursive(root, 0, targetSum, path, ans)
        return ans

    def precess_recursive(self, root: TreeNode, cur_sum, targetSum: int, path: List[int], ans: List[List[int]]):
        # base case
        if root.right is None and root.left is None:
            if root.val + cur_sum == targetSum:
                path.append(root.val)
                ans.append(path.copy())
                path.pop()
                # return nothing, namely None
        else:
            path.append(root.val)
            if root.left:  # 我们不需要进入None的节点，因为空节点不会为path做出贡献
                self.precess_recursive(root.left, root.val + cur_sum, targetSum, path, ans)
            if root.right:
                self.precess_recursive(root.right, root.val + cur_sum, targetSum, path, ans)
            path.pop()
