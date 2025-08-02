import sys

# ------------------------------------------------------------------
# Static Space Allocation (using module-level global variables)
# ------------------------------------------------------------------
# This is the Python equivalent of Java's static variables.
# We pre-allocate space to avoid creating new lists for each test case.

MAXN = 201
MAXM = 201

# Pre-allocate the matrix and the auxiliary array
mat = [[0] * MAXM for _ in range(MAXN)]
arr = [0] * MAXM

# Global variables to hold the dimensions of the current test case
# These correspond to the static n and m in the Java code.
n, m = 0, 0


# ------------------------------------------------------------------
# Core Algorithm (using global variables)
# ------------------------------------------------------------------

def max_sum_subarray() -> int:
    """
    求一维数组的最大子数组和 (Kadane's 算法)。
    This function uses the global `arr` and `m` variables,
    so it does not need any parameters.
    """
    max_val = -float('inf')
    cur_sum = 0
    # Loop up to the current column count `m`
    for i in range(m):
        cur_sum += arr[i]
        max_val = max(max_val, cur_sum)
        cur_sum = 0 if cur_sum < 0 else cur_sum
    return max_val


def max_sum_submatrix() -> int:
    """
    计算子矩阵最大累加和的核心逻辑。
    This function uses the global `mat`, `arr`, `n`, and `m` variables.
    """
    max_global = -float('inf')

    # Loop up to the current row count `n`
    for i in range(n):
        # IMPORTANT: Reset the reusable auxiliary array `arr`.
        # This is the equivalent of Java's `Arrays.fill(arr, 0, m, 0)`.
        # We only need to clear the part we are using, which is up to `m`.
        for k in range(m):
            arr[k] = 0

        for j in range(i, n):
            # Accumulate values into the compressed array `arr`
            for k in range(m):
                arr[k] += mat[j][k]

            # Find the max subarray sum from the compressed array
            max_global = max(max_global, max_sum_subarray())

    return max_global


# ------------------------------------------------------------------
# ACM 模式的主程序入口
# ------------------------------------------------------------------

def main():
    """
    Main function to handle I/O, similar to Java's `public static void main`.
    """
    # We must use the `global` keyword to modify the module-level n and m
    global n, m

    # Process all input lines at once for efficiency
    lines = iter(sys.stdin.read().splitlines())

    for line in lines:
        if not line: continue

        # 1. Read and update global dimensions n and m
        n, m = map(int, line.split())

        # 2. Read data into the pre-allocated global `mat`
        for i in range(n):
            row_data = list(map(int, next(lines).split()))
            # Copy data into the global matrix slice by slice
            for j in range(m):
                mat[i][j] = row_data[j]

        # 3. Call the core logic function (which uses globals) and print
        print(max_sum_submatrix())


if __name__ == "__main__":
    main()

import sys

# ---------------------------------------------------------
# 算法核心逻辑 (这部分无需改动)
# ---------------------------------------------------------

# 预分配静态空间，这个思想依然是有效的
MAXN, MAXM = 201, 201
mat = [[0] * MAXM for _ in range(MAXN)]
arr = [0] * MAXM
n, m = 0, 0

def max_sum_subarray() -> int:
    """求一维数组的最大子数组和 (Kadane's 算法)"""
    max_val = -float('inf')
    cur_sum = 0
    for i in range(m):
        cur_sum += arr[i]
        max_val = max(max_val, cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    return max_val

def max_sum_submatrix() -> int:
    """计算子矩阵最大累加和"""
    max_global = -float('inf')
    for i in range(n):
        # 重置辅助数组
        for k in range(m):
            arr[k] = 0
        for j in range(i, n):
            # 压缩矩阵到一维数组
            for k in range(m):
                arr[k] += mat[j][k]
            # 更新最大值
            max_global = max(max_global, max_sum_subarray())
    return max_global

# ---------------------------------------------------------
# 【全新】主函数与 IO 处理
# ---------------------------------------------------------

def main():
    """
    采用 Pythonic 高性能 I/O 方式的主函数。
    """
    global n, m

    # 1. 一次性读取所有输入，并按空白分割成一个“词语”列表。
    # 这是Python中处理此类问题最简单、最稳健、且速度极快的方法。
    try:
        tokens = iter(sys.stdin.read().split())
    except IOError:
        return

    # 用于缓存所有输出结果的列表
    output_buffer = []

    # 2. 通过循环和迭代器，不断地从 tokens 中取出数据。
    while True:
        try:
            # `next(tokens)` 会从列表中取出一个元素。
            # `int()` 将其转换为整数。
            n = int(next(tokens))
            m = int(next(tokens))

            for i in range(n):
                for j in range(m):
                    mat[i][j] = int(next(tokens))

            result = max_sum_submatrix()
            output_buffer.append(f"{result}\n")

        except StopIteration:
            # 当 `next(tokens)` 尝试从一个空的迭代器中取数据时，
            # 会自然地触发 `StopIteration` 异常。
            # 这是我们正常结束循环的信号。
            break

    # 3. 所有测试用例处理完毕后，一次性写入所有结果。
    if output_buffer:
        sys.stdout.write("".join(output_buffer))

if __name__ == "__main__":
    main()