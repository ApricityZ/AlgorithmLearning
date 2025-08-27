# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# // 搜索二叉树上寻找两个节点的最近公共祖先
# // 测试链接 : https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


##============================================================================##
# 从搜索二叉树的性质出发，不用使用遍历，只需要判断当前节点与p，q值的大小关系，一直往左/右移动即可
# 如果遇到了p/q，该节点即为最近公共祖先
##============================================================================##
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root is not p and root is not q:
            if min(p.val, q.val) < root.val < max(p.val, q.val):
                return root
            root = root.left if root.val > max(p.val, q.val) else root.right
        return root
