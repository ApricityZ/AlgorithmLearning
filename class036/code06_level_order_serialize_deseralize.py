# // 二叉树按层序列化和反序列化
# // 测试链接 : https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.max_len = 10001
        self.queue: list[TreeNode | None] = [None] * self.max_len

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.ans = ''
        # if not root:
        if root:
            l = r = 0
            self.queue[r] = root
            self.ans += f'{root.val},'
            r += 1
            while l < r:
                node = self.queue[l]
                l += 1
                # self.ans += f'{node.val},'
                if node.left:
                    self.queue[r] = node.left
                    r += 1
                    self.ans += f"{node.left.val},"
                else:
                    self.ans += '#,'
                if node.right:
                    self.queue[r] = node.right
                    r += 1
                    self.ans += f"{node.right.val},"
                else:
                    self.ans += '#,'
        else:  # 空链表需要返回特殊标志
            self.ans += '#,'
        return self.ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        val_list: list[str] = data.rstrip(',').split(',')  # 虽然rstrip不影响结果，但是更准确，不去掉list最后多一个空白元素
        gene_node = lambda val: None if val == '#' else TreeNode(int(val))  # 一般来讲，传入的应该是int
        val_idx = 0
        l = r = 0

        head = gene_node(val_list[val_idx])
        val_idx += 1
        self.queue[r] = head
        r += 1

        while l < r and head:  # 增加对head为空特例的判断， 此时不能进入循环，否则会直接报错
            node = self.queue[l]
            l += 1
            node.left = gene_node(val_list[val_idx])
            val_idx += 1
            node.right = gene_node(val_list[val_idx])
            val_idx += 1
            if node.left:
                self.queue[r] = node.left
                r += 1
            if node.right:
                self.queue[r] = node.right
                r += 1
        return head

# Your Codec object will be instantiated and called as such:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))

