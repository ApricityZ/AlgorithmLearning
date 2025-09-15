# 描述
# 字典树又称为前缀树或者Trie树，是处理字符串常用的数据结构。假设组成所有单词的字符仅是‘a’～‘z’，请实现字典树的结构，并包含以下四个主要的功能。
# void insert(String word)：添加word，可重复添加；
# void delete(String word)：删除word，如果word添加过多次，仅删除一次；
# boolean search(String word)：查询word是否在字典树中出现过(完整的出现过，前缀式不算)；
# int prefixNumber(String pre)：返回以字符串pre作为前缀的单词数量。
# 现在给定一个m，表示有m次操作，每次操作都为以上四种操作之一。每次操作会给定一个整数op和一个字符串word，op代表一个操作码，如果op为1，则代表添加word，
# op为2则代表删除word，op为3则代表查询word是否在字典树中，op为4代表返回以word为前缀的单词数量（数据保证不会删除不存在的word）。

# 输入描述： 输入包含多行，第一行一个整数m ( 1 ≤ 𝑚 ≤ 1 0 5 ) (1≤m≤10 5 )，代表操作次数。
# 接下来m行，每行包含一个整数op ( 1 ≤ 𝑜 𝑝 ≤ 4 ) (1≤op≤4)，和一个字符串word ( 1 ≤ 𝑙 𝑒 𝑛 𝑔 𝑡 ℎ 𝑤 𝑜 𝑟 𝑑 ≤ 20 ) (1≤length word ≤20)。

# 输出描述： 对于每次操作，如果op为3时，如果word在字典树中，请输出“YES”，否则输出“NO”；如果op为4时，请输出返回以word为前缀的单词数量，其它情况不输出。

# // 用固定数组实现前缀树，空间使用是静态的。推荐！
# // 测试链接 : https://www.nowcoder.com/practice/7f8a8553ddbf4eaab749ec988726702b
# // 请同学们务必参考如下代码中关于输入、输出的处理
# // 这是输入输出处理效率很高的写法
# // 提交以下的code，提交时请把类名改成"Main"，可以直接通过
import sys


class Trie:
    def __init__(self):
        self.max_len = 150001
        self.tree = [[0] * 26 for _ in range(self.max_len)]
        self.pass_times = [0] * self.max_len
        self.end_times = [0] * self.max_len
        self.root = 1
        self.zero_idx = ord('a')
        self.cnt = 1

    def insert(self, word: str) -> None:
        cur = self.root
        self.pass_times[cur] += 1
        for char in word:
            path_idx = ord(char) - self.zero_idx
            if self.tree[cur][path_idx] == 0:
                new_node_idx = self.cnt + 1
                self.cnt += 1  # 指针忘记移动了
                self.tree[cur][path_idx] = new_node_idx
            cur = self.tree[cur][path_idx]
            self.pass_times[cur] += 1
        self.end_times[cur] += 1

    def delete(self, word: str) -> None:
        if self.search(word):
            cur = self.root
            self.pass_times[cur] -= 1
            for char in word:
                path_idx = ord(char) - self.zero_idx
                next_node = self.tree[cur][path_idx]
                self.pass_times[next_node] -= 1
                if self.pass_times[next_node] == 0:
                    self.tree[cur][path_idx] = 0  # 因为insert时总是再增加self.cnt，不用担心计数污染的问题
                    return
                cur = next_node
            self.end_times[cur] -= 1

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            path_idx = ord(char) - self.zero_idx
            if self.tree[cur][path_idx] == 0:
                return False
            cur = self.tree[cur][path_idx]
        # return True  # 这里不对 ， 我们要判定是否为完整单词，现在可能存在完整路径，但只是其他单词的一部分，要使用end times判定
        return self.end_times[cur] > 0

    def prefixNumber(self, pre: str) -> int:
        cur = self.root
        for char in pre:
            path_idx = ord(char) - self.zero_idx
            if self.tree[cur][path_idx] == 0:
                return 0
            cur = self.tree[cur][path_idx]
        return self.pass_times[cur]

    def clear(self):
        # self.tree.clear()
        # self.pass_times.clear()
        # self.end_times.clear()
        self.tree = [[0] * 26 for _ in range(self.max_len)]
        self.pass_times = [0] * self.max_len
        self.end_times = [0] * self.max_len
        self.root = 1
        self.cnt = 1


# def main():
#     trie = Trie()
#     inputs = iter(sys.stdin.readlines())
#     line = next(inputs)
#     while line:
#         m = int(line)
#         for _ in range(m):
#             line = next(inputs)
#             op, input_str = line.split()
#             if op == 1:
#                 trie.insert(input_str)
#             elif op == 2:
#                 trie.delete(input_str)
#             elif op == 3:
#                 sys.stdout.write('YES') if trie.search(input_str) else sys.stdout.write('NO')
#             elif op == 4:
#                 sys.stdout.write(str(trie.prefixNumber(input_str)))
#         trie.clear()

def main():
    data = sys.stdin.buffer.read().split()
    # data: [m, op, word, op, word, ..., m, ...]
    it = iter(data)
    out_lines = []
    trie = Trie()

    while True:
        try:
            m = int(next(it))
        except StopIteration:
            break

        # 如果题目是“只有一组 m”，这段也 OK；如果是多组 m，也能依次处理
        # 如需每组清空一遍（通常不需要），可以在这里： trie.clear()

        for _ in range(m):
            op = int(next(it))
            word = next(it).decode()
            if op == 1:
                trie.insert(word)
            elif op == 2:
                trie.delete(word)
            elif op == 3:
                out_lines.append("YES" if trie.search(word) else "NO")
            elif op == 4:
                out_lines.append(str(trie.prefixNumber(word)))
            else:
                # 非法操作码（一般不会出现）
                pass

    sys.stdout.write("\n".join(out_lines))


if __name__ == '__main__':
    main()
