# 小和问题，利用分治方法解决
# // 测试链接 : https://www.nowcoder.com/practice/edfe05a1d45c4ea89101d936cac32469
# // 请同学们务必参考如下代码中关于输入、输出的处理
# // 这是输入输出处理效率很高的写法
# // 提交以下的code，提交时请把类名改成"Main"，可以直接通过

import sys

max_len = 100001
arr = [0] * max_len
help_arr = [0] * max_len
n = 0


def merge(l: int, mid: int, r: int) -> int:
    # 统计部分
    i = l
    j = mid + 1
    sum, ans = 0, 0
    while j <= r:
        while i <= mid:
            if arr[i] <= arr[j]:
                sum += arr[i]
                i += 1
            else:  # 注意这里，如果不满足条件，需要跳出这个循环，否则陷入死循环
                break
        ans += sum
        j += 1

    # 归并部分
    help_arr[l: r + 1] = arr[l:r + 1]
    a = l
    b = mid + 1
    for k in range(l, r + 1):
        if a > mid:
            arr[k] = help_arr[b]  # 注意这里，不要惯性的写作：arr[i] = help_arr[b]，因为我们之前一直用i，但这里使用k作为循环变量
            b += 1
        elif b > r:
            arr[k] = help_arr[a]
            a += 1
        elif help_arr[a] <= help_arr[b]:
            arr[k] = help_arr[a]
            a += 1
        else:
            arr[k] = help_arr[b]
            b += 1

    return ans


def small_sum(l, r):
    if l == r:  # 使用递归方法首先要写 base case，否则无限递归
        return 0
    mid = (l + r) // 2
    return small_sum(l, mid) + small_sum(mid + 1, r) + merge(l, mid, r)


def main():
    nums = iter(list(map(int, sys.stdin.read().strip().split())))
    global n, arr
    n = next(nums)
    arr = [next(nums) for _ in range(n)]
    sys.stdout.write(str(small_sum(0, n - 1)))  # 注意这里，write方法参数只支持 字符串 str 类型


if __name__ == '__main__':
    main()
