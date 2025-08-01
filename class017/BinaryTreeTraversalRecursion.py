# TreeNode 类保持不变，非常标准
class TreeNode:
    """二叉树节点类"""

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTreeTraversalRecursion:

    def __init__(self):
        self.pre_order_elements = []
        self.mid_order_elements = []
        self.pos_order_elements = []

    def pre_order(self, head: TreeNode, is_firest_call=True):
        if head is None:
            return
        if not is_firest_call:  # 不够优雅，下面的不改了
            print('-', end='')
        print(head.val, end='')
        self.pre_order(head.left, is_firest_call=False)
        self.pre_order(head.right, is_firest_call=False)

    def mid_order(self, head: TreeNode):
        if head is None:
            return
        self.mid_order(head.left)
        print(head.val, end='-')
        self.mid_order(head.right)

    def pos_order(self, head: TreeNode):
        if head is None:
            return
        self.pos_order(head.left)
        self.pos_order(head.right)
        print(head.val, end='-')

    def recursion(self, head: TreeNode):
        if head is None:
            return
        # 第一次到达head节点（输入参数的节点，递归过程中是不断变化的，实参不断变化）
        self.recursion(head.left)
        # 左孩子总会遍历结束，来到这里，第二次经过head节点
        self.recursion(head.right)
        # 遍历完右孩子，返回到这里，第三次经过head节点
        # 解释器再往下走没代码了，那么整个函数运行结束，所以每个节点都会来三次。
        # 这个输入参数，总是可以认为是一个树/子树的头节点（即中间节点，左中右的中），
        # 那么如果第一次到达节点就打印，相当于是：中->左->右，即为先序遍历
        # 那么如果第二次到达节点才打印，相当于是：左->中->右，即为中序遍历
        # 那么如果第三次到达节点才打印，相当于是：左->右->中，即为后续遍历
        # 当然，上面的 左 中 右 三个的顺序只是相对顺序，未必是相邻的

    # 所以基于上面，你可以用一个函数包含三种遍历
    def uni_order(self, head: TreeNode):
        if head is None:
            return
        self.pre_order_elements.append(head.val)
        self.uni_order(head.left)
        self.mid_order_elements.append(head.val)
        self.uni_order(head.right)
        self.pos_order_elements.append(head.val)

    def get_three_orders(self):
        if self.pre_order_elements and self.mid_order_elements and self.pos_order_elements:
            return self.pos_order_elements, self.mid_order_elements, self.pre_order_elements
        else:
            print("The uni_order function haven't called, no ordered elements to show")
            return None, None, None


def print_bin_tree(order_ele):
    print(f"{'-'.join(map(str, order_ele))}")


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
head.right.left = TreeNode(6)
head.right.right = TreeNode(7)

Traversal_orders = BinaryTreeTraversalRecursion()
print("\npre order:")
Traversal_orders.pre_order(head)
print("\nmid order:")
Traversal_orders.mid_order(head)
print("\npos order")
Traversal_orders.pos_order(head)
print("\nunify order")
Traversal_orders.uni_order(head)
pre, mid, pos = Traversal_orders.get_three_orders()
print_bin_tree(pre)
print_bin_tree(mid)
print_bin_tree(pos)


# 1. 代码存在的问题与优化点
# 问题 1: 函数职责不单一
# 原始的 pre_order, mid_order, pos_order 函数混合了两个职责：遍历计算和结果打印 (print(head.val, end='-'))。这降低了代码的可重用性。
# 如果其他地方需要的是遍历结果的列表（list）而不是直接打印，这三个函数就无法满足需求。
# 优化建议：让函数只负责一件事。遍历函数应该返回一个包含遍历结果的列表。打印操作应该由调用者来完成。
# 问题 2: 状态管理
# BinaryTreeTraversalRecursion 类通过实例变量（self.pre_order_elements 等）来存储遍历结果。这导致该类的实例是有状态的。
# 潜在风险：如果在同一个实例上对不同的树或者多次调用 uni_order，结果会不断累加到列表中，导致结果错误。
# Python
# # 示例：错误的使用方式
# traverser = BinaryTreeTraversalRecursion()
# traverser.uni_order(tree1) # 列表被填充
# traverser.uni_order(tree2) # 结果会追加到上一次的结果后面，而不是覆盖
# 优化建议：让遍历方法成为无状态的。方法接受一个树的根节点作为输入，并返回遍历结果，而不是修改实例的状态。这样，同一个实例可以被安全地重复使用。
# 问题 3: print_bin_tree 函数的 Bug
# 您的 print_bin_tree 函数尝试对一个整数列表（order_ele）使用 join 方法：'-'.join(order_ele)。join 方法要求列表中的元素必须是
# 字符串（str），因此这里会触发 TypeError。
# 优化建议：在 join 之前，需要将列表中的所有整数转换为字符串。
# 问题 4: get_three_orders 的返回值顺序
# 您在 get_three_orders 中返回的顺序是 pos_order_elements, mid_order_elements, pre_order_elements，但在主程序中接收时，
# 变量命名是 pre, mid, pos，这会导致变量名与实际内容不匹配。
# 优化建议：调整返回顺序，使其与通用的“先、中、后”序习惯保持一致。

# =================================================

class BinaryTreeTraversal:
    """
    一个更健壮和可重用的二叉树遍历类。
    方法是无状态的，它们接收一个根节点并返回结果列表。
    """

    # 方案A：为每种遍历提供独立的、返回列表的方法
    def pre_order(self, root: TreeNode) -> list[int]:
        """先序遍历，返回结果列表"""
        result = []
        self._pre_order_recursive(root, result)
        return result

    def _pre_order_recursive(self, node: TreeNode, result: list[int]):
        if node is None:
            return
        result.append(node.val)
        self._pre_order_recursive(node.left, result)
        self._pre_order_recursive(node.right, result)

    def in_order(self, root: TreeNode) -> list[int]:
        """中序遍历，返回结果列表"""
        result = []
        self._in_order_recursive(root, result)
        return result

    def _in_order_recursive(self, node: TreeNode, result: list[int]):
        if node is None:
            return
        self._in_order_recursive(node.left, result)
        result.append(node.val)
        self._in_order_recursive(node.right, result)

    def post_order(self, root: TreeNode) -> list[int]:
        """后序遍历，返回结果列表"""
        result = []
        self._post_order_recursive(root, result)
        return result

    def _post_order_recursive(self, node: TreeNode, result: list[int]):
        if node is None:
            return
        self._post_order_recursive(node.left, result)
        self._post_order_recursive(node.right, result)
        result.append(node.val)

    # 方案B：保留您的一次性遍历思路，但使其无状态
    def get_all_orders(self, root: TreeNode) -> tuple[list[int], list[int], list[int]]:
        """
        通过一次递归遍历，同时获取先序、中序、后序遍历的结果。
        返回一个包含三个列表的元组 (pre_order, in_order, post_order)。
        """
        pre_order_elements = []
        in_order_elements = []
        post_order_elements = []

        def _uni_order_recursive(node: TreeNode):
            if node is None:
                return

            # 第一次访问节点：先序
            pre_order_elements.append(node.val)
            _uni_order_recursive(node.left)

            # 第二次访问节点：中序
            in_order_elements.append(node.val)
            _uni_order_recursive(node.right)

            # 第三次访问节点：后序
            post_order_elements.append(node.val)

        _uni_order_recursive(root)
        return pre_order_elements, in_order_elements, post_order_elements


def print_tree_traversal(name: str, elements: list[int]):
    """
    一个更健壮的打印函数，可以正确处理整数列表。
    """
    if not elements:
        print(f"{name}: []")
        return
    # 将列表中的每个元素（可能是int）转换为str，然后再join
    formatted_string = " -> ".join(map(str, elements))
    print(f"{name}: {formatted_string}")


# --- 主程序测试 ---
# 1. 创建树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# 2. 创建遍历器实例
traverser = BinaryTreeTraversal()

# 3. 使用独立的遍历方法 (方案A)
print("--- 使用独立遍历方法 (方案 A) ---")
pre_order_list = traverser.pre_order(root)
print_tree_traversal("Pre-order", pre_order_list)

in_order_list = traverser.in_order(root)
print_tree_traversal("In-order", in_order_list)

post_order_list = traverser.post_order(root)
print_tree_traversal("Post-order", post_order_list)

print("\n" + "=" * 40 + "\n")

# 4. 使用统一的遍历方法 (方案B)
print("--- 使用统一遍历方法 (方案 B) ---")
pre, mid, pos = traverser.get_all_orders(root)
print_tree_traversal("Unified Pre-order", pre)
print_tree_traversal("Unified In-order", mid)
print_tree_traversal("Unified Post-order", pos)
