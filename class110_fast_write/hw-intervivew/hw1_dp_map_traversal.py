import sys

def solve_map_crossing():
    """
    使用动态规划解决地图穿越问题。
    """
    # --- 1. 输入读取与参数校验 ---
    try:
        lines = sys.stdin.readlines()
        if not lines:
            print(-2)
            return

        k_str = lines[0].strip()
        # 检查 K 是否为有效正整数
        if not k_str.isdigit() or int(k_str) <= 0:
            print(-2)
            return
        k = int(k_str)

        if k > 100:
            print(-2)
            return

        map_lines = lines[1:]
        # 检查行数是否匹配
        if len(map_lines) != k:
            print(-2)
            return

        game_map = []
        for line in map_lines:
            row_str = line.strip().split()
            # 检查列数是否匹配
            if len(row_str) != k:
                print(-2)
                return

            row = []
            for val_str in row_str:
                # 检查地图元素是否为有效数字及范围
                if not val_str.isdigit():
                    print(-2)
                    return
                val = int(val_str)
                if not (0 <= val <= 10):
                    print(-2)
                    return
                row.append(val)
            game_map.append(row)

    except (ValueError, IndexError):
        # 捕获所有潜在的格式错误
        print(-2)
        return

    # --- 2. DP 数组初始化 ---
    # dp[r][c] 表示到达 (r, c) 的最小体力消耗
    dp = [[float('inf')] * k for _ in range(k)]

    # 起点 (0, 0) 的消耗就是其自身的高度值
    dp[0][0] = game_map[0][0]

    # --- 3. 填充 DP 数组 ---
    for r in range(k):
        for c in range(k):
            # 跳过已经初始化的起点
            if r == 0 and c == 0:
                continue

            # 计算从上方 (r-1, c) 移动过来的可能消耗
            cost_from_up = float('inf')
            if r > 0 and abs(game_map[r][c] - game_map[r-1][c]) <= 1:
                cost_from_up = dp[r-1][c]

            # 计算从左方 (r, c-1) 移动过来的可能消耗
            cost_from_left = float('inf')
            if c > 0 and abs(game_map[r][c] - game_map[r][c-1]) <= 1:
                cost_from_left = dp[r][c-1]

            # 取两个来源中的最小消耗
            min_prev_cost = min(cost_from_up, cost_from_left)

            # 如果该点可以通过上方或左方到达
            if min_prev_cost != float('inf'):
                dp[r][c] = game_map[r][c] + min_prev_cost

    # --- 4. 寻找最终结果 ---
    # 结果是最后一列中的最小值
    min_total_cost = float('inf')
    for r in range(k):
        min_total_cost = min(min_total_cost, dp[r][k-1])

    # --- 5. 输出结果 ---
    if min_total_cost == float('inf'):
        print(-1)  # 无法到达右侧
    else:
        print(int(min_total_cost))


# 执行函数
solve_map_crossing()