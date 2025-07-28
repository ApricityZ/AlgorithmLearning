import time

import numpy as np


# 研究时间复杂度

class Complexity:
    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    def bubble_sort(self, arr):
        # 用一个 while 循环和两个状态变量 (i 和 end) 成功模拟了传统双层 for 循环的行为：
        # end 变量扮演了外层循环的角色，标记每一轮“冒泡”的终点。每完成一轮，end 就减一。
        # i 变量扮演了内层循环的角色，作为比较指针在 [0, end-1] 的范围内移动。
        # if i < end - 1 这个条件判断就相当于内层循环的继续。
        # else 分支则代表内层循环的结束，此时重置 i=0 并让 end 减一，进入下一轮。

        if arr is None or len(arr) < 2:
            return
        n = len(arr)
        end = n - 1
        i = 0
        while end > 0:
            if arr[i] > arr[i + 1]:
                self.swap(arr, i, i + 1)
            if i < end - 1:
                i += 1
            else:
                end -= 1
                i = 0

    def main(self):
        # 随机生成长度为n
        # 值在0 ~ v-1之间
        # 并且相邻任意两数不相等的数组
        n = 10
        v = 4
        arr1 = np.zeros(n)
        arr1[0] = np.random.randint(v)
        for i in range(1, n):
            while arr1[i] == arr1[i - 1]:
                arr1[i] = np.random.randint(v)
        for num in arr1:
            print(f'{num} ')
        print()
        print('=======')

        # python 中的动态数组是 list
        # 各个语言中的动态数组的初始大小和实际扩容银子可能会变化，但均摊都是O(1)
        # 课上用2作为扩容银子知识举例而已
        arr2 = list()
        arr2.append(5)
        arr2.append(4)
        arr2.append(9)
        arr2[1] = 6
        print(arr2[1])
        print('=======')

        arr = [64, 31, 78, 0, 5, 7, 103]
        self.bubble_sort(arr)
        for num in arr:
            print(f'{num} ')
        print()
        print('=======')

        N: int = 200000
        print('===test starts===')
        start_time = time.time()
        for i in range(1, N + 1):
            for j in range(i, N + 1, i):
                pass
        end_time = time.time()
        print(f"test end, duration: {end_time - start_time} ")

        print('===test start===')
        start_time = time.time()
        for i in range(1, N + 1):
            for j in range(i, N + 1):
                pass
        end_time = time.time()
        print(f'test ended, duration: {end_time - start_time}')

    def __call__(self, *args, **kwargs):
        self.main()


complexity = Complexity()
complexity()
