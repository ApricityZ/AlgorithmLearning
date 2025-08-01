from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Stack:
    def __init__(self, k=100):
        self.capacity = k
        self.arr: list[None | TreeNode] = [None] * self.capacity
        self.size = 0

    def push(self, node: TreeNode) -> None:
        self.arr[self.size] = node
        self.size += 1

    def pop(self) -> TreeNode:
        self.size -= 1
        return self.arr[self.size]

    def peek(self) -> TreeNode:
        return self.arr[self.size - 1]

    def is_empty(self) -> bool:
        return self.size == 0


class BinaryTreeTraversalIteration:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        stack = Stack()
        stack.push(root)
        results: list[int] = []
        while not stack.is_empty():
            head = stack.pop()
            results.append(head.val)
            if head.right:
                stack.push(head.right)
            if head.left:
                stack.push(head.left)
        return results

    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        stack = Stack()
        results: list[int] = []
        while (not stack.is_empty()) or root:
            if root:
                stack.push(root)
                root = root.left
            else:
                node = stack.pop()
                results.append(node.val)
                root = node.right
        return results

    def posorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        stack = Stack()
        last = root
        stack.push(root)
        results: list[int] = []
        while not stack.is_empty():
            current = stack.peek()
            if current.left and (current.left is not last) and (current.right is not last):
                stack.push(current.left)
            elif current.right and (current.right is not last):
                stack.push(current.right)
            else:
                node = stack.pop()
                results.append(node.val)
                last = node
        return results
# def posorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
#     if root is None:
#         return []
#     stack = Stack()
#     last_print_node = root
#     results: list[int] = []
#     current = root
#     while current:  # here may be an error
#         # stack.push(current)
#         if current and (current is not last_print_node.left) and (current is not last_print_node.right):
#             stack.push(current.left)
#             current = current.left
#         elif current and (current is not last_print_node.right):
#             stack.push(current)
#             current = current.right
#         else:
#             node = stack.pop()
#             results.append(node.val)
#             last_print_node = node
#             current = node.right

# %%
# 当然，这三个迭代遍历的 `while` 循环条件是算法设计的核心，理解它们是关键。我们来逐一分析。
#
# ### 1. 先序遍历 (Pre-order)
#
# * **目标：** 中 -> 左 -> 右
# * **循环条件：** `while not stack.is_empty()`
# * **逻辑解释：**
#     在先序遍历中，**栈（Stack）扮演着一个“待办事项”列表的角色**。
#     1.  我们先把根节点（第一个任务）放进栈里。
#     2.  只要这个“待办事项”列表不为空，我们就从里面拿出一个任务（`head = stack.pop()`）来处理。
#     3.  **处理（访问）** 就是把节点值加入结果列表。
#     4.  处理完当前节点后，我们把它的子任务（右孩子、左孩子）加回“待办事项”列表。因为栈是“后进先出”的，所以我们**先放右孩子，再放左孩子**，这样下次取出的就一定是左孩子。
#     5.  当所有节点和它们的子节点都被处理完后，栈自然就空了，循环结束。
#
#     所以，`while not stack.is_empty()` 的意思是：“**只要还有待处理的节点，就继续循环。**”
#
# ***
#
# ### 2. 中序遍历 (In-order)
#
# * **目标：** 左 -> 中 -> 右
# * **循环条件：** `while (not stack.is_empty()) or root:`
# * **逻辑解释：**
#     中序遍历要复杂一些，因为我们不能在第一次遇到节点时就处理它，必须先处理完它的整个左子树。
#     这里的 `while` 条件有两个部分，由 `or` 连接，意味着**满足任意一个条件循环就会继续**。
#
#     1.  **`if root:` 部分 (当 `root` 不为 `None` 时):**
#         * **任务：** 不断深入左子树，找到最左边的节点。
#         * **栈的作用：** 像导航一样，**记录我们一路向左走过的“父节点”路径**。
#         * 只要 `root` 指针指向一个有效节点，我们就把它压入栈中，然后继续往左走 (`root = root.left`)。
#
#     2.  **`else:` 部分 (当 `root` 为 `None` 时):**
#         * **任务：** 说明我们已经走到了左边的尽头，是时候处理一个节点了。
#         * 我们从栈中弹出一个节点 (`node = stack.pop()`)，这个节点就是当前应该**访问（处理）**的节点。
#         * 处理完后，我们将 `root` 指针指向这个弹出节点的右孩子 (`root = node.right`)，准备对它的右子树重复上述过程。
#
#     **为什么需要 `or root`?**
#     * **启动循环：** 一开始栈是空的，但 `root` 不是 `None`，`or root` 确保循环可以开始。
#     * **处理右子树：** 当我们处理完一个节点（比如节点 `A`）并转向它的右子树时，有可能此时栈是空的（如果 `A` 是根节点）。但它的右子树还需要处理，`or root` 确保循环能为这个右子树继续下去。
#
#     循环的终止条件是：**当栈为空（所有父节点都已处理）并且 `root` 也为 `None`（刚刚处理完最右节点的右孩子）时**，表示整棵树都遍历完毕。
#
# ***
#
# ### 3. 后序遍历 (Post-order)
#
# * **目标：** 左 -> 右 -> 中
# * **循环条件：** `while not stack.is_empty()`
# * **逻辑解释：**
#     后序遍历是最复杂的，因为一个节点必须在它的左、右孩子都处理完毕后才能被处理。
#
#     1.  **栈的作用：** 同样是**记录当前的访问路径**。
#     2.  **`last` 变量是关键：** 它用来记录**上一个被访问（处理并加入结果列表）的节点**。通过比较 `current` (栈顶节点) 和 `last`，我们可以判断出我们是从左子树返回，还是从右子树返回，从而决定下一步的行动。
#         * `current.left is not last` 和 `current.right is not last` 的判断，就是为了防止在处理完一个节点的子节点后，回来又重复进入同一个子节点，造成死循环。
#     3.  **循环逻辑：** 只要栈不为空，就说明路径上还有节点没有被彻底处理（它自己或它的右子树）。
#         * 我们查看 (`peek`) 栈顶节点 `current`。
#         * 先尝试去它的左子树（如果左子树存在且没被访问过）。
#         * 如果左边走不通，再尝试去右子树（如果右子树存在且没被访问过）。
#         * 如果左、右都走不通（说明它们都已被访问或不存在），这时才能**处理（访问）** `current` 节点自己，然后更新 `last` 记录。
#
#     这个循环的条件和先序遍历一样，因为栈都代表着“待处理的路径/节点”。不同之处在于，后序遍历在决定是否可以 `pop` 和处理一个节点时，有更复杂的内部判断逻辑。循环的结束条件很简单：**当路径上所有节点都按后序规则处理完毕后，栈为空，循环结束。**
#
# ### 总结 📝
#
# | 遍历顺序 | 循环条件 | 核心思想 |
# | :--- | :--- | :--- |
# | **先序 (Pre-order)** | `while not stack.is_empty()` | 栈是“待办事项”列表。取出就处理，再把子任务加回去。 |
# | **中序 (In-order)** | `while stack or root` | 栈是“返回路径”。一路向左，到头后返回处理，再转向右边。`or root` 保证了启动和右子树的处理。 |
# | **后序 (Post-order)**| `while not stack.is_empty()` | 栈是“访问路径”。用 `last` 变量辅助判断，确保左右孩子都处理完后，才处理根节点。 |当然，这三个迭代遍历的 `while` 循环条件是算法设计的核心，理解它们是关键。我们来逐一分析。
#
# ### 1. 先序遍历 (Pre-order)
#
# * **目标：** 中 -> 左 -> 右
# * **循环条件：** `while not stack.is_empty()`
# * **逻辑解释：**
#     在先序遍历中，**栈（Stack）扮演着一个“待办事项”列表的角色**。
#     1.  我们先把根节点（第一个任务）放进栈里。
#     2.  只要这个“待办事项”列表不为空，我们就从里面拿出一个任务（`head = stack.pop()`）来处理。
#     3.  **处理（访问）** 就是把节点值加入结果列表。
#     4.  处理完当前节点后，我们把它的子任务（右孩子、左孩子）加回“待办事项”列表。因为栈是“后进先出”的，所以我们**先放右孩子，再放左孩子**，这样下次取出的就一定是左孩子。
#     5.  当所有节点和它们的子节点都被处理完后，栈自然就空了，循环结束。
#
#     所以，`while not stack.is_empty()` 的意思是：“**只要还有待处理的节点，就继续循环。**”
#
# ***
#
# ### 2. 中序遍历 (In-order)
#
# * **目标：** 左 -> 中 -> 右
# * **循环条件：** `while (not stack.is_empty()) or root:`
# * **逻辑解释：**
#     中序遍历要复杂一些，因为我们不能在第一次遇到节点时就处理它，必须先处理完它的整个左子树。
#     这里的 `while` 条件有两个部分，由 `or` 连接，意味着**满足任意一个条件循环就会继续**。
#
#     1.  **`if root:` 部分 (当 `root` 不为 `None` 时):**
#         * **任务：** 不断深入左子树，找到最左边的节点。
#         * **栈的作用：** 像导航一样，**记录我们一路向左走过的“父节点”路径**。
#         * 只要 `root` 指针指向一个有效节点，我们就把它压入栈中，然后继续往左走 (`root = root.left`)。
#
#     2.  **`else:` 部分 (当 `root` 为 `None` 时):**
#         * **任务：** 说明我们已经走到了左边的尽头，是时候处理一个节点了。
#         * 我们从栈中弹出一个节点 (`node = stack.pop()`)，这个节点就是当前应该**访问（处理）**的节点。
#         * 处理完后，我们将 `root` 指针指向这个弹出节点的右孩子 (`root = node.right`)，准备对它的右子树重复上述过程。
#
#     **为什么需要 `or root`?**
#     * **启动循环：** 一开始栈是空的，但 `root` 不是 `None`，`or root` 确保循环可以开始。
#     * **处理右子树：** 当我们处理完一个节点（比如节点 `A`）并转向它的右子树时，有可能此时栈是空的（如果 `A` 是根节点）。但它的右子树还需要处理，`or root` 确保循环能为这个右子树继续下去。
#
#     循环的终止条件是：**当栈为空（所有父节点都已处理）并且 `root` 也为 `None`（刚刚处理完最右节点的右孩子）时**，表示整棵树都遍历完毕。
#
# ***
#
# ### 3. 后序遍历 (Post-order)
#
# * **目标：** 左 -> 右 -> 中
# * **循环条件：** `while not stack.is_empty()`
# * **逻辑解释：**
#     后序遍历是最复杂的，因为一个节点必须在它的左、右孩子都处理完毕后才能被处理。
#
#     1.  **栈的作用：** 同样是**记录当前的访问路径**。
#     2.  **`last` 变量是关键：** 它用来记录**上一个被访问（处理并加入结果列表）的节点**。通过比较 `current` (栈顶节点) 和 `last`，我们可以判断出我们是从左子树返回，还是从右子树返回，从而决定下一步的行动。
#         * `current.left is not last` 和 `current.right is not last` 的判断，就是为了防止在处理完一个节点的子节点后，回来又重复进入同一个子节点，造成死循环。
#     3.  **循环逻辑：** 只要栈不为空，就说明路径上还有节点没有被彻底处理（它自己或它的右子树）。
#         * 我们查看 (`peek`) 栈顶节点 `current`。
#         * 先尝试去它的左子树（如果左子树存在且没被访问过）。
#         * 如果左边走不通，再尝试去右子树（如果右子树存在且没被访问过）。
#         * 如果左、右都走不通（说明它们都已被访问或不存在），这时才能**处理（访问）** `current` 节点自己，然后更新 `last` 记录。
#
#     这个循环的条件和先序遍历一样，因为栈都代表着“待处理的路径/节点”。不同之处在于，后序遍历在决定是否可以 `pop` 和处理一个节点时，有更复杂的内部判断逻辑。循环的结束条件很简单：**当路径上所有节点都按后序规则处理完毕后，栈为空，循环结束。**
#
# ### 总结 📝
#
# | 遍历顺序 | 循环条件 | 核心思想 |
# | :--- | :--- | :--- |
# | **先序 (Pre-order)** | `while not stack.is_empty()` | 栈是“待办事项”列表。取出就处理，再把子任务加回去。 |
# | **中序 (In-order)** | `while stack or root` | 栈是“返回路径”。一路向左，到头后返回处理，再转向右边。`or root` 保证了启动和右子树的处理。 |
# | **后序 (Post-order)**| `while not stack.is_empty()` | 栈是“访问路径”。用 `last` 变量辅助判断，确保左右孩子都处理完后，才处理根节点。 |