# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# // 普通二叉树上寻找两个节点的最近公共祖先
# // 测试链接 : https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> TreeNode | None:
        # basecase : 遇到null， p or q
        if root is None or root is p or root is q:
            # 返回值：当前节点
            return root

        l: TreeNode = self.lowestCommonAncestor(root.left, p, q)
        r: TreeNode = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root

        if l is None and r is None:
            return None

        return l if l else r

