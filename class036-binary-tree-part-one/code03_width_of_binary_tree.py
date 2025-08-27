# 给你一棵二叉树的根节点 root ，返回树的 最大宽度 。
# 树的 最大宽度 是所有层中最大的 宽度 。
# 每一层的 宽度 被定义为该层最左和最右的非空节点（即，两个端点）之间的长度。将这个二叉树视作与满二叉树结构相同，两端点间会出现一些延伸到这一层的 null 节点，这些 null 节点也计入长度。
# 题目数据保证答案将会在  32 位 带符号整数范围内。
from typing import Optional


# // 二叉树的最大特殊宽度，java版
# // 测试链接 : https://leetcode.cn/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_len = 3001
        queue_list: list[Optional[TreeNode]] = [None] * max_len
        idx_list: list[int] = [0] * max_len
        l = r = 0
        ans = 0

        if root is not None:
            queue_list[r] = root
            idx_list[r] = 1
            r += 1
            while l < r:
                cur_level_size = r - l
                ans = max(ans, idx_list[r - 1] - idx_list[l] + 1)
                for _ in range(cur_level_size):
                    cur_node = queue_list[l]
                    cur_idx = idx_list[l]
                    l += 1

                    if cur_node.left:
                        queue_list[r] = cur_node.left
                        idx_list[r] = 2 * cur_idx
                        r += 1
                    if cur_node.right:
                        queue_list[r] = cur_node.right
                        idx_list[r] = 2 * cur_idx + 1
                        r += 1  # 新增/减去元素是，一定不能忘记移动指针，尤其是当使用固定长度列表时
        return ans


# 可以参考的更简洁的写法
class SolutionRef:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans, que = 1, [(0, root)]  # 起始坐标为0，节点为根节点
        while que:
            ans = max(ans, que[-1][0] - que[0][0] + 1)
            tmp = []  # 下一轮队列
            for i, q in que:  # 坐标节点生成
                if q.left: tmp.append((i * 2, q.left))
                if q.right: tmp.append((i * 2 + 1, q.right))
            que = tmp
        return ans
