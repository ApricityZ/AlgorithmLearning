import numpy as np

'''寻找 <= num 的最右侧索引'''


def random_array(len, max_value):
    return np.random.randint(0, max_value + 1, len)


def right(arr, num):
    for i, value in enumerate(reversed(arr)):
        if value <= num:
            return len(arr) - 1 - i
    return -1


def find_right(arr, num):
    l = 0
    r = len(arr) - 1
    ans = -1
    while l <= r:
        mid = l + ((r - l) >> 1)
        if arr[mid] <= num:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans


def validation(r1, r2):
    return r1 == r2


def main():
    max_len = 100
    max_val = 1000
    test_times = 50000
    print('===Test Starts===')
    for i in range(test_times):
        len = np.random.randint(0, max_len + 1)
        num = np.random.randint(0, max_val + 2)
        arr = random_array(len, max_val)
        arr.sort()
        r1 = right(arr, num)
        r2 = find_right(arr, num)
        if not validation(r1, r2):
            print('===Error Occurred===')
    print('===Test Finished===')


if __name__ == '__main__':
    main()
