# 102. 二叉树的层序遍历
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
import queue
from typing import Optional, List


# // 二叉树的层序遍历
# // 测试链接 : https://leetcode.cn/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        map_node_level: dict[TreeNode, int] = dict()
        queue_node: queue.Queue[TreeNode] = queue.Queue()
        ans: list[list[int]] = list(list())

        if root is not None:
            queue_node.put(root)
            map_node_level.update({root: 1})
            while not queue_node.empty():
                node: TreeNode = queue_node.get()
                if len(ans) != map_node_level.get(node):
                    ans.append([])
                ans[-1].append(node.val)

                if node.left:
                    queue_node.put(node.left)
                    # map_node_level.update({root: map_node_level.get(node) + 1})  # 很奇怪，怎么会写成root，应该是node.left
                    map_node_level.update({node.left: map_node_level.get(node) + 1})
                if node.right:
                    queue_node.put(node.right)
                    # map_node_level.update({root: map_node_level.get(node) + 1})  # 同上
                    map_node_level.update({node.right: map_node_level.get(node) + 1})

        return ans

    def levelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
        map_node_level: dict[TreeNode, int] = dict()
        queue_node: queue.Queue[TreeNode] = queue.Queue()
        ans: list[list[int]] = list()

        if root is not None:
            queue_node.put(root)
            map_node_level.update({root: 0})  # 不要忘记同步更新 map
            while not queue_node.empty():
                cur_node: TreeNode = queue_node.get()
                level = map_node_level[cur_node]
                if len(ans) == level:  # 当某一层第一个节点到这里，会进入分支新建列表，剩下的同层节点再来的时候，已经有比如 2 == 1 了，不会重复新建空列表
                    ans.append([])
                ans[level].append(cur_node.val)

                if cur_node.left:
                    queue_node.put(cur_node.left)
                    map_node_level.update({cur_node.left: level + 1})
                if cur_node.right:
                    queue_node.put(cur_node.right)
                    map_node_level.update({cur_node.right: level + 1})

        return ans

    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        max_len = 2001
        queue_node_list: list[Optional[TreeNode]] = [None] * max_len
        ans: list[list[int]] = list()

        l = r = 0
        if root is not None:
            queue_node_list[r] = root
            r += 1
            while l < r:
                cur_level_num = r - l
                cur_level_val_list = []

                for i in range(cur_level_num):
                    cur_node = queue_node_list[l]
                    cur_level_val_list.append(cur_node.val)
                    l += 1

                    if cur_node.left:
                        queue_node_list[r] = cur_node.left
                        r += 1
                    if cur_node.right:
                        queue_node_list[r] = cur_node.right
                        r += 1
                ans.append(cur_level_val_list)
        return ans
