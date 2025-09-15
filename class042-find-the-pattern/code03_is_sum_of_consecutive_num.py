# // 判断一个数字是否是若干数量(数量>1)的连续正整数的和

def is_sum_of_cons_num(n: int):
    """
    判断n是否是一段连续正整数的和
    :param n: int 待判定的数
    :return: bool 是否满足条件
    """
    for i in range(1, n):
        sum = i
        for j in range(i + 1, n):
            sum += j
            if sum == n:
                return True
            if sum > n:
                # continue
                break
    return False


def find_pattern():
    for i in range(200):
        print(f"{i}: {is_sum_of_cons_num(i)}")


# find_pattern()


# 发现如果为 2 的倍数，那么结果不满足
def is2(n):
    return (n & (n - 1)) != 0

def test():
    for i in range(200):
        if is_sum_of_cons_num(i) != is2(i):
            print("Error")
    print("Finished")
test()
