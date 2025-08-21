# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
#
# 例如 arr = [2,3,4] 的中位数是 3 。
# 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
# 实现 MedianFinder 类:
#
# MedianFinder() 初始化 MedianFinder 对象。
#
# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
#
# double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。
import heapq


# 	// 测试链接 : https://leetcode.cn/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0 or -self.max_heap[0] >= num:  # 注意我们在使用大根堆的时候，将所有元素变成了相反数，用的时候要取反
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        self.balance()

    def balance(self):
        if abs(len(self.min_heap) - len(self.max_heap)) == 2:
            if len(self.max_heap) > len(self.min_heap):
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            else:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return self.min_heap[0] if len(self.min_heap) > len(self.max_heap) else -self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
