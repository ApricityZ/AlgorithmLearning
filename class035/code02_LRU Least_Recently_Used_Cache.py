# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

# // 测试链接 : https://leetcode.cn/problems/lru-cache/

# 思路，哈希表＋双向链表

class DoubleLinkedNode:
    def __init__(self, key: int, val: int, last_node=None, next_node=None):
        self.key = key  # 这里需要key的信息，这样在remove head node时才可以将map中的元素根据key删掉
        self.val = val
        self.last = last_node
        self.next = next_node


class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node: DoubleLinkedNode):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            # 在尾部添加
            self.tail.next = node
            node.last = self.tail
            self.tail = node

    def move_to_tail(self, node: DoubleLinkedNode):
        if node is self.tail:
            return
        if node is self.head:
            self.head = node.next
            self.head.last = None
        else:
            node.last.next = node.next
            node.next.last = node.last
        self.tail.next = node
        node.last = self.tail
        self.tail = node
        self.tail.next = None

    def remove_head(self):
        deleted_node = self.head
        if self.head is not None and self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.last = None
        return deleted_node


class LRUCache:

    def __init__(self, capacity: int):
        self.double_linked_list = DoubleLinkList()
        self.map = dict()
        self.cap = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.double_linked_list.move_to_tail(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.double_linked_list.move_to_tail(node)
        else:
            new_node = DoubleLinkedNode(key, value)  # 将key也保存在节点信息中
            self.map.update({key: new_node})
            if self.size < self.cap:
                self.double_linked_list.add(new_node)
                self.size += 1
            else:
                deleted_node = self.double_linked_list.remove_head()
                # del self.map[deleted_node.val]  # 这里应该用key啊！！！
                del self.map[deleted_node.key]
                self.double_linked_list.add(new_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
