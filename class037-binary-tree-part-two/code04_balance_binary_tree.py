# // 验证平衡二叉树
# // 测试链接 : https://leetcode.cn/problems/balanced-binary-tree/
# Definition for a binary tree node.
from idlelib.autocomplete import TRY_A
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ================================================== #
# 采用递归的方式，遍历每一个节点的子树是否是平衡二叉树
# 涉及到二叉树的最深层数计算
# 全局变量/变量传递的使用
# base case：遇到空节点，空节点会进入循环
# return value： 当前节点为根节点的（子）数的高度，空节点的高度为0
# 使用self.attr 是更见方便的全局状态共享的方式
# =================================================== #

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True
        if root:
            _, balance = self.verify_height(root, global_balance=balance)
        return balance

    def verify_height(self, root: TreeNode, global_balance: bool) -> tuple[int, bool]:  # 要注意，直接传递是改变不了balance的
        # base case
        if not global_balance or root is None:
            # 返回值：从当前节点的树高，None为0
            return 0, True
        left_height, l_balance = self.verify_height(root.left, global_balance)
        right_height, r_balance = self.verify_height(root.right, global_balance)
        if abs(left_height - right_height) > 1:
            global_balance = False
        return max(left_height, right_height) + 1, global_balance


root = TreeNode(1, TreeNode(2), TreeNode(2))
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
s = Solution()
ans = s.isBalanced(root)
print(ans)
