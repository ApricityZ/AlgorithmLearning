# 这是您需要提交到平台的“填函数”风格代码
# 平台会自动创建 Solution 类的实例，并调用 sumOfSubMatrix 方法
# // 展示填函数风格的测试方式
# // 子矩阵的最大累加和问题，不要求会解题思路，后面的课会讲
# // 测试链接 : https://www.nowcoder.com/practice/840eee05dccd4ffd8f9433ce8085946b

class Solution:
    def sumOfSubMatrix(self, mat: list[list[int]], n: int) -> int:
        """
        这是你需要填充的主函数，接口与 Java 示例保持一致。
        这里的 'n' 根据原始接口，代表这是一个 n*n 的方阵。
        这个函数直接调用了核心逻辑函数。
        """
        # 原始 Java 代码的 `sumOfSubMatrix` 调用了 `maxSumSubmatrix(mat, n, n)`
        # 我们在这里也保持同样的行为
        # 注意：这里的 m 就等于 n
        return self.max_sum_submatrix(mat, n, n)

    @staticmethod
    def max_sum_subarray(arr: list[int]) -> int:
        """
        辅助方法1：求一维数组的最大子数组和 (Kadane's 算法)。
        这完全对应 Java 代码中的 `maxSumSubarray` 静态方法。
        使用 @staticmethod 装饰器表示这是一个静态方法，可以不通过实例调用。
        """
        # 使用 -float('inf') 对应 Java 的 Integer.MIN_VALUE
        # 这样可以正确处理数组元素全部为负数的情况
        max_val = -float('inf')
        cur_sum = 0
        for num in arr:
            cur_sum += num
            max_val = max(max_val, cur_sum)
            # 如果当前累加和变为负数，则从下一位置重新开始计算
            cur_sum = 0 if cur_sum < 0 else cur_sum
        return max_val

    def max_sum_submatrix(self, mat: list[list[int]], n: int, m: int) -> int:
        """
        辅助方法2：计算子矩阵最大累加和的核心逻辑。
        这完全对应 Java 代码中的 `maxSumSubmatrix` 方法。
        """
        max_global = -float('inf')

        # 循环，固定子矩阵的“上边界”
        for i in range(n):
            # 这是“压缩”后的一维数组，每次更换上边界时都重置
            compressed_arr = [0] * m

            # 循环，固定子矩阵的“下边界”
            for j in range(i, n):
                # 把当前下边界所在行的数据，累加到压缩数组中
                for k in range(m):
                    compressed_arr[k] += mat[j][k]

                # 在“压缩”后的一维数组上求解最大子数组和，并更新全局最大值
                max_global = max(max_global, self.max_sum_subarray(compressed_arr))

        return max_global