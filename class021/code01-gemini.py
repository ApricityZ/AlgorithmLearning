import sys

def merge(arr: list[int], l: int, mid: int, r: int, temp_arr: list[int]):
    """
    合并两个有序子数组 arr[l...mid] 和 arr[mid+1...r]
    """
    # 将需要合并的部分复制到辅助数组
    # temp_arr[l:r+1] = arr[l:r+1] # 也可以这样做，但下面的方式更清晰
    for i in range(l, r + 1):
        temp_arr[i] = arr[i]

    a = l
    b = mid + 1

    # 遍历主数组的当前合并区间 [l, r]，决定放入哪个元素
    for i in range(l, r + 1):
        if a > mid:  # 左半部分已用完，直接取右半部分的
            arr[i] = temp_arr[b]
            b += 1
        elif b > r:  # 右半部分已用完，直接取左半部分的
            arr[i] = temp_arr[a]
            a += 1
        elif temp_arr[a] <= temp_arr[b]: # 比较左右两部分，取较小者
            arr[i] = temp_arr[a]
            a += 1
        else:
            arr[i] = temp_arr[b]
            b += 1

# --- 递归实现 ---
def _merge_sort_recursive(arr: list[int], l: int, r: int, temp_arr: list[int]):
    """递归排序的辅助函数"""
    if l >= r:
        return
    mid = (l + r) // 2
    _merge_sort_recursive(arr, l, mid, temp_arr)
    _merge_sort_recursive(arr, mid + 1, r, temp_arr)
    # 优化：如果数组已经有序，则无需合并
    if arr[mid] > arr[mid+1]:
        merge(arr, l, mid, r, temp_arr)

def merge_sort_recursive(arr_to_sort: list[int]):
    """归并排序（递归）的入口函数"""
    n = len(arr_to_sort)
    if n <= 1:
        return
    temp_arr = [0] * n
    _merge_sort_recursive(arr_to_sort, 0, n - 1, temp_arr)

# --- 迭代实现 ---
def merge_sort_iterative(arr_to_sort: list[int]):
    """归并排序（迭代/自底向上）的入口函数"""
    n = len(arr_to_sort)
    if n <= 1:
        return
    temp_arr = [0] * n
    step = 1
    while step < n:
        l = 0
        while l < n:
            mid = l + step - 1
            # 确保 mid 和 r 不会越界
            if mid >= n - 1:
                break
            r = min(l + 2 * step - 1, n - 1)
            merge(arr_to_sort, l, mid, r, temp_arr)
            l += 2 * step
        step *= 2

def main():
    """主函数，处理输入和输出"""
    try:
        # 一次性读取所有输入并转换为数字
        inputs = list(map(int, sys.stdin.read().strip().split()))
    except (IOError, ValueError):
        return

    input_iter = iter(inputs)
    results = []

    while True:
        try:
            n = next(input_iter)
            if n == 0:
                continue

            current_arr = [next(input_iter) for _ in range(n)]

            # 创建一个副本进行排序，以防需要原始数据
            arr_to_sort = list(current_arr)

            # --- 在这里选择一种排序方式 ---
            # merge_sort_recursive(arr_to_sort)
            merge_sort_iterative(arr_to_sort)

            results.append(arr_to_sort)

        except StopIteration:
            break

    # 统一输出所有结果
    for res_arr in results:
        # 输出以空格分隔的数字，更符合常规
        sys.stdout.write(' '.join(map(str, res_arr)) + '\n')

if __name__ == '__main__':
    main()