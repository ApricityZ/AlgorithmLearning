# // 草一共有n的重量，两只牛轮流吃草，A牛先吃，B牛后吃
# // 每只牛在自己的回合，吃草的重量必须是4的幂，1、4、16、64....
# // 谁在自己的回合正好把草吃完谁赢，根据输入的n，返回谁赢

class EatGrass:
    def win(self, n: int) -> str:
        """
        主函数，调用递归函数
        :param n: 草的总分数
        :return: 获胜者
        """
        return self.recursive_decide(n, "A")

    def recursive_decide(self, n: int, cur: str) -> str:
        """
        还剩 n 份草，当前是cur的轮次要吃草（先手）
        :param n: 剩余的草的份数
        :param cur: 当前轮到谁吃草
        :return: 谁获胜了
        """
        # base case
        enemy = "B" if cur == "A" else "A"
        if n < 5:
            return enemy if (n == 0 or n == 2) else cur
        # recursion
        grass = 1
        while grass < n:
            if self.recursive_decide(n - grass, enemy) == cur:
                return cur
            grass *= 4
        return enemy


def find_pattern():
    for i in range(100):
        print(f" {i}: {EatGrass().win(i)}")


# find_pattern()


def win(n, cur="A"):
    enemy = "B" if cur == "A" else "A"
    res = n % 5
    if res == 0 or res == 2:
        return enemy
    else:
        return cur


def test():
    for i in range(60):
        if EatGrass().win(i) != win(i):
            print("Error")
    print("Finished!")


test()
