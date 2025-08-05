# // 无序数组中第K大的元素
# // 测试链接 : https://leetcode.cn/problems/kth-largest-element-in-an-array/
import random


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        value = randomized_select(arr=nums, i=len(nums) - k)
        return value


def randomized_select(arr, i):
    l = 0
    r = len(arr) - 1
    ans = 0
    while l <= r:
        first, last = partition(arr, l, r, arr[random.randint(l, r)])
        if i < first:
            r = first - 1
        elif i > last:
            l = last + 1
        else:
            ans = arr[i]
            break
    return ans


def partition(arr, l, r, x):
    a = l
    b = r
    i = l
    while i <= b:
        if arr[i] < x:
            swap(arr, i, a)
            i += 1
            a += 1
        elif arr[i] == x:
            i += 1
        else:
            swap(arr, i, b)
            b -= 1
    return a, b


def swap(arr, l, r):
    tmp = arr[l]
    arr[l] = arr[r]
    arr[r] = tmp
