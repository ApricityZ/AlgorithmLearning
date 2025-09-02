# // 用递归函数排序栈
# // 栈只提供push、pop、isEmpty三个方法
# // 请完成无序栈的排序，要求排完序之后，从栈顶到栈底从小到大
# // 只能使用栈提供的push、pop、isEmpty三个方法、以及递归函数
# // 除此之外不能使用任何的容器，数组也不行
# // 就是排序过程中只能用：
# // 1) 栈提供的push、pop、isEmpty三个方法
# // 2) 递归函数，并且返回值最多为单个整数
import random
from queue import LifoQueue


class SortStack:
    def sort(self, stack: LifoQueue[int]):
        """主逻辑函数"""
        stack_deep = self.deep(stack)
        while stack_deep > 0:
            max_val = self.find_max(stack, stack_deep)
            times = self.count_max(stack, stack_deep, max_val)
            self.down_max(stack, stack_deep, max_val, times)
            stack_deep -= times
        return stack

    def deep(self, stack: LifoQueue[int]) -> int:
        """返回栈的深度"""
        if stack.qsize() == 0:
            return 0
        num = stack.get()
        res_deep = self.deep(stack) + 1
        stack.put(num)  # 可以认为是恢复现场
        return res_deep

    def find_max(self, stack: LifoQueue[int], deep: int) -> int:
        """从栈顶向内查找deep个元素的最大值并返回"""
        # if stack.qsize() == 0:  # base case 不能以 stack.qsize() == 0 判断，因为我们这个函数是从 从栈顶往下 deep 个元素内工作的，否则变成了全局范围。
        if deep == 0:
            return -2 ** 31
        num = stack.get()
        max_val = max(self.find_max(stack, deep - 1), num)
        stack.put(num)
        return max_val  # 这一层的调用返回是为了给上一层使用

    def count_max(self, stack: LifoQueue[int], deep: int, max_val: int) -> int:
        """从栈顶向下查找deep个数，统计max_val的个数"""
        if deep == 0:
            return 0
        num = stack.get()
        counts = 0
        counts += 1 if num == max_val else 0
        counts += self.count_max(stack, deep - 1, max_val)
        stack.put(num)
        return counts

    def down_max(self, stack: LifoQueue[int], deep: int, max_val: int, k) -> None:
        """在从栈顶deep个数字内，将出现 k 次的最大值 max_val 放到 deep 的最下方（连续放置）"""
        if deep == 0:
            for i in range(k):
                stack.put(max_val)
        else:
            num = stack.get()
            self.down_max(stack, deep - 1, max_val, k)
            if num != max_val:
                stack.put(num)


def generate_random_stack(num, max_val):
    stack = LifoQueue()
    for _ in range(num):
        stack.put(random.randint(0, max_val + 1))
    return stack


def validate_sort(stack: LifoQueue[int]) -> bool:
    num = -2 ** 31
    while stack.qsize() > 0:
        if num > stack.queue[-1]:
            return False
        num = stack.get()
    return True


def test(num, max_val):
    sort_stack = SortStack()
    return validate_sort(sort_stack.sort(generate_random_stack(num, max_val)))


def main():
    stack = LifoQueue()
    stack.put(1)
    stack.put(4)
    stack.put(2)
    stack.put(7)
    stack.put(3)

    sort_stack = SortStack().sort(stack)
    print(sort_stack.queue)

    max_num = 100
    max_value = 1000
    test_times = 1000
    for _ in range(test_times):
        if not test(random.randint(1, max_num), random.randint(0, max_value)):
            print("Error occurred!")
    print("Test Finished!")


if __name__ == '__main__':
    main()
