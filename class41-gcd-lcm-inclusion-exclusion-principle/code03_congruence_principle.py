# // 加法、减法、乘法的同余原理
# // 不包括除法，因为除法必须求逆元，后续课讲述
import random


# 	// 计算 ((a + b) * (c - d) + (a * c - b * d)) % mod 的非负结果

def direct_calculation(a, b, c, d, mod: int):
    in_ans1 = a + b
    in_ans2 = c - d
    in_ans3 = in_ans1 * in_ans2
    in_ans4 = a * c
    in_ans5 = b * d
    in_ans6 = in_ans4 - in_ans5
    in_ans7 = in_ans3 + in_ans6
    in_ans8 = in_ans7 % mod
    if in_ans8 < 0:
        return in_ans8 + mod
    else:
        return in_ans8


# “在进行加、减、乘的连续模运算时，最保险、最健壮的做法就是先将每一个原始数字或中间结果进行取模，然后再参与下一步运算。”
# 注意不包括除法
# 这样做主要有三大好处：
# 绝对安全（防溢出）：这是最重要的原因。它能从根本上杜绝在C++、Java等定长整数语言中因中间结果过大而导致的溢出问题。
# 代码一致性（跨平台）：无论你用的是 Python（自动处理大数）还是 C++（需要关心溢出），遵循这个原则写出的逻辑都是一样的，代码移植性与可读性更高。
# 性能更优（提效率）：对两个较小的数进行运算，通常比对两个天文数字般的整数进行运算要快得多。
def inner_mode_cal(a, b, c, d, mod: int):
    o1 = a + b
    o1 = o1 % mod
    o2 = c % mod - d % mod
    o2 = (o2 + mod) % mod
    o3 = o1 * o2
    o3 = o3 % mod
    o4 = a * c
    o4 = (a * c) % mod
    o5 = b * d
    o5 = o5 % mod
    o6 = (o4 % mod - o5 % mod + mod) % mod
    o7 = (o3 + o6) % mod
    return o7


def generate_five_num():
    int_max_num = 2 ** 31 - 1
    a = random.random() * int_max_num
    b = random.random() * int_max_num
    c = random.random() * int_max_num
    d = random.random() * int_max_num
    mod = random.random() * int_max_num
    return a.__int__(), b.__int__(), c.__int__(), d.__int__(), mod.__int__()


def validate(ans1, ans2):
    if ans1 != ans2:
        return False
    return True


def main():
    test_times = 10000
    print("Start!")
    for _ in range(test_times):
        params = generate_five_num()
        if not validate(direct_calculation(*params), inner_mode_cal(*params)):
            print("Error Occurred!")
    print("finished!")


if __name__ == '__main__':
    main()
