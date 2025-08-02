import sys

# ------------------------------------------------------------------
# 核心算法部分 (与之前的翻译相同)
# ------------------------------------------------------------------

def max_sum_subarray(arr: list[int]) -> int:
    """
    求一维数组的最大子数组和 (Kadane's 算法)。
    这完全对应 Java 代码中的 `maxSumSubarray` 方法。
    """
    # 使用 -float('inf') 对应 Java 的 Integer.MIN_VALUE
    max_val = -float('inf')
    cur_sum = 0
    for num in arr:
        cur_sum += num
        max_val = max(max_val, cur_sum)
        # 如果当前累加和变为负数，则从下一位置重新开始计算
        cur_sum = 0 if cur_sum < 0 else cur_sum
    return max_val

def max_sum_submatrix(mat: list[list[int]], n: int, m: int) -> int:
    """
    计算子矩阵最大累加和的核心逻辑。
    这完全对应 Java 代码中的 `maxSumSubmatrix` 方法。
    """
    max_global = -float('inf')

    # 循环，固定子矩阵的“上边界”
    for i in range(n):
        # 这是“压缩”后的一维数组，每次更换上边界时都重置
        compressed_arr = [0] * m

        # 循环，固定子矩阵的“下边界”
        for j in range(i, n):
            # 把当前下边界所在行的数据，累加到压缩数组中
            for k in range(m):
                compressed_arr[k] += mat[j][k]

            # 在“压缩”后的一维数组上求解最大子数组和，并更新全局最大值
            max_global = max(max_global, max_sum_subarray(compressed_arr))

    return max_global

# ------------------------------------------------------------------
# ACM 模式的主程序入口
# ------------------------------------------------------------------

def main():
    """
    主函数，负责循环读取和处理所有测试用例。
    这对应 Java 代码中的 `main` 方法。
    """
    # sys.stdin 是一个可迭代对象，可以逐行读取所有输入
    # 这比 `while True` 加 try-except 更简洁，可以自然处理到文件末尾的情况
    lines = iter(sys.stdin.read().splitlines())

    for line in lines:
        # 1. 读取矩阵维度 n 和 m
        # line.split() 会将 "3 3" 这样的字符串分割成 ['3', '3']
        # map(int, ...) 会将它们转换为整数
        n, m = map(int, line.split())

        # 2. 读取 n 行来构建矩阵
        mat = []
        for _ in range(n):
            # 从迭代器中获取下一行并解析
            row_line = next(lines)
            row = list(map(int, row_line.split()))
            mat.append(row)

        # 3. 调用核心算法计算结果
        result = max_sum_submatrix(mat, n, m)

        # 4. 打印结果
        # 在 Python 中，print() 会自动在末尾添加换行符
        print(result)

if __name__ == "__main__":
    # 在牛客网等平台上，通常建议使用 try-except 来包裹主函数调用，
    # 以防止因为一些意外的输入格式错误导致整个程序崩溃。
    try:
        main()
    except (IOError, ValueError):
        pass


# 代码要点与 Java 版本对比
# 处理多组测试用例:
#
# Java: 使用 while (in.nextToken() != StreamTokenizer.TT_EOF) 循环，直到没有更多的 token（输入流结束）。
#
# Python: 我这里使用了 sys.stdin.read().splitlines() 读取所有行并创建一个迭代器。for line in lines: 会一直处理直到所有行都被消耗完毕，从而优雅地处理到文件末尾。这种方式适合一次性将输入读入内存，如果输入文件极大，逐行读取会更好（如下面“备选方案”所示）。
#
# 读取输入:
#
# Java: 使用 StreamTokenizer，通过 in.nextToken() 和 in.nval 逐个读取数字。
#
# Python: 使用 sys.stdin.readline().split() 或 line.split() 读取一整行，然后用 map(int, ...) 将该行所有由空格分隔的数字字符串一次性转换成整数。这在 Python 中是更惯用、更简洁的做法。
#
# 输出:
#
# Java: 使用 PrintWriter 配合缓冲区来提高输出效率，最后需要 out.flush()。
#
# Python: 内置的 print() 函数通常已经足够快，并且默认就会使用缓冲区。对于绝大多数在线编程竞赛来说，直接使用 print() 不会造成性能问题。