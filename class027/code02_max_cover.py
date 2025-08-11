import sys

# // 最多线段重合问题
# // 测试链接 : https://www.nowcoder.com/practice/1ae8d0b6bb4e4bcdbf64ec491f63fc37
# // 测试链接 : https://leetcode.cn/problems/meeting-rooms-ii/
# // 请同学们务必参考如下代码中关于输入、输出的处理
# // 这是输入输出处理效率很高的写法
# // 提交以下的code，提交时请把类名改成"Main"，可以直接通过

max_len = 10000
lines = [[0, 0] for _ in range(max_len)]
heap = [0] * max_len
n = 0
size = 0


def main():
    global n
    nums = iter(map(int, list(sys.stdin.read().strip().split())))
    n = next(nums)
    for i in range(n):
        lines[i][0] = next(nums)
        lines[i][1] = next(nums)
    sys.stdout.write(str(compute()))


def compute():
    global lines
    lines = sorted(lines[0:n], key=lambda x: x[0])
    ans = 0
    global size, heap
    for i in range(n):
        while size > 0 and lines[i][0] >= heap[0]:
            pop()
        add(lines[i][1])
        ans = max(ans, size)
    return ans


def pop():
    global size, heap
    swap(0, size - 1)
    size -= 1
    i = 0
    l = 2 * i + 1
    while l < size:
        best = l + 1 if l + 1 < size and heap[l + 1] < heap[l] else l
        best = best if heap[best] < heap[i] else i
        if best == i:
            break
        swap(i, best)  # 怎么可以忘记交换呢
        i = best
        l = 2 * i + 1


def add(val):
    global size, heap
    heap[size] = val
    i = size
    size += 1
    while (i - 1) // 2 >= 0 and heap[(i - 1) // 2] > heap[i]:
        swap(i, (i - 1) // 2)
        i = (i - 1) // 2
    # 您的简化思路是：
    # while heap[(i - 1) // 2] > heap[i]:
    # 这个简化其实是行不通的，i > 0 这个条件至关重要。
    # 在 Python 中，heap[-1] 会访问列表的最后一个元素。
    # 在我们的代码里，**heap 是一个预先分配了很大空间的列表**，所以 heap[-1] 的值很可能是初始的 0，或者某个之前计算留下的“脏数据”。
    # 这时，程序就会拿堆顶的元素 heap[0] 和一个完全不相干的值 heap[-1] 进行比较，这会导致两个严重的问题：
    # 逻辑错误：比较本身就是错的。
    # 数据损坏：如果条件碰巧成立了（比如堆顶是个正数，而heap[-1]是0），程序会执行 swap(0, -1)，把堆顶元素和最后一个元素交换，彻底破坏了堆的结构。
    # 而我们原来的写法：
    # while i > 0 and heap[i] < heap[(i - 1) // 2]:
    # 利用了 Python 的“短路求值”特性。当 i 变成 0 时，i > 0 这个条件为 False，Python 就不会再执行 and 后面的部分了，从而完美地避免了用 -1 做索引的问题。
    # 所以，i > 0 是确保元素到达堆顶时循环能正确、安全停止的关键。


def swap(a, b):
    tmp = heap[a]
    heap[a] = heap[b]
    heap[b] = tmp


if __name__ == '__main__':
    main()
