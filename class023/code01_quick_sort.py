# // 随机快速排序，acm练习风格
# // 测试链接 : https://www.luogu.com.cn/problem/P1177
# // 请同学们务必参考如下代码中关于输入、输出的处理
# // 这是输入输出处理效率很高的写法
# // 提交以下的code，提交时请把类名改成"Main"，可以直接通过
import random
import sys

max_len = 100001
arr = [0] * max_len
n = 0


def swap(a, b) -> None:
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp


def partition1(l, r, x):
    a = l
    xi = 0
    # l   ...   r  x
    for i in range(l, r + 1):
        if arr[i] <= x:
            swap(a, i)
            if arr[a] == x:
                xi = a
            a += 1

    swap(xi, a - 1)
    return a - 1


def quick_sort1(l, r):
    if l >= r:
        return
    # x = random.choice(arr[0:n]) # 枢轴选取错误，应该从给定的区域中选择，而不是全局区域，否则可能不存在x，导致错误
    x = random.choice(arr[l: r + 1])
    mid = partition1(l, r, x)
    quick_sort1(l, mid - 1)
    quick_sort1(mid + 1, r)


global first, last


def partition2(l, r, x):
    global first, last
    first = l
    last = r
    i = l
    while i <= last:
        if arr[i] < x:
            swap(first, i)
            first += 1
            i += 1
        elif arr[i] == x:
            i += 1
        else:
            swap(last, i)
            last -= 1


def quick_sort2(l, r):
    if l >= r:
        return
    global n, first, last
    # x = random.choice(arr[0:n - 1]) # 枢轴选取错误，应该从给定的区域中选择，而不是全局区域，否则可能不存在x，导致错误
    x = random.choice(arr[l: r + 1])
    partition2(l, r, x)
    a = first  # 这里避免了first last的值覆盖问题，但是不够直观，并且使得代码更加脆弱，晦涩
    b = last
    quick_sort2(l, a - 1)
    quick_sort2(b + 1, r)


def main():
    numbers = iter(map(int, list(sys.stdin.read().strip().split())))
    global n, arr
    n = next(numbers)
    for i in range(n):
        arr[i] = next(numbers)
    quick_sort1(0, n - 1)
    sys.stdout.write(' '.join(map(str, arr[0: n])))


if __name__ == '__main__':
    main()
