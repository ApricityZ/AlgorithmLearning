class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """定义单链表及其操作"""

    def __init__(self):
        self.head: Node | None = None  # 链表头节点

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def append(self, data):
        """在链表尾部添加新节点"""
        new_node = Node(data)
        if self.is_empty():
            # 如果是空链表，新节点就是头节点
            self.head = new_node
        else:
            # 否则，遍历到链表末尾
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        """在链表头部添加新节点"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """删除指定数据的节点"""
        if self.is_empty():
            print("Error: Linked list is empty.")
            return

        # 如果头节点就是要删除的节点
        if self.head.data == data:
            self.head = self.head.next
            return

        # 查找要删除的节点
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:
            # 找到了，将前一个节点的next指向被删除的节点的下一个节点
            current.next = current.next.next

        else:
            print(f"Error: Node with data '{data}' not found.")

    def search(self, data):
        """查找节点并返回"""
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None  # 未找到

    def display(self):
        """打印整个链表"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + ' -> None')

    def reverse(self):
        pre = None
        while self.head is not None:
            next_node = self.head.next
            self.head.next = pre
            pre = self.head
            self.head = next_node
        self.head = pre


def reversed(head: Node):
    pre = None
    next = None
    while head is not None:
        next = head.next
        head.next = pre
        # pre = head.next  # 这里有问题，pre应该指向head，head.next已经指向pre
        pre = head
        head = next
    return pre


sll = SinglyLinkedList()

sll.append(10)
sll.append(20)
sll.append(30)
sll.display()

sll.prepend(5)
sll.display()

sll.delete(20)
sll.display()

sll.delete(99)

node = sll.search(10)
if node:
    print(f"Found node with data: {node.data}")

print('Print the origin linked list')
sll.display()

sll.reverse()
print('Print the reversed linked list')
sll.display()


# ======== 双链表实现 ========

class DoublyNode:
    """定义双链表节点"""

    def __init__(self, data):
        self.data = data
        self.next = None  # 指向后一个节点
        self.prev = None  # 指向前一个节点


class DoublyLinkedList:
    """定义双链表及其操作"""

    def __init__(self):
        self.head: DoublyNode | None = None
        self.tail: DoublyNode | None = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def append(self, data):
        """在链表尾部添加新节点(O(1)时间复杂度)"""
        new_node = DoublyNode(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        """在链表头部添加新节点"""
        new_node = DoublyNode(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        """删除指定数据的节点"""
        current = self.head
        # 遍历查找要删除的节点
        while current and current.data != data:
            current = current.next

        if current is None:
            print(f"Error: Node with data '{data} not found.")
            return

        # 如果要删除的不是头节点
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

        # 如果要删除的不是尾节点
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

    def display(self):
        """从头到尾打印整个链表"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print("None <- " + " <-> ".join(elements) + " -> None")

    def display_reverse(self):
        """从尾到头打印整个链表"""
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        print("None <- " + ' <-> '.join(elements) + ' -> None')

    def search(self, data):
        """查找节点并返回"""
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def reverse(self):
        """反转双向链表 (修复版)"""
        pre = None
        current = self.head

        # 原来的头节点将成为新的尾节点
        self.tail = current

        while current:
            # 保存原始的下一个节点，这是我们前进的“路标”
            next_node = current.next

            # 交换 prev 和 next 指针
            current.next = pre
            current.prev = next_node

            # 移动指针，为下一次循环做准备
            pre = current
            current = next_node  # 使用保存好的“路标”前进，而不是被修改过的 current.next

        # 循环结束后，pre 指向了原来的尾节点，它现在是新的头节点
        self.head = pre

    def reverse1(self):
        """反转双向链表的另一种写法"""
        current = self.head

        while current:
            current.prev, current.next = current.next, current.prev

            current = current.prev

        self.head, self.tail = self.tail, self.head


dll = DoublyLinkedList()

print('\n===Doubly Linked List ===\n')
dll.append(10)
dll.append(20)
dll.append(30)
dll.display()

dll.prepend(5)
dll.display()
dll.display_reverse()

node = dll.search(10)
if node:
    print(f"Found node with data: {node.data}")

node = dll.search(15)
if node:
    print(f"Found node with data: {node.data}")

print('===反转链表===')
dll.reverse()
dll.display()
dll.display_reverse()

dll.reverse1()
dll.display()
dll.display_reverse()
print('===反转链表结束===')

dll.delete(15)

dll.delete(20)
dll.display()

dll.delete(5)
dll.display()

dll.delete(30)
dll.display()
print(f"Head {dll.head.data}, Tail: {dll.tail.data}")
