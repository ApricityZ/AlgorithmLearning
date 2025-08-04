# define global variable
import sys

max_len = 501
arr = [0] * max_len
help_arr = list(arr)
n = 0


def merge(l: int, mid: int, r: int) -> None:
    help_arr[l:r + 1] = arr[l:r + 1]
    a = l
    b = mid + 1
    m = mid

    for i in range(l, r + 1):
        if a > m:
            arr[i] = help_arr[b]
            b += 1
        elif b > r:
            arr[i] = help_arr[a]
            a += 1
        elif help_arr[a] < help_arr[b]:
            arr[i] = help_arr[a]
            a += 1
        else:
            arr[i] = help_arr[b]
            b += 1


def merge_sort_r(l, r):
    if l == r:
        return
    mid = (l + r) // 2
    merge_sort_r(l, mid)
    merge_sort_r(mid + 1, r)
    merge(l, mid, r)


def merge_sort_i():
    step = 1
    while step < n:
        l = 0
        while l < n:
            m = l + step - 1
            if m >= n - 1:
                break
            r = min((l + 2 * step - 1), n - 1)
            merge(l, m, r)
            l = r + 1
        step *= 2


def main():
    global n

    input = list(map(int, sys.stdin.read().strip().split()))
    nums = iter(input)
    output = []

    while True:
        try:
            n = next(nums)

            for i in range(n):
                arr[i] = next(nums)

            # merge_sort_r(0, n - 1)
            merge_sort_i()
            output.append(list(arr[0: n]))
        except StopIteration:
            break

    for result in output:
        sys.stdout.write(" ".join(map(str, result)) + '\n')


if __name__ == '__main__':
    main()
