import numpy


# // 峰值元素是指其值严格大于左右相邻值的元素
# // 给你一个整数数组 nums，已知任何两个相邻的值都不相等
# // 找到峰值元素并返回其索引
# // 数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
# // 你可以假设 nums[-1] = nums[n] = 无穷小
# // 你必须实现时间复杂度为 O(log n) 的算法来解决此问题
# // 测试链接 : https://leetcode.cn/problems/find-peak-element/
def find_peak_element(arr):
    max_index = len(arr) - 1
    if arr is None or max_index == 0:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[max_index] > arr[max_index - 1]:
        return max_index
    l, r, ans = 1, max_index - 1, -1
    while l <= r:
        mid = l + ((r - l) >> 1)
        lm = mid - 1
        rm = mid + 1
        if arr[mid] > arr[lm] and arr[mid] > arr[rm]:
            ans = mid
            break
        elif arr[lm] > arr[mid] > arr[rm]:
            r = mid - 1
        else:
            l = mid + 1

    return ans
