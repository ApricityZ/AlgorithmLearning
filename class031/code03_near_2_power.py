# // 已知n是非负数
# // 返回大于等于n的最小的2某次方
# // 如果int范围内不存在这样的数，返回整数最小值

def logical_right_shift(val, n):
    """
    对一个整数执行逻辑右移操作。

    Args:
      val: 需要移位的整数 (可以是正数或负数)。
      n:   向右移动的位数。

    Returns:
      逻辑右移后的结果。
    """
    # 定义位长，对于大多数现代系统，整数是64位或32位。
    # 我们用64位作为示例，这在多数情况下是安全的。
    BIT_LENGTH = 32

    # 创建一个掩码，例如对于64位整数，它将是 2^64 - 1
    # 或者写作 0b111...111 (共64个1)
    mask = (1 << BIT_LENGTH) - 1

    # 1. 将 val (无论正负) 与掩码进行 & 运算，将其视为无符号数
    #    对于负数 -20，这会得到一个非常大的正整数
    unsigned_val = val & mask

    # 2. 对这个结果进行标准的右移
    return unsigned_val >> n


def near_two_power(n):
    if n <= 0:
        return 1
    n -= 1  # 预防类似与 n = 2^5 = 32这种类型
    n |= logical_right_shift(n, 1)
    n |= logical_right_shift(n, 2)
    n |= logical_right_shift(n, 4)
    n |= logical_right_shift(n, 8)
    n |= logical_right_shift(n, 16)

    ans = n + 1
    if ans > 2 ** 31 - 1:
        ans -= 2 ** 32

    return ans


print(near_two_power(5))


def test():
    # --- 测试 ---
    # 使用 -20 进行测试
    val = -20
    shifted_val = logical_right_shift(val, 2)

    print(f"对 {-20} 进行逻辑右移 2 位的结果是: {shifted_val}")

    # 让我们看看它的二进制和十六进制，以验证结果
    # -20 的 64 位补码是: ...1111111111101100
    # 逻辑右移 2 位后应该是: 00...00111111111111111011
    # 这个结果是一个非常大的正数
    print(bin(-20))
    print(f"十六进制表示: {bin(shifted_val)}")
test()
