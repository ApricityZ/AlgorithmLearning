# // 二叉树打家劫舍问题
# // 测试链接 : https://leetcode.cn/problems/house-robber-iii/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.yes: int
        self.no: int

    def rob(self, root: Optional[TreeNode]) -> int:
        self._rob(root)
        return max(self.yes, self.no)

    def _rob(self, root: Optional[TreeNode]) -> None:
        if root is None:
            self.yes = 0
            self.no = 0
        else:
            y = root.val
            n = 0
            self._rob(root.left)
            y += self.no
            n += max(self.yes, self.no)
            self._rob(root.right)
            y += self.no
            n += max(self.yes, self.no)
            self.yes = y
            self.no = n
