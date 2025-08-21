# RandomizedCollection 是一种包含数字集合(可能是重复的)的数据结构。它应该支持插入和删除特定元素，以及删除随机元素。
#
# 实现 RandomizedCollection 类:
#
# RandomizedCollection()初始化空的 RandomizedCollection 对象。
# bool insert(int val) 将一个 val 项插入到集合中，即使该项已经存在。如果该项不存在，则返回 true ，否则返回 false 。
# bool remove(int val) 如果存在，从集合中移除一个 val 项。如果该项存在，则返回 true ，否则返回 false 。注意，如果 val 在集合中出现多次，我们只删除其中一个。
# int getRandom() 从当前的多个元素集合中返回一个随机元素。每个元素被返回的概率与集合中包含的相同值的数量 线性相关 。
# 您必须实现类的函数，使每个函数的 平均 时间复杂度为 O(1) 。
#
# 注意：生成测试用例时，只有在 RandomizedCollection 中 至少有一项 时，才会调用 getRandom 。


# 	// 测试链接 :
# 	// https://leetcode.cn/problems/insert-delete-getrandom-o1-duplicates-allowed/

import random


class RandomizedCollection:

    def __init__(self):
        self.arr: list[int] = list()
        self.map: dict[int, set[int]] = dict()

    def insert(self, val: int) -> bool:
        # if val in self.map:  # 允许插入重复元素，这里不能这么写
        #     return False
        ans = True
        if val in self.map:
            ans = False
        self.arr.append(val)
        # self.map.update({val: {len(self.arr) - 1}})  # 这里是不合适的，因为允许重复元素，不是第一次插入时，map中的value的下表set应保留之前的值
        # self.map.update({val: self.map.get(val, set()).add(len(self.arr) - 1)})
        self.map.setdefault(val, set()).add(len(self.arr) - 1)
        # ans = True  # 还是没看清题，逻辑有点问题，返回True or False只应该根据val是否在map中来判断， 走到这里不应该ans = True
        # return True  # 根据题意，这里不能这样写，要看清楚题目要求
        return ans

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        val_idx_set = self.map[val]
        end_val = self.arr[-1]
        deleted_idx = val_idx_set.pop()
        self.arr[deleted_idx] = end_val
        if deleted_idx != len(self.arr) - 1:  # 考虑边界条件，如果溢出的元素恰好在列表尾部
            end_val_idx_set: set = self.map[end_val]
            end_val_idx_set.remove(len(self.arr) - 1)
            end_val_idx_set.add(deleted_idx)
        self.arr.pop()  # 应该从列表中删掉最后一个元素
        if len(val_idx_set) == 0:
            del self.map[val]
        # del self.map[val] if len(val_idx_set) == 0 else None  # 不能这样写
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)

# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
param_1 = obj.insert(1)
p = obj.insert(1)
param_2 = obj.remove(1)
param_3 = obj.getRandom()
