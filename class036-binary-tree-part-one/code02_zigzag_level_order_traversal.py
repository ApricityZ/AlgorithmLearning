# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# // 二叉树的锯齿形层序遍历
# // 测试链接 : https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        max_len = 2001
        queue_node_list: list[Optional[TreeNode]] = [None] * max_len
        l = r = 0
        ans: list[list[int]] = list()
        reverse_val_list = False

        if root is not None:
            queue_node_list[r] = root
            r += 1
            while l < r:
                # cur_level_size = l - r  # 应该是r - l，这里要注意，总是无意识地顺手写成 l - r
                cur_level_size = r - l

                cur_level_val_list = [queue_node_list[i].val for i in range(l, r)] if not reverse_val_list else \
                    [queue_node_list[i].val for i in range(r - 1, l - 1, -1)]

                for _ in range(cur_level_size):
                    cur_node = queue_node_list[l]
                    l += 1
                    if cur_node.left:
                        queue_node_list[r] = cur_node.left
                        r += 1
                    if cur_node.right:
                        queue_node_list[r] = cur_node.right
                        r += 1
                ans.append(cur_level_val_list)
                reverse_val_list = not reverse_val_list
        return ans
