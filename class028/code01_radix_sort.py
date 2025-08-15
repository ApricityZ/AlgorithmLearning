# // 基数排序，acm练习风格
# // 测试链接 : https://www.luogu.com.cn/problem/P1177
# // 请同学们务必参考如下代码中关于输入、输出的处理
# // 这是输入输出处理效率很高的写法
# // 提交以下的code，提交时请把类名改成"Main"，可以直接通过

import sys

max_len = 100001
arr = [0] * max_len
help_arr = [0] * max_len
base = 10
counts = [0 for i in range(base)]  # 不要写成 [i for i in range(bese)] 初始值应该是0
n = 0


def main():
    global n, arr  # 凡是在局部函数使用全局变量，防止出错都要使用global声明，否则其他地方使用全局变量n可能数值错误
    nums = iter(map(int, list(sys.stdin.read().strip().split())))
    n = next(nums)
    for i in range(n):
        arr[i] = next(nums)

    # 获取最小值，最大值
    min_num = arr[0]
    for num in arr[0: n]:
        min_num = min(min_num, num)

    max_num = 0
    for i in range(n):
        arr[i] -= min_num
        max_num = max(max_num, arr[i])

    # 获取bits位数
    bites_len = bites(max_num)

    # 排序
    radix_sort(bites_len)

    # 恢复正常值
    for i in range(n):
        arr[i] += min_num

    # 打印
    sys.stdout.write(' '.join(map(str, arr[0: n])))


def bites(num):
    ans = 0
    global base
    while num > 0:
        ans += 1
        num //= base
    return ans


def radix_sort(bits):
    global counts, base, help_arr, n
    offset = 1
    for _ in range(bits):  # 用不到的循环变量，使用 _ 替代，防止出错
        # !!! 核心修正点 !!!
        # 在每一轮开始时，必须将计数数组清零
        # 否则上一轮的计数值会干扰本轮的计算
        for i in range(base):
            counts[i] = 0

        for j in range(n):  # 这里应该是 base，不是n,不对不对，应该是n，不是base
            counts[(arr[j] // offset) % base] += 1  # 这里的j错误写成了i，注意循环变量别弄混

        for k in range(1, base):
            counts[k] += counts[k - 1]  # 同样的问题

        for l in reversed(range(n)):
            counts_index = (arr[l] // offset) % base
            help_arr[counts[counts_index] - 1] = arr[l]  # counts[count_index] 减去 1 才是索引值
            counts[counts_index] -= 1

        arr[0: n] = help_arr[0: n]

        offset *= base

if __name__ == '__main__':
    main()