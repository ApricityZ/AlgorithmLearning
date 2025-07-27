import numpy as np


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def selection_sort_wrong(arr):
    if (not arr) or len(arr) < 2:
        return
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:  # <-- 错误在这里
                min_index = j

        swap(arr, i, min_index)


def selection_sort(arr):
    if (not arr) or len(arr) < 2:
        return
    for i in range(len(arr)):
        min_index = i
        # 在 i 到 len(arr) 的范围内寻找最小值的索引
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:  # <-- 与当前最小值 arr[min_index] 比较
                min_index = j
        # 将找到的最小元素与未排序部分的第一个元素交换
        swap(arr, i, min_index)


def bubble_sort(arr):
    if (not arr) or len(arr) < 2:
        return
    for i in reversed(range(len(arr))):
        for j in range(i):
            if arr[j] > arr[j + 1]:  # 这里有j+1，故不用担心右边界
                swap(arr, j, j + 1)


def insertion_sort_wrong(arr):
    if (not arr) or len(arr) < 2:
        return
    for i in range(len(arr)):
        for j in reversed(range(i)):
            if arr[i] < arr[j]:
                swap(arr, i, j)
                # i = j
                i -= 1  # <-- 问题在这里 # 因为我们直接在arr上交换的，所以不要忘记新来的数位置交换后会变化（向左），所以要改变新来的数的索引
            else:
                continue


# ❌ 问题分析:
# 你的插入排序实现有比较大的逻辑问题，这可能也是你加上注释提醒自己的原因。
#
# 错误的比较对象: 在内层循环中，arr[i] 是本轮要插入的元素。当你执行一次 swap(arr, i, j) 后，这个要插入的元素的位置就从 i 变成了 j。但是你的代码在下一次内层循环时，依然使用 arr[i] 作为比较对象，而此时 arr[i] 已经变成了之前 arr[j] 的值。
# 代码其实能用，但晦涩、反直觉
# 修改外层循环变量: 在内层循环里修改外层循环的计数器 (i -= 1) 是一种非常危险且不规范的写法。这会严重干扰外层循环的正常流程，导致某些元素被跳过，无法正确排序。

# 结论：它为什么能工作，但为什么不推荐
# 你的代码能工作，是因为 i -= 1 这个操作，在一个 j 每次也减 1 的 reversed 循环中，恰好让变量 i 的值等于了目标元素被交换后的新索引 j。这是一种非常隐晦的逻辑。
#
# 尽管它能工作，但在软件工程中，这被认为是一种不好的实践，原因如下：
#
# 极易误解：任何有经验的程序员看到在内层循环修改与外层循环同名的变量时，第一反应都会是“这是一个 Bug”。代码首先是写给人读的，这种写法会给阅读和维护代码的人带来巨大的困惑。
#
# 逻辑不清晰：代码没有清晰地表达出它的意图。它的意图是“追踪目标元素的位置”，但代码写的却是 i -= 1。更清晰的写法应该是 i = j，因为元素被交换到了 j 的位置。你的 i -= 1 恰好能用，是因为 j 在下一次循环前也恰好是 i-1。
#
# 过于“巧合”：这段代码的正确性依赖于 Python for 循环的一些特性（它不重用被修改的循环变量，而是每次都从迭代器取新值）和你的 i 与 j 之间微妙的递减关系。这种依赖于“巧合”的代码非常脆弱，稍有改动就可能出错。
#
# 所以，你提出了一个绝佳的例子，它点明了“代码能跑出正确结果”和“代码是好代码”之间的区别。你的代码虽然能用，但它晦涩、反直觉且难以维护，因此我们仍然推荐使用前面提到的标准写法。
#
# 插入排序的核心思想是：将当前元素（arr[i]）取出，然后在它左边的已排序区间里，从后往前找到一个合适的位置把它插入。
def insertion_sort(arr):
    if (not arr) or len(arr) < 2:
        return
    # 从第二个元素开始，逐个向前插入
    for i in range(1, len(arr)):
        # j 是当前要插入的元素的索引
        j = i
        # 如果当前元素比它前面的元素小，就交换，然后继续向前比较
        while j > 0 and arr[j] < arr[j - 1]:
            swap(arr, j, j - 1)
            j -= 1  # 继续向前检查


def insertion_sort_for_loop_shifting(arr):
    if (not arr) or len(arr) < 2:
        return

    # 从第二个元素开始遍历
    for i in range(1, len(arr)):
        current_val = arr[i]
        # 记录最终要插入的位置
        insert_pos = i

        # 从 i-1 开始，倒序遍历所有已排序的元素
        for j in reversed(range(i)):
            if arr[j] > current_val:
                # 如果已排序的元素更大，则将其后移一位
                arr[j + 1] = arr[j]
                insert_pos = j  # 更新插入位置
            else:
                # 找到了不大于 current_val 的元素，说明找到了插入位置
                # 下一个位置 j+1 就是正确的位置，跳出内层循环
                break

        # 将暂存的元素放入最终找到的插入位置
        arr[insert_pos] = current_val


arr = [2, 4, 3, 1, 5, 9, 65, 1, 2, 5, 7, 3, 6, 4, 8, 10, 0]

# selection_sort(arr)
# bubble_sort(arr)
insertion_sort_wrong(arr)

print(arr)
