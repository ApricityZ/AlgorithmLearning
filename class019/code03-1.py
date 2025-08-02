import sys
import io  # 导入 io 模块

# ---------------------------------------------------------
# 算法核心逻辑 (这部分完全不变)
# ---------------------------------------------------------

# 预分配静态空间
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
# 主函数与 IO 处理 (这部分也完全不变)
# ---------------------------------------------------------

def main():
    """
    采用 Pythonic 高性能 I/O 方式的主函数。
    """
    global n, m

    try:
        tokens = iter(sys.stdin.read().split())
    except IOError:
        return

    output_buffer = []

    while True:
        try:
            n = int(next(tokens))
            m = int(next(tokens))

            for i in range(n):
                for j in range(m):
                    mat[i][j] = int(next(tokens))

            result = max_sum_submatrix()
            output_buffer.append(f"{result}\n")

        except StopIteration:
            break

    if output_buffer:
        sys.stdout.write("".join(output_buffer))

# ---------------------------------------------------------
# 【新增】sys.stdin 模拟与程序主入口
# ---------------------------------------------------------

if __name__ == "__main__":

    # 1. 将你的所有测试用例定义为一个多行字符串
    #    使用三个引号 `"""` 可以方便地创建包含换行的字符串。
    test_data = """
    3 3
    -1 -1 -1
    -1 2 -1
    -1 -1 -1
    """

    # 你可以轻松地在这里添加或切换其他测试用例
    # test_data = """
    # 2 2
    # 10 -1
    # -5 20
    # """

    # 2. 保存原始的 sys.stdin
    original_stdin = sys.stdin

    # 3. 使用 try...finally 来确保无论程序是否出错，原始的 stdin 都能被恢复
    try:
        # 4. 创建一个在内存中的“假”输入文件，并将 sys.stdin 指向它
        sys.stdin = io.StringIO(test_data)

        # 5. 现在调用 main() 函数，它会从我们上面定义的 test_data 中读取数据
        print("--- 开始模拟 sys.stdin 输入 ---")
        main()
        print("--- 模拟结束 ---")

    finally:
        # 6. 恢复原始的 sys.stdin
        sys.stdin = original_stdin