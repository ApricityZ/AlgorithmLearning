# -*- coding: utf-8 -*-
import functools
from sortedcontainers import SortedSet, SortedList

class Employee:
    """
    对应Java的Employee类。
    在Python中，我们通常会实现 __init__ 和 __repr__ 方法。
    __repr__ 方法能让我们在打印对象时获得一个清晰的、可读的表示。
    """
    def __init__(self, company, age):
        self.company = company
        self.age = age

    def __repr__(self):
        return f"Employee(company={self.company}, age={self.age})"

# Java中的`EmployeeComparator`是一个实现了Comparator接口的类。
# 在Python中，我们通常不创建单独的比较器类，而是直接在需要的地方
# 使用一个函数（通常是lambda表达式）作为`key`参数。
# `key`函数的作用是：为列表中的每个元素生成一个用于比较的“键”。
# Python会根据这些生成的“键”来进行排序。

def main():
    s1 = Employee(2, 27)
    s2 = Employee(1, 60)
    s3 = Employee(4, 19)
    s4 = Employee(3, 23)
    s5 = Employee(1, 35)
    s6 = Employee(3, 55)

    # 原始数组
    arr = [s1, s2, s3, s4, s5, s6]
    print("原始数组:", arr)

    # --- 1. 列表排序 (对应 Arrays.sort) ---

    # 案例一：按年龄升序排序
    # Java: Arrays.sort(arr, new EmployeeComparator());
    # Python: 使用 `list.sort()` 方法的 `key` 参数。
    # `lambda e: e.age` 的意思是：“对于列表中的每一个元素e，使用它的age属性作为排序的键”。
    arr.sort(key=lambda e: e.age)
    print("\n按年龄升序排序:")
    for e in arr:
        print(e)

    print("=" * 20)

    # 案例二：按年龄降序排序
    # Java: Arrays.sort(arr, (a, b) -> b.age - a.age);
    # Python: 在使用 `key` 的基础上，将 `reverse` 参数设为 True。
    arr.sort(key=lambda e: e.age, reverse=True)
    print("按年龄降序排序:")
    for e in arr:
        print(e)

    print("=" * 20)

    # 案例三：多级排序
    # 需求：先按公司编号升序，如果公司编号相同，再按年龄升序。
    # Java: Arrays.sort(arr, (a, b) -> a.company != b.company ? (a.company - b.company) : (a.age - b.age));
    # Python: 让 `key` 函数返回一个元组 (tuple)！
    # Python会按元组的元素顺序逐级比较，这非常优雅和强大。
    # (a.company, a.age) vs (b.company, b.age)
    arr.sort(key=lambda e: (e.company, e.age))
    print("按公司、再按年龄升序排序:")
    for e in arr:
        print(e)

    print("=" * 20)

    # --- 2. 有序集合与去重逻辑 (对应 TreeSet) ---

    # 场景一：TreeSet根据比较器去重
    # Java: TreeSet<Employee> treeSet1 = new TreeSet<>(new EmployeeComparator()); (按年龄比较)
    # Python: SortedSet同样可以使用一个key函数来决定排序和“唯一性”。
    # SortedSet 的 key 参数只负责排序。它告诉内部的 SortedList 如何排列元素。
    # SortedSet 的去重（唯一性）由被添加对象本身的 __eq__ 和 __hash__ 方法决定。这是由其内部的 set 组件决定的。
    tree_set1 = SortedSet(key=lambda e: e.age)

    original_arr = [s1, s2, s3, s4, s5, s6]
    for e in original_arr:
        tree_set1.add(e)

    # 由于s1(age=27), s4(age=23), s5(age=35)等的年龄都不同，都能加进去
    # 但是，如果两个员工年龄相同，后一个就加不进去
    print(f"原始数组大小: {len(original_arr)}")
    print(f"按年龄排序的SortedSet大小: {len(tree_set1)}")
    print(tree_set1)


    tree_set1.add(Employee(2, 27)) # 公司是99，但年龄是27
    print(f"添加一个age=27的新员工后的大小: {len(tree_set1)}")
    print(tree_set1)

    print("=" * 20)

    # 场景二：如何保留重复元素？
    # Java中通过构造一个极其复杂的比较器，确保只有对象地址相同时才返回0。
    # 这在实践中是一种反模式（anti-pattern）。
    # Python的哲学是：如果你需要一个允许重复元素的有序集合，那么你应该用正确的工具。
    # `set`的定义就是不重复，强行让它重复是不对的。正确的工具是 `SortedList`。

    print("使用 SortedList 来实现允许重复的有序集合:")
    # 使用和多级排序一样的key
    sorted_list = SortedList(key=lambda e: (e.company, e.age, id(e)))

    for e in original_arr:
        sorted_list.add(e)

    print(f"SortedList 的大小: {len(sorted_list)}")

    # 尝试添加一个和 s1 内容完全相同的员工
    # 因为 SortedList 允许重复，所以这次添加会成功！
    sorted_list.add(Employee(2, 27))
    print(f"添加一个重复员工后，SortedList 的大小: {len(sorted_list)}")
    print("SortedList 内容:")
    for e in sorted_list:
        print(e)

    print("=" * 20)

    # --- 3. 其他 ---

    # 关于 PriorityQueue (heapq)
    # Java的PriorityQueue和Python的heapq都不会去重，它们只保证每次弹出的元素是最小/最大的。
    # 如果多个元素的优先级相同，它们都会被存入堆中。
    print("注：Python的 heapq 模块 (优先队列) 也不会去重。")

    # 字符串的字典序比较
    # Java: str1.compareTo(str2) 返回一个整数
    # Python: 直接使用比较运算符，返回布尔值
    str1 = "abcde"
    str2 = "ks"
    print(f"在Python中，'{str1}' < '{str2}' 的结果是: {str1 < str2}")
    print(f"在Python中，'{str2}' < '{str1}' 的结果是: {str2 < str1}")
    arr1 = [str1, str2]
    arr1.sort()
    print(arr1)


if __name__ == "__main__":
    main()