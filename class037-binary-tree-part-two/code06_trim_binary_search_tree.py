# // 修剪搜索二叉树
# // 测试链接 : https://leetcode.cn/problems/trim-a-binary-search-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# =--=-=-=-=--=-=-=-=-=-=-=-=-= #
# 要么if-else分支，basecase在其中一个分支，只需要一个return
# 像下面这种，触发条件后如果之后的代码不需要再被运行，一定要使用return语句，否则分支之外的代码仍被运行了

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # base case
        if root is None:
            return None  # 返回值是节点

        if root.val < low:
            # self.trimBST(root.right, low, high)  # 走完这里，应该直接return，下面的代码不应该再被运行了
            return self.trimBST(root.right, low, high)
        # if root.val > low:  # 写错鸟，该是high
        if root.val > high:
            # self.trimBST(root.left, low, high)  # 走完这里，应该直接return，下面的代码不应该再被运行了
            return self.trimBST(root.left, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root

root = TreeNode(1, TreeNode(0), TreeNode(2))
obj = Solution()
print(obj.trimBST(root, 1, 2))