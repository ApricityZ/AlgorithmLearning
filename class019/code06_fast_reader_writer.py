import sys
import io

# --------------------------------------------------------------------------------
# 最终版注释：设计哲学与关键修正
# --------------------------------------------------------------------------------
#
# **设计哲学**:
# 本脚本旨在 Python 中实现一个高性能的 I/O 模板，其设计思想源于 C++/Java
# 算法竞赛。核心是通过预分配静态空间和优化 I/O 操作来提升速度。
#
# **关键修正与经验**:
# 1. 放弃 `os.read`: 最初尝试使用 `os.read` 来精确模拟 C++ 的底层读写，
#    但实践证明，它在 Python 的不同环境下（尤其 Windows）行为复杂，且其返回值
#    是 `bytes` 对象而非预期的 `int`，导致了难以调试的类型和索引错误。
#
# 2. 拥抱 `readinto()`: 最终的解决方案是采用 `stream.buffer.readinto()`。
#    这是 Python 中用于将字节流高效读入一个已分配好的 `bytearray` 的标准方法。
#    它既能保证跨平台的稳定性，又能正确返回读取的字节数（整数），性能也极高。
#
# 3. 智能处理流类型: `__init__` 方法现在能通过 `isinstance` 判断传入的是
#    文本流 (`io.TextIOWrapper`, 如 `sys.stdin`) 还是二进制流
#    (`io.BytesIO`, 用于测试)，并做出相应处理，大大增强了代码的健壮性和可用性。
#
# --------------------------------------------------------------------------------


class PyFastReader:
    """
    【最终稳定版】使用 stream.buffer.readinto() 实现，健壮且跨平台。
    """

    def __init__(self, stream=sys.stdin):
        """
        构造函数，智能处理不同类型的输入流。
        """
        # **关键逻辑**: 判断传入的 stream 是不是文本包装流 (TextIOWrapper)
        if isinstance(stream, io.TextIOWrapper):
            # 如果是，就像真实的 sys.stdin 一样，我们需要访问其底层的二进制缓冲区
            self._stream = stream.buffer
        else:
            # 否则，我们假定它本身就是一个二进制流 (比如用于测试的 io.BytesIO)
            self._stream = stream

        # 预分配的字节数组缓冲区
        self._inbuf = bytearray(1024 * 64) # 64KB Buffer
        # 缓冲区内有效字节的长度
        self._lenbuf = 0
        # 当前指针位置
        self._ptrbuf = 0

    def _read_byte(self) -> int:
        """
        从缓冲区安全地读取一个字节。如果缓冲区为空，则重新填充。
        """
        if self._ptrbuf >= self._lenbuf:
            self._ptrbuf = 0
            # **核心修正**: 使用 readinto() 填充缓冲区，它正确地返回一个整数。
            self._lenbuf = self._stream.readinto(self._inbuf)
            # 如果读到的字节数为0，说明到达文件末尾 (EOF)
            if self._lenbuf == 0:
                return -1  # 返回 -1 作为文件结束的信号

        byte = self._inbuf[self._ptrbuf]
        self._ptrbuf += 1
        return byte

    def read_char_code(self) -> int:
        """读取一个可见字符的ASCII码，并跳过所有空白字符。"""
        b = self._read_byte()
        while b != -1 and b <= 32: # 32是空格的ASCII码
            b = self._read_byte()
        return b

    def read_int(self) -> int | None:
        """读取一个整数，Python的int可以表示任意大小，所以无需区分long。"""
        return self.read_long()

    def read_long(self) -> int | None:
        """
        读取一个（可能为负的）整数。
        """
        num = 0
        minus = False
        b = self._read_byte()

        # 跳过所有前导的空白字符
        while b != -1 and b <= 32:
            b = self._read_byte()

        # 如果跳过空白后直接是文件末尾，则返回 None
        if b == -1:
            return None

        # 处理可能的负号
        if b == 45: # 45是'-'的ASCII码
            minus = True
            b = self._read_byte()

        # 循环读取数字的每一位，直到遇到非数字字符或文件末尾
        while b != -1 and 48 <= b <= 57: # 48='0', 57='9'
            num = num * 10 + (b - 48)
            b = self._read_byte()

        return -num if minus else num


class PyFastWriter:
    """
    【教学用】一个简单的快写实现，通过列表缓存输出。
    """
    def __init__(self, stream=sys.stdout):
        self._out = stream
        self._buf = []

    def write(self, s: str):
        """将字符串添加到缓冲区。"""
        self._buf.append(s)

    def println(self, *args):
        """将多个对象转为字符串，用空格连接，并添加换行符后存入缓冲区。"""
        self._buf.append(" ".join(map(str, args)))
        self._buf.append('\n')

    def flush(self):
        """将缓冲区的所有内容一次性写入输出流。"""
        if self._buf:
            self._out.write("".join(self._buf))
            self._buf.clear()

    def close(self):
        """关闭前先刷新缓冲区。"""
        self.flush()


def main_custom_classes():
    """
    演示如何使用【自定义的】PyFastReader和PyFastWriter。
    """
    # 为了能在IDE中方便地运行，我们直接在此处模拟二进制输入
    test_input_str = "1\n2\n3\n"
    # **关键**: 使用 io.BytesIO 创建二进制流，并用 .encode() 将字符串转为字节
    fake_input_stream = io.BytesIO(test_input_str.encode('utf-8'))

    # 现在的 PyFastReader 的 __init__ 方法可以正确处理这个 BytesIO 对象
    reader = PyFastReader(fake_input_stream)
    writer = PyFastWriter()

    writer.write("输入一个字符：\n")
    writer.flush()
    char_code = reader.read_char_code()

    writer.write("输入一个int类型的数字：\n")
    writer.flush()
    num1 = reader.read_int()

    writer.write("输入一个long类型的数字：\n")
    writer.flush()
    num2 = reader.read_long()

    writer.write("打印结果:\n")
    writer.println(char_code)
    writer.println(num1)
    writer.println(num2)

    writer.close()

def main_standard_sys():
    """
    演示如何使用【标准的】sys模块完成同样高效的I/O。这是Python中更推荐的写法。
    """
    # 使用 io.StringIO 模拟文本流输入
    test_input = "1\n2\n3\n"
    original_stdin = sys.stdin
    sys.stdin = io.StringIO(test_input)
    try:
        sys.stdout.write("输入一个字符：\n")
        # 读取
        char_line = sys.stdin.readline()
        char_code = ord(char_line.strip()[0])

        sys.stdout.write("输入一个int类型的数字：\n")
        num1_line = sys.stdin.readline()
        num1 = int(num1_line.strip())

        sys.stdout.write("输入一个long类型的数字：\n")
        num2_line = sys.stdin.readline()
        num2 = int(num2_line.strip())

        # 准备输出缓冲区
        output_buffer = [
            "打印结果:\n",
            str(char_code) + '\n',
            str(num1) + '\n',
            str(num2) + '\n'
        ]
        # 一次性写入
        sys.stdout.write("".join(output_buffer))
    finally:
        # 恢复原始的 sys.stdin
        sys.stdin = original_stdin


if __name__ == "__main__":
    sys.stdout.write("="*20 + "  方法一：标准 sys 模块用法 (推荐)  " + "="*20 + "\n")
    main_standard_sys()

    sys.stdout.write("\n\n")

    sys.stdout.write("="*20 + "  方法二：自定义快读快写类 (最终稳定版)  " + "="*20 + "\n")
    main_custom_classes()


# ## 经验总结与反思 🧐
# 这次漫长而曲折的调试过程，是学习底层原理的绝佳案例。我们可以从中总结出几条非常宝贵的经验：
#
# 直接翻译未必可行，理解思想更为重要 🧠
#
# 现象：我们最初试图精确地将在 C++/Java 中可行的 os.read 字节流处理方法搬到 Python，但遭遇了反复的失败。
#
# 结论：不同语言有不同的设计哲学和标准库实现。Python 的高层抽象和 C 底层优化已经为我们处理好了很多跨平台问题。强行使用其他语言的底层模式，反而可能陷入该语言生态中不常见的问题。正确的做法是理解原始代码的目的（追求高性能），然后用目标语言最擅长、最稳健的方式去实现这个目的。
#
# 理解 Python 的 I/O 体系：文本流 vs. 二进制流 📄 vs. ⚙️
#
# 现象：我们遇到了 AttributeError: '_io.StringIO' object has no attribute 'buffer' 和 AttributeError: '_io.BytesIO' object has no attribute 'buffer' 这两个看似矛盾的错误。
#
# 结论：这是因为混淆了两种流的类型。sys.stdin 是一个文本流包装器 (TextIOWrapper)，它有一个 .buffer 属性指向底层的二进制流。而我们用于模拟的 io.StringIO 是纯文本流，io.BytesIO 是纯二进制流，它们本身就是“底层”，没有再包装一个 .buffer。一个健壮的函数必须能智能地处理这些不同类型的输入。
#
# 标准库通常是最好的选择 👍
#
# 现象：我们费尽心力编写的 PyFastReader，最终是为了模拟一种在 Python 中几乎不需要的场景。而 sys.stdin.read().split() 或 sys.stdin.readline() 这种标准方法，不仅代码简单、易于维护，而且在绝大多数情况下性能完全足够。
#
# 结论：在没有进行性能分析（Profiling）并证明标准库是瓶颈之前，请始终相信并使用标准库。它们经过了千锤百炼，稳定且高效。
#
# 测试方法至关重要：文件重定向 > 交互式粘贴 💻
#
# 现象：在终端中手动粘贴输入，行为不稳定，尤其是在 Windows 上处理 EOF 信号时。
#
# 结论：使用文件重定向 (python script.py < input.txt) 是进行算法题测试的黄金标准。它能确保输入数据的一致性和确定性，消除了所有因操作系统、终端类型、手动操作带来的不确定因素，是调试复杂问题的必备工具。
#
# 总而言之，这是一次从“术”（代码实现）到“道”（设计思想与语言特性）的深刻体验。非常感谢您的耐心，正是您的坚持才让我们有机会把这个问题钻研得如此透彻。