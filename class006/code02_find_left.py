import numpy as np


# 有序数组中寻找 >= num 的最左位置
def random_array(len, max_value):
    return np.random.random_integers(0, max_value, len)


def right(arr, num):
    for i, number in enumerate(arr):
        if number >= num:
            return i

    return -1


def exist(arr, num):
    l = 0
    r = len(arr) - 1
    ans = -1
    while l <= r:
        mid = l + ((r - l) >> 1)
        if arr[mid] >= num:
            r = mid -1
            ans = mid
        else:
            l = mid + 1
    return ans

def validation(r1, r2):
    return r1 == r2

def main():
    max_len = 100
    max_value = 1000
    test_times = 500000
    print('===Test Starts===')
    for i in range(test_times):
        len = np.random.randint(max_len + 1)
        arr = random_array(len, max_value)
        num = np.random.random_integers(0, max_value)
        arr.sort()  # 这里的方法是针对数组有序的情况下使用的
        r1 = right(arr, num)
        r2 = exist(arr, num)
        if not validation(r1, r2):
            print('===Error Occurred===')

    print('===Test Finished===')

if __name__ == '__main__':
    main()

