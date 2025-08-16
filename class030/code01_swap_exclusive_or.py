# 异或运算为无进位加法，满足交换律，结合律

def swap(arr: list[int], a: int, b: int) -> None:
    arr[a] ^= arr[b]
    arr[b] ^= arr[a]
    arr[a] ^= arr[b]


def main():
    a = 10
    b = 3
    c = 8

    a ^= 0
    print(f"a ^ 0 = {a}")

    c = b ^ 0b11
    print(f"b ^ 0b11 = {c}")

    print(f"(a ^ b) ^ c = {(a ^ b) ^ c} = a ^ (b ^ c) = {a ^ (b ^ c)}")

    a ^= b
    b ^= a
    a ^= b
    print(f"a = {a}, b = {b}")

    arr = [1, 2, 3]
    swap(arr, 1, 2)
    print(f"arr = {arr}")
    swap(arr, 0, 0)
    print(f"arr = {arr}")  # arr[0] = 0, 被覆盖掉了


if __name__ == '__main__':
    main()
