import sys


def get_max_value(arr: list[int], l: int, r: int) -> int:
    if l == r:
        return arr[r]
    # mid = l + ((r - l) >> 1)
    mid = (r + l) // 2
    lmax = get_max_value(arr, l, mid)
    rmax = get_max_value(arr, mid + 1, r)
    return max(lmax, rmax)


def max_value(arr: list[int]) -> int:
    return get_max_value(arr, 0, len(arr) - 1)


def main():
    arr = [1, 2, 4, 5, 6, 2, 3, 1, 0]
    sys.stdout.write(f"max value of arr is: {max_value(arr)}")


if __name__ == '__main__':
    main()
