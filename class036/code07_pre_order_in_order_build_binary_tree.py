# // 利用先序与中序遍历序列构造二叉树
# // 测试链接 : https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or (not inorder) or (len(preorder) != len(inorder)):
            return None

        _map: dict[int, int] = dict()

        for i in range(len(inorder)):
            _map.update({inorder[i]: i})

        return self.recursive_left_head_right(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, _map)

    def recursive_left_head_right(self, preorder: list[int], l1: int, r1: int,
                                  inorder: list[int], l2: int, r2: int, map_idx: dict[int, int]) -> Optional[TreeNode]:
        if l1 > r1:
            return None
        head = TreeNode(preorder[l1])
        if l1 == r1:
            return head
        head_in_inorder_idx = map_idx[head.val]
        head.left = self.recursive_left_head_right(preorder, l1 + 1, l1 + 1 + head_in_inorder_idx - 1 - l2, inorder, l2,
                                                   head_in_inorder_idx - 1, map_idx)
        head.right = self.recursive_left_head_right(preorder, l1 + 1 + head_in_inorder_idx - l2, r1, inorder,
                                                    head_in_inorder_idx + 1, r2, map_idx)
        return head
