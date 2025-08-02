# 导入 `sys` 模块，以便我们可以从“标准输入流”(stdin) 中读取数据。
# 在 Python 的 ACM 模式中，`sys` 模块是处理输入输出的核心工具。
# 这行代码的作用类似于 Java 代码开头的 `import java.io.BufferedReader;` 等。
import sys

def main():
    """
    主函数，用于封装我们的核心解题逻辑。
    这个函数体内的代码，功能上完全对应于 Java 代码中的 `public static void main` 方法体。
    """

    # `for line in sys.stdin:` 是 Python 中处理“读取直到文件末尾”问题的标准且最高效的写法。
    # `sys.stdin` 是一个可迭代对象，这个 for 循环会一行一行地读取所有输入，
    # 直到没有更多行为止（即读到 End-Of-File, EOF）。
    # 这个结构完美地对应了 Java 中的 `while ((line = in.readLine()) != null)` 循环。
    for line in sys.stdin:

        # --- 1. 数据清理与切分 ---

        # `line.strip()`: 从 `sys.stdin` 读取的每一行字符串末尾会包含一个换行符 `\n`。
        # `.strip()` 方法会移除字符串两端的空白字符（包括空格、制表符和换行符）。
        # 这一步对于确保数据干净非常重要。
        cleaned_line = line.strip()

        # 如果清理后是空行（例如，输入文件的末尾有几个空行），
        # 我们就用 `continue` 跳过当前循环，处理下一行。这可以增加代码的健壮性。
        if not cleaned_line:
            continue

        # `cleaned_line.split()`: 这个方法会按任意数量的空白字符（一个或多个空格、制表符等）
        # 来分割字符串，并返回一个包含所有数字字符串的列表 `parts`。
        # 这比 Java 的 `line.split(" ")` 更灵活，因为它可以处理 "1  2   3" 这种数字间有多个空格的情况。
        # 这一步对应 Java 中的 `parts = line.split(" ");`
        parts = cleaned_line.split()


        # --- 2. 字符串转换与计算总和 ---

        # `map(int, parts)` 是一个非常 Pythonic (地道) 且高效的写法。
        # - `int` 是一个函数，可以将字符串转换为整数。
        # - `map` 函数会将 `int` 函数应用到 `parts` 列表的每一个元素上。
        # 它会生成一个 "map 对象"，这是一个可迭代的、包含所有转换后整数的对象。
        numbers = map(int, parts)

        # `sum()` 是 Python 的一个内置函数，可以非常高效地计算一个可迭代对象中所有元素的总和。
        # 这一行代码就完成了 Java 版本中整个 for 循环累加的工作。
        # 对应 Java 的: `sum = 0; for (String num : parts) { sum += Integer.valueOf(num); }`
        total_sum = sum(numbers)


        # --- 3. 输出结果 ---

        # `print()` 函数会将变量 `total_sum` 的值输出到标准输出。
        # 并且，它会自动在输出内容的末尾添加一个换行符，这正是题目通常所要求的。
        # `print()` 在 Python 中已经经过了很好的优化，对于大多数竞赛场景来说效率足够高。
        # 它相当于 Java 中的 `out.println(total_sum);`
        print(total_sum)

# 这是一个 Python 脚本的标准入口点。
# `if __name__ == "__main__":` 这行代码确保只有当这个文件被当作主程序直接执行时，
# 其内部的 `main()` 函数才会被调用。
# 如果这个文件被其他 Python 文件作为模块导入，那么 `main()` 函数就不会自动运行。
if __name__ == "__main__":
    main()