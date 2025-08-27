# // 验证搜索二叉树
# // 测试链接 : https://leetcode.cn/problems/validate-binary-search-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 中序遍历，逐个元素验证顺序关系
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_len = 10001
        stack: list[TreeNode | None] = [None] * max_len
        r = 0
        pre: Optional[TreeNode] = None
        ans = True
        if root:
            while root or r > 0:  # 遍历条件中，root可能为空，判断条件不完整；应加上 r > 0
                if root:
                    stack[r] = root
                    r += 1
                    root = root.left
                else:
                    r -= 1
                    node = stack[r]
                    if pre and pre.val >= node.val:
                        ans = False
                        return ans
                    pre = node
                    root = node.right

        return ans

    def __init__(self):
        self.min = 0
        self.max = 0

    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            self.min = 2 ** 31 - 1
            self.max = -2 ** 31
            return True  # 不要忘记了basecase中的返回值
        lok = self.isValidBST1(root.left)
        lmin = self.min
        lmax = self.max
        rok = self.isValidBST1(root.right)
        rmin = self.min
        rmax = self.max
        self.min = min(lmin, rmin, root.val)
        self.max = max(lmax, rmax, root.val)

        return lok and rok and (lmax < root.val < rmin)  # 由于这里要严格小于或大于，所以上面的min/max值要取得范围更大一些


root = TreeNode(5, TreeNode(1), TreeNode(4))
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
obj = Solution()
print(obj.isValidBST(root))
