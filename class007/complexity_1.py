import time
import numpy as np

def generate_special_array(n, v):
    """
    随机生成长度为n, 值在0~v-1之间, 且相邻两数不相等的数组
    """
    if v <= 1 and n > 1:
        raise ValueError("当v<=1时，无法生成相邻不相等的数组")

    arr = np.zeros(n, dtype=int)
    arr[0] = np.random.randint(v)
    for i in range(1, n):
        # 拒绝采样：如果生成的和前一个相同，则重新生成
        # 这是一个简单实现，但在v很小时效率不高
        arr[i] = np.random.randint(v)
        while arr[i] == arr[i - 1]:
            arr[i] = np.random.randint(v)
    return arr

def bubble_sort(arr):
    """
    优化的冒泡排序实现
    - 使用双层for循环，可读性好
    - 交换使用Pythonic的元组解包
    - 增加提前退出的标志
    """
    if not isinstance(arr, list) or len(arr) < 2:
        return

    n = len(arr)
    for end in range(n - 1, 0, -1):
        is_sorted = True
        for i in range(end):
            if arr[i] > arr[i + 1]:
                # Pythonic swap
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
        if is_sorted:
            # 如果一轮下来没有发生交换，则数组已有序
            break

def time_it(name, func, *args):
    """
    一个高阶函数，用于为其他函数计时并打印结果
    """
    print(f'=== {name} 测试开始 ===')
    start_time = time.time()
    func(*args)
    end_time = time.time()
    print(f'--- {name} 测试结束, 耗时: {end_time - start_time:.4f} 秒 ---')

def run_n_log_n_test(N):
    """O(N log N) 复杂度的测试函数"""
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            pass

def run_n_square_test(N):
    """O(N^2) 复杂度的测试函数"""
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            pass

def main():
    """
    主函数，用于演示各个功能
    """
    # 1. 演示生成特殊数组
    print("--- 1. 演示生成特殊数组 ---")
    arr1 = generate_special_array(n=10, v=4)
    print(f"生成的数组: {' '.join(map(str, arr1))}")
    print('=' * 20)

    # 2. 演示Python的list (动态数组)
    print("\n--- 2. 演示Python list ---")
    arr2 = [5, 4, 9]
    arr2.append(100)
    arr2[1] = 6 # 修改
    print(f"List内容: {arr2}")
    print('=' * 20)

    # 3. 演示冒泡排序
    print("\n--- 3. 演示冒泡排序 ---")
    arr_to_sort = [64, 31, 78, 0, 5, 7, 103, -5]
    print(f"排序前: {arr_to_sort}")
    bubble_sort(arr_to_sort)
    print(f"排序后: {arr_to_sort}")
    print('=' * 20)

    # 4. 性能测试
    print("\n--- 4. 性能测试 ---")
    N = 2000
    time_it("O(N log N)", run_n_log_n_test, N)

    # N=200000对于O(N^2)太大了，会运行非常久，这里使用一个较小的值来演示
    N_small = 2000
    time_it("O(N^2)", run_n_square_test, N_small)
    print('=' * 20)


if __name__ == "__main__":
    main()