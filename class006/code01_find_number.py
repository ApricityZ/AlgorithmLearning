import numpy as np


def gene_random_array(n, v):
    arr = np.ones(n)
    for i in range(len(arr)):
        arr[i] = np.random.randint(v) + 1
    return arr


def right(arr, num):
    for number in arr:
        if number == num:
            return True
        else:
            continue
    return False


def exist(arr, num):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + ((r - l) >> 2)
        if arr[mid] == num:
            return True
        elif arr[mid] < num:
            l = mid + 1
            continue
        elif arr[mid] > num:
            r = mid - 1
            continue

    return False

def validation(result1, result2):
    return result1 == result2


def main():
    max_arr_len = 100
    max_element_value = 1000
    test_times = 50000
    print(f'===Test Starts!===')
    for i in range(test_times):
        arr_len = np.random.randint(max_arr_len + 1)
        arr = gene_random_array(arr_len, max_element_value)
        num = np.random.randint(max_element_value) + 1
        arr.sort()
        if not validation(right(arr, num), exist(arr, num)):
            print('===Error Occurred===')
    print(f'===Test Finished!===')

if __name__ == '__main__':
    main()



