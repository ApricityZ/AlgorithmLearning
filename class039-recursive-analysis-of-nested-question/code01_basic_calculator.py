# // 含有嵌套的表达式求值
# // 力扣上本题为会员题，所以额外提供了牛客网的测试链接
# // 如果在牛客网上提交，请将函数名从calculate改为solve
# // 测试链接 : https://leetcode.cn/problems/basic-calculator-iii/
# // 测试链接 : https://www.nowcoder.com/practice/c215ba61c8b1443b996351df929dc4d4


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 返回表达式的值
# @param s string字符串 待计算的表达式
# @return int整型
from queue import LifoQueue
from typing import Union

global where


class Solution:
    def solve(self, s: str) -> int:
        global where
        where = 0
        return self.recursive_parse(s, 0)

    def recursive_parse(self, s: str, i: int):
        global where
        # 从 i 索引位置开始
        num_stack: LifoQueue[Union[int, float]] = LifoQueue()
        op_stack: LifoQueue[str] = LifoQueue()
        cur = 0
        while i < len(s) and s[i] != ')':
            # cur = 0  # 应该在循环外初始化cur
            if '0' <= s[i] <= '9':  # 可以等于
                cur = cur * 10 + int(s[i])
                i += 1
            elif s[i] != '(':
                self.push(num_stack, op_stack, cur, s[i])
                cur = 0  # 存放之后cur要清零
                i += 1
            else:
                cur = self.recursive_parse(s, i + 1)
                i = where + 1
        self.push(num_stack, op_stack, cur, "+")
        where = i
        return self.compute(num_stack, op_stack)

    def push(self, num_stack: LifoQueue[Union[int, float]], op_stack: LifoQueue[str], cur: int, op: str):
        top_op = "" if op_stack.qsize() == 0 else op_stack.queue[-1]
        if top_op == '+' or top_op == '-' or top_op == "":
            num_stack.put(cur)
            op_stack.put(op)
        else:
            # 栈顶符号为 “*” 或者 “/”
            top_op = op_stack.get()
            top_num = num_stack.get()
            if top_op == "*":
                num = top_num * cur
            else:
                num = top_num / cur
            num_stack.put(num)
            op_stack.put(op)

    def compute(self, num_stack: LifoQueue[Union[int, float]], op_stack: LifoQueue[str]):
        ans = num_stack.queue[0]
        i = 1
        while i < num_stack.qsize():
            ans += num_stack.queue[i] if op_stack.queue[i - 1] == "+" else -num_stack.queue[i]
            i += 1  # 我们使用的是 while 循环，一定要手动改变循环变量
        return ans

ret = Solution().solve("1+2+(1-2-(-1))")
print(ret)