import sys
import numpy as np

nint8 = lambda x: np.int8(x)
nint16 = lambda x: np.int16(x)
nint32 = lambda x: np.int32(x)
nint64 = lambda x: np.int64(x)
nuint8 = lambda x: np.uint8(x)
nuint16 = lambda x: np.uint16(x)
nuint32 = lambda x: np.uint32(x)
nuint64 = lambda x: np.uint64(x)


def printBinary(num):
    print("".join("1" if num & (1 << i) else '0' for i in reversed(range(32))))


a = nint32(78)
print(a)
printBinary(a)
print('===a===')

print(f"{nint32(2 ** 31 - 1) + 1} 得到负数，溢出")  # overflow，得到负数
print(nint32(-2 ** 31))
print('===validate overflow===')

b = nint32(-6)
print(f"b {b}")
printBinary(b)
print('===b===')

c = 0b100110  # 直接写二进制形式定义变量
print(c)
printBinary(c)
print('===c===')

d = nint32(0x4e)
print(d)
printBinary(d)
print('===d===')

# ~ 相反数
print(a)
printBinary(a)
printBinary(~a)
e = ~a + 1
print(e)
printBinary(e)
print('===e===')

minus_b = ~b + 1
minus_b1 = ~(b - 1)
print(b, minus_b, minus_b1)

# int，long的最小值，取相反数、绝对值都是自己
f = nint32(-2 ** 31)
print(f)
printBinary(f)
print(f"-f {f}")
printBinary(-f)
print(f"-f+1 {~f + 1}")
printBinary(~f + 1)
print('===f===')

# | & ^
g = nint32(0b0001010)
h = nint32(0b0001100)
printBinary(g)
printBinary(h)
printBinary(g | h)
printBinary(g & h)
printBinary(g ^ h)
print('===g,h===')
# // 可以这么写 : int num = 3231 | 6434;
# // 可以这么写 : int num = 3231 & 6434;
# // 不能这么写 : int num = 3231 || 6434;
# // 不能这么写 : int num = 3231 && 6434;
# // 因为 ||、&& 是 逻辑或、逻辑与，只能连接boolean类型
# // 不仅如此，|、& 连接的两侧一定都会计算
# // 而 ||、&& 有穿透性的特点
printBinary(g or h)  # 不是逐位运算，会打印g，讲g和h视为两个独立的条件，如果不为零，那么视为True，短路
def return_true():
    print("进入了return_true函数")
    return True


def return_false():
    print("进入了return_false函数")
    return False
print(f'test1 | {return_true() | return_false()}')
# 进入了return_true函数
# 进入了return_false函数  不会短路
print(f'test2 || {return_true() or return_false()}')
# 进入了return_true函数
# test2 || True 短路，之进入了return_true函数，然后后续不在运行

print(f"test3 & {return_false() & return_true()}")
# 进入了return_false函数
# 进入了return_true函数
# test3 & False 两个函数都会进入
print(f"test3 && {return_false() and return_true()}")
# 进入了return_false函数
# test3 && False 发生短路，遇到第一个 false之后直接停止
print('===|, &, ||, &&===')

i = nint32(0b0011010)
printBinary(i)
printBinary(i << 2)
printBinary(i << 2)
printBinary(i << 3)
print(i)
print(i << 1)
print(i << 2)
print(i << 3)
print('===i << ===')

# 对于非负数而言，>> >>>（无符号位移，不管原来符号位是什么，都补零，导致负数变正数）是一样的，故对非负数无所谓

printBinary(i)
printBinary(i >> 2)
print(i >> 2)
print('===i >>===')

j = 0b111100000000000000000000  #❗ 在 Python/ NumPy 中，你确实无法直接用 np.int32(0b1111...) 的方式定义一个二进制补码的负数，
# 除非你先把它转成正确的十进制负数或用 uint32 再转视图。
printBinary(j)
printBinary(j >> 2)
print(j) # 这里其实是正数
print(j >> 2)
print('===j >>===')

# // 非负数 << 1，等同于乘以2
# // 非负数 << 2，等同于乘以4
# // 非负数 << 3，等同于乘以8
# // 非负数 << i，等同于乘以2的i次方
# // ...
# // 非负数 >> 1，等同于除以2
# // 非负数 >> 2，等同于除以4
# // 非负数 >> 3，等同于除以8
# // 非负数 >> i，等同于除以2的i次方
# // 只有非负数符合这个特征，负数不要用

k = nint32(10)
print(k)
print(k << 1)
print(k << 2)
print(k << 3)
print(k >> 1)
print(k >> 2)
print(k >> 3)
print('===k===')



