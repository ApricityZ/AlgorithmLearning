# 导入 sys 模块，这是 Python 中进行标准输入输出的核心。
import sys
# 导入 collections.deque，这是一个双端队列，比用 list 实现队列更高效。
from collections import deque

# --------------------------------------------------------------------------------
# 教学性注释：Python I/O 与 Java I/O 的核心区别
# --------------------------------------------------------------------------------
#
# 在 Java 中，存在多种 I/O 方式，比如：
# 1. `Scanner`: 方便但慢。
# 2. `StreamTokenizer`: 性能高，但有局限性，比如无法正确读取非常大的 long 或某些科学记数法 double。
# 3. `BufferedReader` + `StringTokenizer` (Kattio 类的实现原理): 非常健壮，性能也很好。
#
# 因此，Java 程序员有时需要一个像 Kattio 这样的自定义类来规避 `StreamTokenizer` 的问题。
#
# 但是，在 Python 中，情况完全不同！
# Python 的标准 I/O 方法 `sys.stdin.readline().split()` 已经是最常用、最高效且最健壮的方式。
# 它天生就能正确处理：
#   - 任意大的整数 (Python 的 int 类型没有溢出限制)。
#   - 各种格式的浮点数，包括科学记数法。
#
# 结论：Python 用户通常不需要自定义一个 `PyKattio` 类。下面的代码主要是为了教学目的，
# 展示如果我们需要，可以如何构建这样一个类，并将其与 Python 的标准方法进行对比。
#
# --------------------------------------------------------------------------------


class PyKattio:
    """
    这是一个模仿 Java Kattio 类的 Python 实现，主要用于教学演示。
    它封装了按需读取和分割输入行的逻辑。
    """

    def __init__(self, instream=sys.stdin, outstream=sys.stdout):
        """
        构造函数，初始化输入和输出流。
        :param instream: 输入流，默认为标准输入 sys.stdin。
        :param outstream: 输出流，默认为标准输出 sys.stdout。
        """
        self.instream = instream
        self.outstream = outstream
        # 使用双端队列 `deque` 作为内部缓冲区，存储分割后的字符串（token）。
        # 从左侧弹出（popleft）比从列表的第0个位置弹出更高效。
        self._tokens = deque()

    def _fetch_tokens(self):
        """
        这是一个内部辅助方法，当缓冲区为空时，负责从输入流读取新的一行并填充缓冲区。
        """
        # 从输入流读取一行，并移除两端的空白字符（如换行符）。
        line = self.instream.readline().strip()
        # 如果读到内容，就按空白字符分割，并填充到缓冲区。
        if line:
            self._tokens.extend(line.split())

    def next(self) -> str:
        """
        读取并返回下一个以空白字符分割的字符串 (token)。
        如果当前行已读取完毕，会自动读取下一行。
        """
        # 如果缓冲区为空，就调用辅助方法填充它。
        while not self._tokens:
            self._fetch_tokens()
        # 从缓冲区的左侧弹出一个 token 并返回。
        return self._tokens.popleft()

    def next_int(self) -> int:
        """读取下一个 token 并将其转换为整数。"""
        return int(self.next())

    def next_long(self) -> int:
        """
        读取下一个 token 并将其转换为长整数。
        在 Python 中，int 类型可以处理任意大小的整数，所以这和 next_int() 没有区别。
        """
        return int(self.next())

    def next_double(self) -> float:
        """读取下一个 token 并将其转换为浮点数。"""
        return float(self.next())

    def println(self, *args, **kwargs):
        """
        打印一行到输出流。
        这个方法直接封装了 Python 内置的 print 函数。
        """
        print(*args, file=self.outstream, **kwargs)

    def flush(self):
        """
        刷新输出缓冲区，确保所有内容都已写入。
        """
        self.outstream.flush()

    def close(self):
        """
        关闭流（在标准输入输出场景下通常不需要手动关闭）。
        """
        self.instream.close()
        self.outstream.close()


def main():
    """
    主函数，用于演示标准 Python I/O 和 PyKattio 类的行为。
    """
    print("--- 演示 Python 标准 I/O 方法 ---")
    print("请输入一个超大整数 (例如: 131237128371723187)，然后按回车:")

    # Python 的标准方法
    # 1. 读取一整行
    line1 = sys.stdin.readline()
    # 2. 直接使用 int() 转换，Python 的 int 可以处理任意精度，不会溢出
    long1 = int(line1.strip())
    print(f"标准方法读取到的数字: \n{long1}")
    print()

    print("请输入一个科学记数法表示的浮点数 (例如: 5.6920E+0001)，然后按回车:")
    line2 = sys.stdin.readline()
    # 直接使用 float() 转换，它能正确解析科学记数法
    double1 = float(line2.strip())
    print(f"标准方法读取到的数字: \n{double1}")

    print("\n" + "="*30 + "\n")

    print("--- 演示自定义的 PyKattio 类 ---")
    # 实例化我们的教学类
    io = PyKattio()
    print("请再次输入那个超大整数 (例如: 131237128371723187)，然后按回车:")
    # 使用 PyKattio 的方法读取
    long2 = io.next_long()
    print(f"PyKattio 读取到的数字: ")
    io.println(long2)
    print()

    print("请再次输入那个科学记数法浮点数 (例如: 5.6920E+0001)，然后按回车:")
    double2 = io.next_double()
    print(f"PyKattio 读取到的数字: ")
    io.println(double2)

    # 刷新并关闭流
    io.flush()


if __name__ == "__main__":
    main()