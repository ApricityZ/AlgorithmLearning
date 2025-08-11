# -*- coding: utf-8 -*-

# 导入Python实现优先队列（堆）的模块
import heapq

# Python标准库中没有内置的TreeMap/TreeSet。
# 要实现键的自动排序和高效的范围查找，最佳实践是使用 sortedcontainers 库。
# 运行前请确保已安装: pip install sortedcontainers
from sortedcontainers import SortedDict, SortedSet

# --- TreeMap (有序字典) ---
# Java的TreeMap底层是红黑树，保证了键(key)的有序性。
# 我们使用 SortedDict 来实现相同的功能。
tree_map = SortedDict()

# .put(key, value) 对应字典的赋值操作
tree_map[5] = "这是5"
tree_map[7] = "这是7"
tree_map[1] = "这是1"
tree_map[2] = "这是2"
tree_map[3] = "这是3"
tree_map[4] = "这是4"
tree_map[8] = "这是8"

# 打印 tree_map，你会发现它是按键排序的：
# SortedDict({1: '这是1', 2: '这是2', 3: '这是3', 4: '这是4', 5: '这是5', 7: '这是7', 8: '这是8'})
print("完整的有序字典:", tree_map)

# .containsKey(key) 对应 Python 的 `in` 关键字
print(f"tree_map 中包含键 1 吗? {1 in tree_map}")
print(f"tree_map 中包含键 10 吗? {10 in tree_map}")

# .get(key) 对应字典的访问
print(f"键 4 对应的值是: {tree_map.get(4)}")

# 更新值
tree_map[4] = "张三是4"
print(f"更新后，键 4 对应的值是: {tree_map.get(4)}")

# .remove(key) 对应 `del` 关键字
del tree_map[4]
print(f"删除键 4 后，获取它的值为 None 吗? {tree_map.get(4) is None}")

# .firstKey() - 获取最小的键
# SortedDict 可以通过索引访问键，iloc[0]代表第一个(最小的)
print(f"最小的键是: {tree_map.keys()[0]}")

# .lastKey() - 获取最大的键
# iloc[-1]代表最后一个(最大的)
print(f"最大的键是: {tree_map.keys()[-1]}")


# 为了实现 floorKey 和 ceilingKey，我们可以利用 SortedDict 高效的二分查找能力
# .floorKey(key) -> 查找 <= key 的最大键
# bisect_right(key) 返回 key 在有序列表中的插入点索引，该点右边的都比key大
# 所以该索引左边的第一个元素就是 floorKey
def floor_key(sorted_dict, key):
    # bisect_right返回一个索引，所有 at[i] <= key for i < index
    index = sorted_dict.bisect_right(key)
    if index == 0:
        return None # 没有小于或等于key的键
    return sorted_dict.keys()[index - 1]

# .ceilingKey(key) -> 查找 >= key 的最小键
# bisect_left(key) 返回 key 在有序列表中的插入点索引，该点是第一个不小于key的位置
def ceiling_key(sorted_dict, key):
    # bisect_left返回一个索引，所有 at[i] < key for i < index
    index = sorted_dict.bisect_left(key)
    if index == len(sorted_dict):
        return None # 没有大于或等于key的键
    return sorted_dict.keys()[index]

print(f"小于或等于 4 的最大键是 (floorKey): {floor_key(tree_map, 4)}")
print(f"大于或等于 4 的最小键是 (ceilingKey): {ceiling_key(tree_map, 4)}")
# 在删除了4之后，小于等于4的最大键是3，大于等于4的最小键是5
print(f"大于或等于 5 的最小键是 (ceilingKey): {ceiling_key(tree_map, 5)}")


print("=" * 20)

# --- TreeSet (有序集合) ---
# Java的TreeSet对应Python的SortedSet
tree_set = SortedSet()
tree_set.add(3)
tree_set.add(3) # 重复元素不会被添加
tree_set.add(4)
tree_set.add(4)

print(f"有序集合的大小: {len(tree_set)}")

# .pollFirst() - 移除并返回第一个(最小)元素
# SortedSet 的 pop(0) 方法可以实现相同效果
print("按顺序从 SortedSet 中取出元素:")
while tree_set:
    # pop(0) 移除并返回索引为0的元素(即最小元素)
    # pop(-1) 对应 pollLast()
    print(tree_set.pop(0))

print("=" * 20)

# --- PriorityQueue (优先队列/堆) ---
# Python 的 `heapq` 模块实现了堆算法。它在一个普通的列表上工作。
# `heapq` 默认实现的是小根堆 (min-heap)。

# 1. 默认小根堆
heap1 = [] # 堆就是一个普通的列表
heapq.heappush(heap1, 3)
heapq.heappush(heap1, 1)
heapq.heappush(heap1, 2) # .add() 对应 heappush
heapq.heappush(heap1, 4)
heapq.heappush(heap1, 4)

print(f"堆的大小: {len(heap1)}")

# .poll() - 移除并返回堆顶元素 (最小值)
# 对应 heapq.heappop()
print("从小根堆中取出元素 (从小到大):")
while heap1:
    print(heapq.heappop(heap1))

print("-" * 20)

# 2. 定制大根堆 (max-heap)
# Java中通过提供一个反向比较器来实现大根堆。
# 在Python的 `heapq` 中，最巧妙和通用的方法是：
# 存入一个数的相反数，这样原本最大的数就变成了最小的负数，会浮到堆顶。
# 取出时再取一次相反数，就恢复了原来的值。
heap2 = []
heapq.heappush(heap2, -3) # 存入 3 的相反数
heapq.heappush(heap2, -3)
heapq.heappush(heap2, -4) # 存入 4 的相反数
heapq.heappush(heap2, -4)

print(f"堆的大小: {len(heap2)}")
# 此时 heap2 内部是: [-4, -4, -3, -3]

print("从大根堆中取出元素 (从大到小):")
while heap2:
    # heappop会弹出最小的元素(-4), 再取反就得到了最大的原始值(4)
    original_value = -heapq.heappop(heap2)
    print(original_value)

# 总结与关键点
# 有序容器: Python 标准库的设计哲学是保持核心功能的精简。对于像“有序字典/集合”这样更专业的数据结构，推荐使用 sortedcontainers 这样的高质量第三方库。它提供了与 Java TreeMap/TreeSet 非常接近的功能和优秀的性能。
#
# 堆 (heapq):
#
# Python 的 heapq 是一个模块，而不是一个类。它提供了一系列函数（如 heappush, heappop）来将一个普通列表（list）当作堆来操作。
#
# 它本身只支持小根堆。
#
# 实现大根堆最常用、最简洁的技巧就是存入相反数。这个技巧在算法竞赛和工程实践中都非常普遍。