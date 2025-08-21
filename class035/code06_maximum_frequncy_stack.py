# 设计一个类似堆栈的数据结构，将元素推入堆栈，并从堆栈中弹出出现频率最高的元素。
#
# 实现 FreqStack 类:
#
# FreqStack() 构造一个空的堆栈。
# void push(int val) 将一个整数 val 压入栈顶。
# int pop() 删除并返回堆栈中出现频率最高的元素。
# 如果出现频率最高的元素不只一个，则移除并返回最接近栈顶的元素。

# 	// 测试链接 : https://leetcode.cn/problems/maximum-frequency-stack/

class FreqStack:

    def __init__(self):
        self.max_times_count: int = 0
        self.stack_map_times_list: dict[int, list[int]] = dict()
        self.map_val_times: dict[int, int] = dict()

    def push(self, val: int) -> None:
        self.map_val_times[val] = self.map_val_times.setdefault(val, 0) + 1
        cur_val_time: int = self.map_val_times[val]
        # self.stack_map_times_list.setdefault(val, list()).append(val)  #  这个字典的key应该是出现次数，而不是值
        self.stack_map_times_list.setdefault(cur_val_time, list()).append(val)
        # self.map_val_times = max(self.max_times_count, cur_val_time)  # 变量名称写混了
        self.max_times_count = max(self.max_times_count, cur_val_time)

    def pop(self) -> int:
        if len(self.map_val_times) == 0:
            raise KeyError("No element to pop")
        max_times_val_list: list[int] = self.stack_map_times_list[self.max_times_count]
        ans: int = max_times_val_list.pop()
        if len(max_times_val_list) == 0:
            del self.stack_map_times_list[self.max_times_count]
            self.max_times_count -= 1
        self.map_val_times[ans] -= 1  # 对应的，这里的词频统计要减少1，否则在计算新的self.max_times_count会出错，关键是多个数据结构之间的统计量要同步！！！！
        if self.map_val_times[ans] == 0:
            del self.map_val_times[ans]
        return ans


# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(4)
obj.push(0)
obj.push(9)
obj.push(3)
obj.push(4)
obj.push(2)

param_1 = obj.pop()

obj.push(6)

obj.pop()

obj.push(1)

obj.pop()

obj.push(1)

obj.pop()

obj.push(4)

obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()

param_2 = obj.pop()
