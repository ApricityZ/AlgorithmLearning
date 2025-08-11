# -*- coding: utf-8 -*-
# 在Python中，我们不需要像Java一样声明包名(package)或导入基础数据结构。
# set 和 dict (字典) 都是Python的内置类型，可以直接使用。

def main():
    """
    主函数，对应Java中的 public static void main(String[] args)
    """

    # --- 字符串(String)与哈希集合(HashSet) ---
    # 在Java中，`new String("Hello")` 会在堆内存中创建新的对象。
    # Python的字符串处理机制有所不同，对于短字符串，它有一个“驻留”机制(interning)，
    # 可能会让多个相同值的字符串变量指向同一个内存地址，但这并非绝对保证。
    str1 = "Hello"
    str2 = "Hello"

    # Java中的 `==` 比较的是内存地址。在Python中，对应的操作是 `is`。
    # CPython(官方Python解释器)对短字符串的优化，可能导致下面的结果为True。
    # 为了更清晰地说明问题，我们关注值的比较。
    print(f"str1 is str2: {str1 is str2}")  # 比较内存地址，结果依赖于Python的实现细节

    # Java中的 `.equals()` 比较的是内容。在Python中，对应的操作是 `==`。
    # 这会调用对象的 __eq__() 方法。
    print(f"str1 == str2: {str1 == str2}")  # 比较值，结果总是True

    # Java的 HashSet 对应 Python 的 set
    # set 是一个无序且不含重复元素的集合。
    set_example = set()

    # set.add(element) - 添加元素
    set_example.add(str1)

    # 检查元素是否存在。在Python中，使用 `in` 关键字，更自然易读。
    # 因为 "Hello" 的值与 str1 的值相同，所以返回 True
    print(f"'Hello' in set_example: {'Hello' in set_example}")
    # 因为 str2 的值也与 "Hello" 相同，set是基于值的哈希来判断成员资格的。
    print(f"str2 in set_example: {str2 in set_example}")

    # 尝试添加一个等值的元素 str2
    # 因为set中已经存在一个值为 "Hello" 的元素，所以集合不会有任何变化。
    set_example.add(str2)

    # len(set) - 获取集合大小，对应Java的 .size()
    print(f"Size of set: {len(set_example)}")

    # set.remove(element) - 删除元素
    set_example.remove(str1)

    # set.clear() - 清空集合
    set_example.clear()

    # 判断集合是否为空。可以直接判断集合的布尔值，空集合为False。
    print(f"Is set empty? {not set_example}")

    print("=" * 20)

    # --- 哈希映射(HashMap) ---
    # Java的 HashMap 对应 Python 的 dict (字典)
    # dict 是一种键(key)-值(value)对的无序集合 (在Python 3.7+版本中，dict变为有序)
    map1 = {}  # 或者 map1 = dict()

    # .put(key, value) 对应 Python 的字典赋值操作
    map1[str1] = "World"

    # .containsKey(key) 对应 Python 的 `in` 关键字
    print(f"'Hello' in map1: {'Hello' in map1}")
    # 同样，字典的键也是基于值的哈希
    print(f"str2 in map1: {str2 in map1}")

    # .get(key) 对应 Python 的字典访问
    # 使用 .get() 方法的好处是，如果键不存在，它会返回 None (或指定的默认值)，而不会报错。
    print(f"Value for str2: {map1.get(str2)}")
    print(f"Value for '你好' is None: {map1.get('你好') is None}")

    # .remove(key) 对应 Python 的 `del` 关键字
    del map1["Hello"]

    # len(dict) - 获取字典大小
    print(f"Size of map1: {len(map1)}")

    # .clear() - 清空字典
    map1.clear()

    # 判断字典是否为空
    print(f"Is map1 empty? {not map1}")

    print("=" * 20)

    # --- 用列表(数组)替代哈希表 ---
    # Java代码中提到，在特定场景下（键是范围可控的非负整数），可以用数组替代哈希表。
    # 这种技巧在Python中同样适用，我们用列表(list)来模拟数组。
    # 这是一种“空间换时间”的策略。

    # 假设key的最大值不会超过99
    # 初始化一个长度为100，所有元素都为None的列表
    array_as_map = [None] * 100

    array_as_map[56] = 7285
    array_as_map[34] = 3671263
    array_as_map[17] = 716311
    array_as_map[24] = 1263161

    # 增、删、改、查的操作变成了直接的索引操作，时间复杂度为 O(1)。
    # 但前提是：
    # 1. key必须是整数。
    # 2. key的范围不能太大，否则会浪费大量内存空间。
    print("在特定场景下，Python的列表(list)也可以像数组一样替代字典。")
    print(f"array_as_map[34] = {array_as_map[34]}")

    print("=" * 20)

    # --- 自定义对象作为哈希表的键 ---
    # 这是非常关键的一个知识点。
    # 默认情况下，Python的自定义对象是“可哈希的(hashable)”，
    # 其哈希值基于对象的内存地址(id())，其相等性比较(==)也是基于内存地址。

    class StudentDefault:
        """
        一个没有重写 __eq__ 和 __hash__ 方法的学生类。
        它的哈希行为将基于对象的内存地址。
        """

        def __init__(self, age, name):
            self.age = age
            self.name = name

    s1_default = StudentDefault(17, "张三")
    s2_default = StudentDefault(17, "张三")

    print(f"s1_default is s2_default: {s1_default is s2_default}")  # False, 不同对象，不同地址
    print(f"s1_default == s2_default: {s1_default == s2_default}")  # False, 默认的==比较也是比较地址

    map_default = {}
    map_default[s1_default] = "这是张三"

    # 因为 s2_default 和 s1_default 是两个不同的对象(内存地址不同)，
    # 所以它们的哈希值也不同。因此，Python认为它们是两个不同的键。
    print(f"s1_default in map_default: {s1_default in map_default}")  # True
    print(f"s2_default in map_default: {s2_default in map_default}")  # False

    map_default[s2_default] = "这是另一个张三"
    print(f"Size of map_default: {len(map_default)}")  # 结果是 2
    print(f"Value for s1_default: {map_default.get(s1_default)}")
    print(f"Value for s2_default: {map_default.get(s2_default)}")

    print("-" * 10 + " 正确的实现 " + "-" * 10)

    # 要想让Python把“值相同”的对象视为“同一个键”，
    # 我们必须实现 __eq__ 和 __hash__ 这两个方法。
    # 规则：
    # 1. 如果 a == b 为真，那么 hash(a) == hash(b) 也必须为真。
    # 2. __eq__ 方法定义了 `==` 操作符的行为。
    # 3. __hash__ 方法定义了 `hash()` 函数的行为。

    class Student:
        """
        一个正确实现了 __eq__ 和 __hash__ 的学生类。
        现在它的哈希行为将基于对象的内容（age 和 name）。
        """

        def __init__(self, age, name):
            self.age = age
            self.name = name

        # 定义 "==" 如何工作
        def __eq__(self, other):
            # 首先检查是不是Student类的实例
            if isinstance(other, Student):
                return self.age == other.age and self.name == other.name
            return False

        # 定义 hash(self) 如何工作
        def __hash__(self):
            # 通常，我们会用一个元组(tuple)来包含所有用于比较的属性，
            # 然后对这个元组求哈希值。因为元组是不可变的，所以它是可哈希的。
            return hash((self.age, self.name))

        # 这个方法不是必须的，但可以让打印对象时更清晰
        def __repr__(self):
            return f"Student(age={self.age}, name='{self.name}')"

    s1 = Student(17, "张三")
    s2 = Student(17, "张三")

    print(f"s1 is s2: {s1 is s2}")  # False, 仍然是不同对象
    print(f"s1 == s2: {s1 == s2}")  # True, 因为我们重写了 __eq__!
    print(f"hash(s1) == hash(s2): {hash(s1) == hash(s2)}")  # True, 因为我们重写了 __hash__!

    map3 = {}
    map3[s1] = "这是张三"

    # 现在，因为 s1 == s2 并且 hash(s1) == hash(s2)，
    # Python会将 s2 视为与 s1 相同的键。
    print(f"s1 in map3: {s1 in map3}")  # True
    print(f"s2 in map3: {s2 in map3}")  # True, 这就是我们想要的结果！

    # 当用 s2 作为键来赋值时，它会覆盖掉以 s1 为键的值。
    map3[s2] = "这是另一个张三"
    print(f"Size of map3: {len(map3)}")  # 结果是 1

    # 用 s1 或 s2 去获取值，都会得到最后更新的那个值。
    print(f"Value for s1: {map3.get(s1)}")
    print(f"Value for s2: {map3.get(s2)}")
    print(s2)


# 这是Python中推荐的执行入口
# if __name__ == "__main__":
#     main()

# 总结与关键点
# 核心数据结构：Java的 HashSet 和 HashMap 直接对应于Python的内置类型 set 和 dict，使用起来更简洁。
#
# 相等性判断：
#
# Java == (比较地址)  <==> Python is
#
# Java .equals() (比较内容) <==> Python ==
#
# 自定义对象作键 (The Key Takeaway)：
#
# 目标：我们希望哈希表（无论是 set 还是 dict）能够根据对象的内容（属性值），而不是内存地址，来判断两个对象是否“相等”。
#
# Java实现：重写 hashCode() 和 equals() 方法。
#
# Python实现：实现 __hash__() 和 __eq__() 特殊方法。
#
# 黄金法则：必须保证，如果两个对象通过 __eq__ (或 equals) 判断是相等的，那么它们的 __hash__ (或 hashCode) 值也必须相等。这是哈希表能够正常工作的基本契约。
#
# 希望这份详细的转换和解释能帮助你更好地理解哈希表、set、map 在不同语言中的实现原理和应用。

main()

print('=' * 20)


class CollisionKey:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        # 让打印更清晰
        return f"Key({self.data})"

    def __hash__(self):
        # 故意让所有实例的哈希值都是一个常量，比如 42
        # 这会强制把所有 CollisionKey 实例都发往同一个“桶”
        return 42

    def __eq__(self, other):
        # 精确比较是基于 data 属性
        if not isinstance(other, CollisionKey):
            return False
        return self.data == other.data


# 创建两个实例
# 它们的值不同，所以它们不相等 (k1 == k2 是 False)
# 但它们的哈希值相同 (hash(k1) == hash(k2) 是 True)
k1 = CollisionKey("Hamlet")
k2 = CollisionKey("Macbeth")

print(f"k1 == k2: {k1 == k2}")
print(f"hash(k1) == hash(k2): {hash(k1) == hash(k2)}")
print("-" * 20)

my_dict = {}

# 存入第一个键
my_dict[k1] = "A great tragedy"
print("存入 k1后: ", my_dict)
print("字典大小: ", len(my_dict))
print("-" * 20)

# 存入第二个键
my_dict[k2] = "Another great tragedy"
print("存入 k2后: ", my_dict)
print("字典大小: ", len(my_dict))  # 注意看大小的变化
print("-" * 20)

# 我们可以成功地分别获取它们的值
print(f"获取 k1 的值: {my_dict[k1]}")
print(f"获取 k2 的值: {my_dict[k2]}")

# 从输出可以清晰地看到，尽管 k1 和 k2 的哈希值相同，但因为它们通过 == 判断不相等，所以它们作为两个独立的键被成功存入了字典，字典的大小变成了2，没有发生任何覆盖。
#
# 总结
# 覆盖 的前提是 逻辑相等 (== 为 True)。
#
# 哈希冲突 (hash 相等但 == 为 False) 是哈希表的正常工作状态之一。
#
# 哈希表通过将冲突的键值对以链表（或其他形式）存储在同一个桶中来解决冲突。
#
# 这带来的唯一影响是性能上的：如果一个桶里的冲突元素太多，查找这个桶里的元素时就会从 O(1) 退化成 O(N)（N是桶内元素个数），因为需要逐个进行 == 比较。但其逻辑正确性不受影响。
