from typing import List

import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os


def calculaeGini(wealth):
    # sumOfAbsolutionDifferences = 0
    # sumOfWealth = 0
    n = len(wealth)
    # for i in range(n):
    #     sumOfWealth += wealth[i]
    #     for j in range(n):
    #         sumOfAbsolutionDifferences += abs(wealth[i] - wealth[j])
    diff_matrix = np.abs(wealth[:, None] - wealth[None, :])

    # return sumOfAbsolutionDifferences / (2 * n * sumOfWealth)
    return diff_matrix.sum() / (2 * n * wealth.sum())


def plot_wealth_distribution(wealth, step, save_dir="frames"):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    plt.figure(figsize=(12, 5))
    plt.bar(range(len(wealth)), wealth)
    plt.title(f"Wealth Distribution at Step {step}")
    plt.xlabel("Person Index (sorted by wealth)")
    plt.ylabel("Wealth")
    plt.tight_layout()
    plt.grid(True, linestyle='--', alpha=0.3)

    filename = os.path.join(save_dir, f"frame_{step:07d}.png")
    plt.savefig(filename)
    plt.close()  # ✅ 不弹出窗口


def experiment(n, t, plot_interval=100):
    wealth = np.ones(100) * 100
    has_money = np.zeros_like(wealth)
    for step in range(t):
        # has_money = np.zeros_like(wealth)
        # for j in range(n):
        #     if wealth[j] > 0:
        #         has_money[j] = True
        has_money = wealth > 0
        for k in range(n):
            if has_money[k]:
                other = k
                while other == k:
                    # other = int(np.random.random() * n)
                    other = np.random.randint(n)
                wealth[k] -= 1
                wealth[other] += 1

        if step % plot_interval == 0:
            plot_wealth_distribution(wealth, step)

    sorted_wealth = np.sort(wealth)
    print("列出每个人从贫穷到富有的财富值：")
    for i in range(n):
        print(sorted_wealth[i])
        if i % 10 == 9:
            print('\n')

    print(f"这个社会的基尼系数为：{calculaeGini(wealth)}")


def create_gif_from_frames(save_dir="frames", gif_name="wealth_evolution.gif", fps=2):
    frames = sorted([
        os.path.join(save_dir, f) for f in os.listdir(save_dir)
        if f.endswith(".png")
    ])
    images = [imageio.imread(frame) for frame in frames]
    imageio.mimsave(gif_name, images, fps=fps)
    print(f"GIF saved to {gif_name}")


def main(n=100, t=1000000):
    print("一个社会的基尼系数是一个在0~1之间的小数")
    print("基尼系数为0代表所有人的财富完全一样")
    print("基尼系数为1代表有1个人掌握了全社会的财富")
    print("基尼系数越小，代表社会财富分布越均衡；越大则代表财富分布越不均衡")
    print("在2022年，世界各国的平均基尼系数为0.44")
    print("目前普遍认为，当基尼系数到达 0.5 时")
    print("就意味着社会贫富差距非常大，分布非常不均匀")
    print("社会可能会因此陷入危机，比如大量的犯罪或者经历社会动荡")
    print("测试开始")
    print(f"人数：{n}")
    print(f"轮数：{t}")
    experiment(n, t)
    create_gif_from_frames()
    print("测试结束")


if __name__ == '__main__':
    main()
