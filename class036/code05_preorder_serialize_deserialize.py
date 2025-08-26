# // 二叉树先序序列化和反序列化
# // 测试链接 : https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.ans = ''
        def _serialize(root: TreeNode):
            if root is None:
                self.ans += '#,'
            else:
                self.ans += f'{root.val},'
                _serialize(root.left)
                _serialize(root.right)

        # return _serialize(root)  # 应该先运行函数，然后返回 self.ans
        _serialize(root)
        return self.ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        node_val: list = data.split(',')
        self.cnt = 0

        def _deserialize(val_list=None):
            val = val_list[self.cnt]
            self.cnt += 1
            if val == '#':
                return None
            head = TreeNode(int(val))  # 一般来讲，传入的应该是int
            head.left = _deserialize(val_list)
            head.right = _deserialize(val_list)
            return head

        return _deserialize(node_val)

# Your Codec object will be instantiated and called as such:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
