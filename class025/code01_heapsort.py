# // 堆结构和堆排序，acm练习风格
# // 测试链接 : https://www.luogu.com.cn/problem/P1177
# // 请同学们务必参考如下代码中关于输入、输出的处理
# // 这是输入输出处理效率很高的写法
# // 提交以下的code，提交时请把类名改成"Main"，可以直接通过
import sys

max_len = 50001
arr = [0] * max_len
n = 0


def swap(a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp


def heap_insert(i):
    while ((i - 1) // 2) >= 0 and arr[i] > arr[(i - 1) // 2]:
        swap(i, (i - 1) // 2)
        i = (i - 1) // 2


def heapify(i, size):
    l = 2 * i + 1
    while l < size:
        best = l + 1 if (l + 1 < size) and (arr[l] < arr[l + 1]) else l
        best = best if arr[best] > arr[i] else i
        if best == i:
            break
        swap(i, best)
        i = best  # 注意，i指向当前需要变换位置的节点，这个节点在交换之后应该进行更新，否则就是指向原来的位置，而不是交换后的位置，导致上面的i错误
        # l = 2 * best + 1
        l = 2 * i + 1  # 为了提醒自己，左子节点应该是节点i指向节点的孩子，该节点交换后应该下沉


def heapsort1():
    # 建立大根堆，从顶到底
    for i in range(n):
        heap_insert(i)

    # 元素归位，排序
    size = n
    while size > 0:
        size -= 1
        swap(0, size)
        heapify(0, size)


def heapsort2():
    # 建立大根堆，从底到顶
    for i in reversed(range(n)):
        heapify(i, n)

    # 元素归位，排序
    size = n
    while size > 0:
        size -= 1
        swap(0, size)
        heapify(0, size)


def main():
    global n, arr
    numbers = iter(map(int, list(sys.stdin.read().strip().split())))
    n = next(numbers)
    for i in range(n):
        arr[i] = next(numbers)

    # heapsort1()
    heapsort2()

    sys.stdout.write(' '.join(map(str, arr[0: n])))


if __name__ == '__main__':
    main()
