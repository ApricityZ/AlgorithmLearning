# // 判断一个整数是不是3的幂
# // 测试链接 : https://leetcode.cn/problems/power-of-three/

def find_max_three_power():
    ans = 1
    while True:
        if ans <= (2 ** 31 - 1) / 3:
            ans *= 3
        else:
            break
    print(ans)
print(2 ** 31 - 1)
find_max_three_power()

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (1162261467 % n == 0)