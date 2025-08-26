# // 验证完全二叉树
# // 测试链接 : https://leetcode.cn/problems/check-completeness-of-a-binary-tree/

# 给你一棵二叉树的根节点 root ，请你判断这棵树是否是一棵 完全二叉树 。
#
# 在一棵 完全二叉树 中，除了最后一层外，所有层都被完全填满，并且最后一层中的所有节点都尽可能靠左。最后一层（第 h 层）中可以包含 1 到 2h 个节点。

# 我们采用层序遍历的方式，注意检查每一个节点，判断条件如下：
# 1. 如果该节点有右节点而无左节点，那么直接判定为 非完全二叉树
# 2. 如果我们已经检测到了叶子节点，那么之后的点都必须时叶子节点，否则也是非完全二叉树

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        max_len = 101
        queue_node: list[TreeNode | None] = [None] * max_len
        l = r = 0
        if root is None:
            return True
        queue_node[r] = root
        r += 1
        detect_leaf_node = False
        while l < r:
            node = queue_node[l]
            l += 1
            if (node.left is None and node.right is not None) or (detect_leaf_node and (node.left or node.right)):
                return False

            if node.left:
                queue_node[r] = node.left
                r += 1

            if node.right:
                queue_node[r] = node.right
                r += 1

            # if node.left is not None and node.right is None:  # 叶节点的判断方式有误，但凡一个节点没有左孩子或右孩子，那么该节点即为叶节点，即该节点在最下层（部分在最下层，左右孩子不全）
            if node.left is None or node.right is None:
                detect_leaf_node = True
        return True
