import sys

# [建议] 使用全局变量（Global Variables）通常不是一个好习惯。
# 这使得函数依赖于外部状态，降低了代码的可读性、可维护性和可复用性。
# 更好的做法是通过函数参数传递数据。
max_len = 5001
arr = [0] * max_len
help = [0] * max_len
n = 0


def main():
    global n, arr
    try:
        inputs = sys.stdin.read().strip().split()
    except IOError:
        return

    out_buffer = []

    # [逻辑问题] 这个 while True + try/except 结构是为了处理多组输入。
    # 虽然能工作，但如果输入格式固定，可以用更简洁的方式来迭代。
    while True:
        try:
            nums = iter(map(int, inputs))
            n = next(nums)
            for i in range(n):
                arr[i] = next(nums)

            # [逻辑问题] 冗余的排序调用。
            # 在这里调用递归排序后，arr 数组就已经是有序的了。
            merge_sort_r(0, n - 1)

            # [逻辑问题] 在一个已经有序的数组上，再次执行迭代排序是完全没有必要的，浪费了计算资源。
            # 你可能意在测试两种方法，但应该分开测试，而不是连续调用。
            merge_sort_iter()

            # [严重错误] 引用错误 (Reference Error)。
            # 这里你将列表 `arr` 的“引用”添加到了 `out_buffer` 中，而不是它的一个“副本”。
            # 这意味着 `out_buffer` 中的所有元素都指向内存中同一个列表对象。
            # 当下一轮循环修改 `arr` 的内容时，`out_buffer` 中所有之前添加的“快照”都会跟着改变。
            out_buffer.append(arr)

        except StopIteration:
            break

    if out_buffer:
        # [错误后果] 由于上面的引用错误，这里会多次打印完全相同的内容——也就是最后一次排序的结果。
        for arr in out_buffer:
            # [建议] 这样的输出格式会将数字直接拼接。例如，数组 [10, 2, 5] 会被打印成字符串 "1025"。
            # 通常我们期望的输出是用空格分隔的，如 "10 2 5"。
            sys.stdout.write(''.join(map(str, arr)))


def merge_sort_r(l: int, r: int) -> list[int] | int:
    if l == r:
        # [建议] 返回值类型不一致。基线条件返回一个 int，而递归调用后返回一个 list。
        # 对于在原数组上直接修改的排序函数（in-place sort），通常约定返回 None。
        return arr[l]
    mid = (l + r) // 2
    merge_sort_r(l, mid)
    merge_sort_r(mid + 1, r)
    merge(l, mid, r)
    return arr


def merge_sort_iter():
    step = 1
    # n = len(arr) # 这行被注释掉了，代码依赖于全局变量 n
    while step < n:
        l = 0
        while l < n:
            m = l + step - 1
            if m + 1 >= n:
                break

            # [风险] 边界处理不够健壮。
            # 这里计算的 r 可能会超出数组的有效索引范围 (n - 1)。
            # 例如，当 n=10, l=8, step=2 时, r 会被计算成 11，超出了边界。
            # 你的 merge 函数需要隐式地处理这个越界，更好的做法是在这里就确保 r 不越界。
            r = l + 2 * step - 1
            merge(l, m, r)

        step *= 2


def merge(l: int, mid: int, r: int) -> None:
    global help
    i = l
    a = l
    b = mid + 1
    while (a <= mid) and (b <= r):
        # help[i] = arr[a] if arr[a] <= arr[b] else arr[b]
        if arr[a] <= arr[b]:
            help[i] = arr[a]
            a += 1
        else:
            help[i] = arr[b]
            b += 1
        i += 1

    while a <= mid:
        help[i] = arr[a]
        i += 1
        a += 1

    # [严重错误] 这是导致排序结果不正确的关键 Bug！
    # 循环条件错误，应该是 `b <= r`，而不是 `b <= mid`。
    while b <= mid:
        # [错误后果] 这个错误的条件导致右半边子数组 arr[mid+1...r] 的剩余部分永远不会被复制。
        # 例如，当左半部分先被耗尽时，右半部分剩下的元素将全部丢失，从而导致最终排序结果不完整且错误。
        help[i] = arr[b]
        i += 1
        b += 1

    # [风险] 由于上面迭代排序中的 r 可能越界，这里的 r+1 也可能越界。
    # 幸运的是 range(l, r+1) 在 Python 中如果 l > r 不会报错，但这是依赖于语言特性的侥幸。
    for idx in range(l, r + 1):
        arr[idx] = help[idx]


if __name__ == '__main__':
    main()
