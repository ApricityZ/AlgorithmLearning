# // 打印n层汉诺塔问题的最优移动轨迹

def move(n):
    if n > 0:
        recursive_move(n, "左", "右", "中")


def recursive_move(n, _from, _to, _other):
    if n == 1:
        print(f"圆盘 {n} 从 {_from} 移动到 {_to}")
    else:
        recursive_move(n - 1, _from, _other, _to)
        print(f"圆盘 {n} 从 {_from} 移动到 {_to}")
        recursive_move(n - 1, _other, _to, _from)

def main():
    move(4)

if __name__ == '__main__':
    main()
