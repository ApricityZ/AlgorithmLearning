import numpy as np




def random_array(n, v):
    arr = np.zeros(n)
    for i in range(n):
        # np.random.random() -> double -> [0, 1)范围内的一个小数
        # np.random.random() * v -> double -> [0, v) 一个小数，依然等概率
        # int(np.random.random() * v) -> int -> {0, 1, ..., v-1} 等概率
        # int(np.random.random() * v + 1) -> int -> {1, 2, ..., v}
        arr[i] = int(np.random.random() * v + 1)
    return arr


def copy_array(arr):
    n = len(arr)
    ans = arr.copy()
    return ans


def same_array(arr1, arr2):
    # n = len(arr1)
    # for i in range(n):
    #     if arr1[i] != arr2[i]:
    #         return False
    # return True
    return np.array_equal(arr1, arr2)


def selection_sort(arr):
    if (arr is None) or len(arr) < 2: # 不能使用 not arr来判断numpy数组是否为空，
        return
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        swap(arr, i, min_index)

def bubble_sort(arr):
    if (arr is None) or len(arr) < 2:
        return
    for i in reversed(range(len(arr))):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)



def insertion_sort(arr):
    if (arr is None) or len(arr) < 2:
        return
    for i in range(len(arr)):
        j = i
        while j > 0 and (arr[j] < arr[j - 1]):
            swap(arr, j, j - 1)
            j -= 1


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def main():
    # the max length of a random list
    N = 200
    v = 1000
    # the value of each element in the random list, which is sample uniformly from {1, 2, ..., v}
    # test times
    test_times = 5000
    print("Test starts")
    for i in range(test_times):
        n = int(np.random.random() * N)
        arr = random_array(n, v)
        arr1 = copy_array(arr)
        arr2 = copy_array(arr)
        arr3 = copy_array(arr)
        selection_sort(arr1)
        bubble_sort(arr2)
        insertion_sort(arr3)
        if (not same_array(arr1, arr2) or not same_array(arr1, arr3)):
            print("Wrong occurred")
    print("Test finished")

main()
