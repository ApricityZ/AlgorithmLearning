class DLinkedNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyCircularDeque:
    def __init__(self, k):
        self.head = None
        self.rear = None
        self.size = 0
        self.capacity = k

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        node = DLinkedNode(value)
        if self.isEmpty():
            self.head = node
            self.rear = node
        else:
            next_node = self.head
            self.head = node
            node.next = next_node
            next_node.prev = self.head
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        node = DLinkedNode(value)
        if self.isEmpty():
            self.head = node
            self.rear = node
        else:
            prev_node = self.rear
            self.rear = node
            prev_node.next = self.rear
            node.prev = prev_node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        delete_node = self.head
        self.head = delete_node.next
        delete_node.next = None
        self.size -= 1

        if self.isEmpty():
            self.rear = None
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        delete_node = self.rear
        self.rear = delete_node.prev
        delete_node.prev = None
        self.size -= 1

        if self.isEmpty():
            self.head = None
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.head.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self.rear.val


class MyCircularDeque1:
    def __init__(self, k):
        self.capacity = k
        self.arr = [None] * self.capacity
        self.head = 0
        self.rear = 0
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def insertFront(self, val: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = self.rear = 0
            self.arr[self.head] = val
        else:
            self.head = (self.head - 1 + self.capacity) % self.capacity
            self.arr[self.head] = val
        self.size += 1
        return True

    def insertLast(self, val: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.head = self.rear = 0
            self.arr[self.rear] = val
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.arr[self.rear] = val
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False

        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1

        return self.arr[self.head]

    def getRear(self):
        if self.isEmpty():
            return -1

        return self.arr[self.rear]


# 双端队列的实现不同于单端队列，由于单端队列始终是从尾部添加，从头部弹出，所以尾部指针总是在头部之后的后面（循环情况下逻辑上的右边），所以呢，这点不同的
# 体现在于：1）不能简单舍弃self.size 参数，在不牺牲一个存储位置的情况下，通过self.head == self.rear来判断是否为空，是因为我们的
# 头尾指针都指向队列的第一个和最后一个元素，如果添加的话，就必须先移动，再放数据， 这就必须要求区分空队列的情况，如果插入时队列为空，我们将head和rear指针都设置为零，保持相对位置
# 在不牺牲一个存储位置的情况下， 同时我们就会出现head == rear的情况，这是，必须引入额外的参数size来判断是否为满/空。
# size 参数是否必要，取决于 head == rear 这个状态是否存在歧义。而我们恰好可以通过改变 rear 指针的定义来消除这种歧义，从而摆脱对 size 参数的依赖。

# 在(为了解决歧义而)增加一个元素的情况下，rear必须指向队尾下一个元素
# head 和 rear 指向头尾元素和指向头元素为元素下一个的影响，在不额外消耗一个存储空间，并且使用size参数的情况的区别是：push时能否同意空/非空时的索引变化逻辑是否统一。
# 如果希望不适用size参数，就需要引入额外的一个空间，并且必须分开指向，head指向头元素，rear指向尾元素的下一个位置（反着也可以吧

# 代码可优化之处
# 你的 insertFront 和 insertLast 中，处理空队列的逻辑其实可以和通用逻辑合并。思考一下：
#
# 当队列为空时，self.size 是 0，self.head 和 self.rear 都是 0。
#
# insertFront: self.head 会变成 (0 - 1 + capacity) % capacity，即 capacity - 1。然后 self.arr[capacity - 1] = val。
# 同时 self.rear 保持为 0。下一次 insertLast 时，self.rear 会变成 1。这样 head 和 rear 指针就不再是同一个位置了。
#
# insertLast: self.rear 会变成 (0 + 1) % capacity，即 1。self.head 保持为 0。
#
# 咦，这样好像不对？如果第一次 insertFront，head 跑到 capacity - 1，而 rear 还是 0，此时 getRear() 会返回 arr[0] 的初始值 None。
#
# 所以，你对空队列的特殊处理是必要的！ 当插入第一个元素时，head 和 rear 必须指向同一个位置。你的实现 self.head = self.rear = 0 保证了这一点。
#
# 另一种不需要特殊处理空队列的实现方式是调整指针的定义：
#
# head 指向队头元素。
#
# rear 指向队尾元素的 下一个 位置。
#
# 采用这种定义后，判空和判满的条件会改变，但插入和删除的逻辑可以更统一。不过，你目前的实现方式更直观，也完全正确。
#
# 好的，我们来重新梳理和总结一下这两种循环双端队列的实现方法及其核心思想。
#
# ---
#
# ### 核心结论
#
# 实现一个基于数组的循环双端队列，主要有两种主流的设计思路，它们的核心区别在于**如何判断队列的“空”和“满”**。
#
# 1.  **方法一：使用 `size` 变量追踪状态 (你的 `MyCircularDeque1`)**
# 2.  **方法二：牺牲一个存储空间，仅用指针位置判断状态 (`MyCircularDeque2`)**
#
# 这两种方法都是完全正确的，只是在空间利用率和代码优雅性之间做了不同的**权衡 (Trade-off)**。
#
# ---
#
# ### 方法一：`size` 变量法
#
# 这是你最初的实现，非常直观。
#
# * **指针定义**:
#     * `head` 指向 **队头元素**。
#     * `rear` 指向 **队尾元素**。
#
# * **状态判断**:
#     * **判空**: `self.size == 0`
#     * **判满**: `self.size == self.capacity`
#
# * **优点**:
#     * **空间利用率100%**: 分配 `k` 个空间，就能存储 `k` 个元素。
#     * **逻辑直观**: `size` 变量直接反映了元素数量，简单明了。
#
# * **缺点**:
#     * **逻辑需要分支**: 由于 `head` 和 `rear` 指针都指向实际元素，在队列为空时插入第一个元素，需要特殊处理来同时设定 `head` 和 `rear` 的初始位置。这导致插入操作的代码有 `if self.isEmpty()` 的分支。
#
# ---
#
# ### 方法二：牺牲空间法 (教科书式)
#
# 这是我们后面讨论的实现，逻辑上更统一。
#
# * **指针定义**:
#     * `head` 指向 **队头元素**。
#     * `rear` 指向 **队尾元素的下一个位置**。
#
# * **状态判断**:
#     * **判空**: `self.head == self.rear`
#     * **判满**: `(self.rear + 1) % self.capacity == self.head`
#     * **注意**: 为了能存 `k` 个元素，内部数组大小必须是 `k + 1`。
#
# * **优点**:
#     * **代码逻辑统一优雅**: 无论队列是否为空，插入和删除操作的指针移动算法完全相同，无需特殊分支判断，代码更简洁。
#
# * **缺点**:
#     * **牺牲存储空间**: 永远有一个数组单元是闲置的，不能用来存储数据。
#
# ---
#
# ### 两者对比速查表
#
# | 特性 | 方法一 (size变量法) | 方法二 (牺牲空间法) |
# | :--- | :--- | :--- |
# | **核心机制** | 用 `size` 变量记录元素个数 | 用指针的相对位置区分状态 |
# | **指针含义** | `head`->队头, `rear`->队尾 | `head`->队头, `rear`->队尾的**下一位** |
# | **空间效率** | **高** (100% 利用) | **低** (浪费一个单元) |
# | **代码优雅性** | 一般 (有特殊分支) | **高** (逻辑统一) |
# | **实现难度** | 较低，符合直觉 | 稍高，需理解指针和判满条件 |
#
# ### 最终思考：为什么会有这两种方法？
#
# 根本原因在于：当 `head` 和 `rear` 指针都指向**实际元素**时，`head == rear` 这个状态本身具有**二义性**——它既可能代表“队列为空”，也可能代表“队列中只有一个元素”。
#
# * **方法一** 的思路是：既然有二义性，那我就引入一个局外裁判 `self.size`，由它来告诉我准确的状态。
# * **方法二** 的思路是：我要从规则上彻底消灭二义性。通过修改 `rear` 的定义并牺牲一个格子，我创造了一套新规则，在这套规则里 `head == rear` **只可能**代表“队列为空”，从而不再需要 `size` 变量。
#
# 理解这两种方法的内在逻辑和它们各自的权衡，就代表你已经完全掌握了循环双端队列的精髓。


class MyCircularDeque2:
    def __init__(self, k):
        self.capacity = k + 1
        self.arr = [None] * self.capacity
        self.head = 0
        self.rear = 0

    def isEmpty(self):
        return self.rear == self.head

    def isFull(self):
        return ((self.head - 1) % self.capacity) == self.rear

    def insertFront(self, val: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head - 1 + self.capacity) % self.capacity
        self.arr[self.head] = val
        return True

    def insertLast(self, val: int) -> bool:
        if self.isFull():
            return False

        self.arr[self.rear] = val
        self.rear = (self.rear + 1) % self.capacity

        return True

    def deleteFront(self):
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % self.capacity
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False

        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return True

    def getFront(self):
        if self.isEmpty():
            return -1

        return self.arr[self.head]

    def getRear(self):
        if self.isEmpty():
            return -1

        return self.arr[(self.rear - 1 + self.capacity) % self.capacity]


class MyCircularDeque3:
    """
    第二种实现方式：
    - head 指向队头元素
    - rear 指向队尾元素的下一个位置
    - 牺牲一个存储空间来区分队满和队空
    """

    def __init__(self, k: int):
        # 为了能存储 k 个元素，我们需要 k+1 的容量
        # 因为 (rear + 1) % capacity == head 时即为满
        self.capacity = k + 1
        self.arr = [None] * self.capacity
        self.head = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        """从队头插入一个元素。如果操作成功返回 true。"""
        if self.isFull():
            return False

        # head 指针向前移动一位，然后在此位置插入新元素
        self.head = (self.head - 1 + self.capacity) % self.capacity
        self.arr[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        """从队尾插入一个元素。如果操作成功返回 true。"""
        if self.isFull():
            return False

        # rear 指向的就是下一个可插入的位置，直接插入
        self.arr[self.rear] = value
        # rear 指针向后移动一位
        self.rear = (self.rear + 1) % self.capacity
        return True

    def deleteFront(self) -> bool:
        """从队头删除一个元素。如果操作成功返回 true。"""
        if self.isEmpty():
            return False

        # head 指向的就是要删除的元素，直接将其后移一位即可
        self.head = (self.head + 1) % self.capacity
        return True

    def deleteLast(self) -> bool:
        """从队尾删除一个元素。如果操作成功返回 true。"""
        if self.isEmpty():
            return False

        # rear 指向队尾元素的下一个位置，所以将 rear 回退一位即可
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return True

    def getFront(self) -> int:
        """从队头获取元素。如果队列为空，返回 -1。"""
        if self.isEmpty():
            return -1
        # head 指向的就是队头元素
        return self.arr[self.head]

    def getRear(self) -> int:
        """获取队尾元素。如果队列为空，返回 -1。"""
        if self.isEmpty():
            return -1
        # 队尾元素在 rear 指针的前一个位置
        rear_element_index = (self.rear - 1 + self.capacity) % self.capacity
        return self.arr[rear_element_index]

    def isEmpty(self) -> bool:
        """检查双端队列是否为空。"""
        return self.head == self.rear

    def isFull(self) -> bool:
        """检查双端队列是否已满。"""
        return (self.rear + 1) % self.capacity == self.head

# 这是一个非常好的探究性问题！它正好打在了我们之前讨论的核心上。
#
# 直接的答案是：在“`rear`指向队尾元素”这个规则下，如果不使用`size`参数，也**不引入任何其他形式的约定或“花招”**，那么是**不可能**实现的。
#
# 因为我们会陷入一个无法靠指针自身解决的“状态歧义”的死胡同里。
#
# ---
#
# ### 让我们来尝试一下（并看看为什么会失败）
#
# 假设我们有：
# * 一个容量为 `k` 的数组。
# * `head` 指针指向队头元素。
# * `rear` 指针指向队尾元素。
# * **没有 `size` 变量。**
#
# 我们的任务是，仅通过 `head` 和 `rear` 的位置，要能准确判断队列的三种基本状态：**空**、**满**、**非空非满**。
#
# #### 核心冲突点
#
# 我们来分析两个最容易混淆的状态：
#
# 1.  **队列只有一个元素时：**
#     假设我们在索引 `i` 处插入一个元素。根据定义，这个元素既是队头也是队尾。所以，必然有 `head = i` 并且 `rear = i`。
#     结论：当队列只有一个元素时，**必然 `head == rear`**。
#
# 2.  **队列为空时：**
#     现在我们需要给“空队列”定义一个指针状态。我们能用什么状态呢？
#     * **尝试定义 `head == rear` 为空？** 这直接就和“只有一个元素”的情况冲突了。计算机看到 `head == rear`，完全不知道是该返回元素还是说队列为空。**此路不通。**
#     * **尝试定义一个特殊值，比如 `head = -1` 为空？**
#         * 这可以工作，但它本质上就是引入了一个**新的状态约定**，类似于 `size` 或布尔标志位。我们不再是“仅通过指针位置”来判断了。
#         * 而且它会增加代码的复杂度。每次插入第一个元素时，都需要把 `head` 和 `rear` 从 `-1` 改为某个有效索引。每次删除最后一个元素时，又需要把它们改回 `-1`。
#
# #### “满”状态的加入让情况更糟
#
# 现在我们再考虑“满”的状态。
#
# * 一个容量为 `k` 的队列满了，意味着 `k` 个槽位都被占了。
# * 比如 `k=5`，元素在 `0, 1, 2, 3, 4`。此时 `head=0`, `rear=4`。
# * `head` 和 `rear` 的关系是 `(head + k - 1) % k == rear`。
#
# 现在想象一下，你无法找到任何一个仅靠 `head` 和 `rear` 的数学关系（例如 `head==rear`, `(rear+1)%k == head` 等）来为“空”状态保留一个唯一的位置。任何你试图为“空”或“满”定义的关系，都可能在经过一系列的入队和出队操作后，被一个“非空非满”的队列状态所复现。
#
# ---
#
# ### 结论
#
# 在 **`rear` 指向队尾元素** 这个最直观的设计下，指针本身携带的信息不足以覆盖队列的所有状态（空、满、各种中间状态）。`head == rear` 的含义太模糊，导致我们必须引入一个“局外信息”来打破僵局。
#
# 这个“局外信息”最干净、最直接的选择就是 `size` 变量。
#
# 所以，我们可以得到一个非常明确的结论：
#
# | 设计选择 | 能否不使用 `size` 变量？ |
# | :--- | :--- |
# | **rear 指向队尾元素** | **不能** (除非引入其他同样效果的复杂约定) |
# | **rear 指向队尾下一位** | **可以** (通过牺牲一个存储空间来消除歧义) |
#
# 你提出的这个问题，实际上完美地反向证明了：为什么“`rear` 指向队尾下一位”这种看起来有些不自然的设计会成为一种经典方案。因为它正是为了解决你在这种情况下会遇到的“无解”困局而发明的。
