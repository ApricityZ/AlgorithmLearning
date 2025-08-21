# // setAll功能的哈希表
# // 测试链接 : https://www.nowcoder.com/practice/7c4559f138e74ceb9ba57d76fd169967
# // 请同学们务必参考如下代码中关于输入、输出的处理
# // 这是输入输出处理效率很高的写法
# // 提交以下的code，提交时请把类名改成"Main"，可以直接通过

import sys


class SetAllHashSet:
    def __init__(self):
        self.set_all_value = 0
        self.set_all_time = -1
        self.map = dict()
        self.time_cnt = 0  # 下一个操作的时间戳

    def put(self, k, v):
        if k in self.map:
            self.map.update({k: [v, self.time_cnt]})
        else:
            self.map[k] = [v, self.time_cnt]
        self.time_cnt += 1

    def get(self, k):
        if k in self.map:
            if self.map[k][1] > self.set_all_time:
                return self.map[k][0]
            else:
                return self.set_all_value
        else:
            return -1

    def set_all_key_value(self, v):
        self.set_all_value = v
        self.set_all_time = self.time_cnt
        self.time_cnt += 1


def main():
    nums = iter(map(int, list(sys.stdin.read().strip().split())))
    op_times = next(nums)
    set_all_hs = SetAllHashSet()
    for _ in range(op_times):
        op = next(nums)
        if op == 1:
            k = next(nums)
            v = next(nums)
            set_all_hs.put(k, v)
        elif op == 2:
            k = next(nums)
            sys.stdout.write(str(set_all_hs.get(k)) + '\n')  # 注意输出格式，要求每个输出独占一行
        else:
            v = next(nums)
            set_all_hs.set_all_key_value(v)


if __name__ == '__main__':
    main()
