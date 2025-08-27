# // 求完全二叉树的节点个数
# // 测试链接 : https://leetcode.cn/problems/count-complete-tree-nodes/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.count_tree(root, 1, self.most_left_height(root, 1))

    def count_tree(self, head: TreeNode, level: int, tree_height: int) -> int:
        if level == tree_height:
            return 1
        if head.right and self.most_left_height(head.right, level + 1) == tree_height:
            return (1 << (tree_height - level)) + self.count_tree(head.right, level + 1, tree_height)
        else:
            return (1 << (tree_height - level - 1)) + self.count_tree(head.left, level + 1, tree_height)

    def most_left_height(self, head: TreeNode, level: int) -> int:
        while head and head.left:  # 现在这种写法呢，在第一次从root计算树高时没问题，但是由于在 23 行，如果不加head.right的判断条件，
            # 那么就会导致不存在右孩子的时候，由于输入的level已经＋1，然后这里没有进入循环直接返回了 level +1 ，会判定右子树未满，其实右子树为空；
            # 解决这一问题的方法是，先判定存在右孩子，没有有孩子不会计算右子树高度；避免额外先 level + 1
            level += 1
            head = head.left
        return level

root = TreeNode(1, TreeNode(2), TreeNode(3))
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
s = Solution()
ans = s.countNodes(root)
print(ans)
