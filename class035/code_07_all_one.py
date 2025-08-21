# 请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。
#
# 实现 AllOne 类：
#
# AllOne() 初始化数据结构的对象。
# inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。
# dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key 从数据结构中删除。测试用例保证：在减少计数前，key 存在于数据结构中。
# getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。
# getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。
# 注意：每个函数都应当满足 O(1) 平均时间复杂度。

# https://leetcode.cn/problems/all-oone-data-structure/

# from __future__ import annotations # 在oj平台，怀疑提交代码上面会有其他代码或导入，故这里会报错，因为该导入必须放在首行


# class DoubleLinkBucket:
#     def __init__(self, count: int, last_node: DoubleLinkBucket = None,
#                  next_node: DoubleLinkBucket = None):
#         self.count: int = count
#         self.str_key_set: set[str] = set()
#         self.last: DoubleLinkBucket = last_node
#         self.next: DoubleLinkBucket = next_node

class DoubleLinkBucket:
    def __init__(self, count: int, last_node=None, next_node=None):
        self.count: int = count
        self.str_key_set: set[str] = set()
        self.last: DoubleLinkBucket = last_node
        self.next: DoubleLinkBucket = next_node


class AllOne:

    def __init__(self):
        self.map_val_bucket: dict[str, DoubleLinkBucket] = dict()
        self.head: DoubleLinkBucket = DoubleLinkBucket(0)
        self.tail: DoubleLinkBucket = DoubleLinkBucket(2 ** 23 - 1)
        self.head.next = self.tail  # 这两个要在初始化的时候连起来，否则开始判断这个self.head.next会报错None没有next属性
        self.tail.last = self.head

    @staticmethod
    def insert_new_bucket(cur_bucket: DoubleLinkBucket, new_bucket: DoubleLinkBucket) -> None:
        # 将新建的桶插入到当前桶后面
        cur_bucket.next.last = new_bucket
        new_bucket.next = cur_bucket.next
        new_bucket.last = cur_bucket
        cur_bucket.next = new_bucket

    @staticmethod
    def delete_cur_bucket(to_delete_bucket: DoubleLinkBucket) -> None:
        to_delete_bucket.next.last = to_delete_bucket.last
        to_delete_bucket.last.next = to_delete_bucket.next
        del to_delete_bucket

    def inc(self, key: str) -> None:
        if key in self.map_val_bucket:  # 如果key存在与map中，那么说明这个key肯定有对应的链表节点，那么此时就需要判断是否需要在链表中删除移除元素后为空的节点，
            # 但是由于是inc，所以在map中这个值肯定会存在下去，频率不会为0
            bucket = self.map_val_bucket[key]
            cur_count = bucket.count
            if bucket.next.count == cur_count + 1:
                bucket.next.str_key_set.add(key)
                self.map_val_bucket.update({key: bucket.next})
                bucket.str_key_set.remove(key)
                # if len(bucket.str_key_set) == 0:
                #     self.delete_cur_bucket(bucket)
            else:
                new_bucket: DoubleLinkBucket = DoubleLinkBucket(cur_count + 1)
                new_bucket.str_key_set.add(key)
                self.insert_new_bucket(bucket, new_bucket)
                self.map_val_bucket.update({key: new_bucket})
                bucket.str_key_set.remove(key)
            if len(bucket.str_key_set) == 0:
                self.delete_cur_bucket(bucket)
        else:
            if self.head.next.count == 1:
                bucket = self.head.next
                bucket.str_key_set.add(key)
                self.map_val_bucket.update({key: self.head.next})
            else:
                new_bucket: DoubleLinkBucket = DoubleLinkBucket(1)
                new_bucket.str_key_set.add(key)
                self.insert_new_bucket(self.head, new_bucket)
                self.map_val_bucket.update({key: new_bucket})

    def dec(self, key: str) -> None:
        key_bucket: DoubleLinkBucket = self.map_val_bucket[key]
        if key_bucket.count == 1:
            del self.map_val_bucket[key]
            key_bucket.str_key_set.remove(key)
        else:
            if key_bucket.last.count == key_bucket.count - 1:
                key_bucket.last.str_key_set.add(key)
                self.map_val_bucket.update({key: key_bucket.last})
                key_bucket.str_key_set.remove(key)
            else:
                new_bucket: DoubleLinkBucket = DoubleLinkBucket(key_bucket.count - 1)
                new_bucket.str_key_set.add(key)
                self.insert_new_bucket(key_bucket.last,
                                       new_bucket)  # 注意，这是插入词频小的，应该插入在key_bucket前面，所以函数形参应该是key_bucket.last
                self.map_val_bucket.update({key: new_bucket})
                key_bucket.str_key_set.remove(key)

        if len(key_bucket.str_key_set) == 0:
            self.delete_cur_bucket(key_bucket)

    def getMaxKey(self) -> str:
        if self.tail.last is self.head:
            return ""
        return next(iter(self.tail.last.str_key_set))  # 为空的时候会报错，所以一眼需要添加条件判断

    def getMinKey(self) -> str:
        if self.head.next is self.tail:
            return ""
        return next(iter(self.head.next.str_key_set))


# 总结：

# 当inc时，如果key存在与map中，说明链表中一定存在节点存储该key，那么我们就需要找出现有节点，将该节点的set中的key移除，并根据移除后set是否为0，
# 来决定是否从链表中删除该节点；因为时inc，所以该元素词频不会为0，那么一定有对应的链表节点， map中该元素也一定不需要被删除

# 当dec时，key一定存在与map中了，那么链表中一定会有对应的节点，不管哪种情况，我们都需要找到当前节点并从该节点的set中删除掉这个元素，然后根据
# 移除后的set size是否为0， 决定是否从链表中删除该节点；同时，由于此时可能会有key的词频为0，那么在链表中就不存在相应的节点存储该可key，此时
# 我们需要根据该key所在的桶的词频是否为1，来决定是否从map中删除该元素


# Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc("hello")
obj.inc("hello")
ans1 = obj.getMaxKey()
ans2 = obj.getMinKey()
obj.inc("leet")
ans3 = obj.getMaxKey()
ans4 = obj.getMinKey()
