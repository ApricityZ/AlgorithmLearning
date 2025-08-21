# 实现RandomizedSet 类：
#
# RandomizedSet() 初始化 RandomizedSet 对象
# bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
# bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
# int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
# 你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。
import random


# 	// 测试链接 : https://leetcode.cn/problems/insert-delete-getrandom-o1/
class RandomizedSet:

    def __init__(self):
        self.map = dict()
        self.arr = list()

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map.update({val: len(self.arr)})
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        val_idx = self.map[val]
        end_val = self.arr[-1]
        self.arr[val_idx] = end_val
        self.map.update({end_val: val_idx})
        del self.arr[-1]
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
