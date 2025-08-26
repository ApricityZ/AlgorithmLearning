# // 求二叉树的最大、最小深度
#
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 	// 测试链接 : https://leetcode.cn/problems/maximum-depth-of-binary-tree/
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 0 if not root else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # 	// 测试链接 : https://leetcode.cn/problems/minimum-depth-of-binary-tree/
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1

        left_depth = 2 ** 31 - 1
        right_depth = 2 ** 31 - 1

        if root.left:
            left_depth = self.minDepth(root.left)
        if root.right:
            right_depth = self.minDepth(root.right)
        return min(left_depth, right_depth) + 1