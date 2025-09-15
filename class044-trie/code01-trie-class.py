from typing import Optional

from sympy.solvers.ode.lie_group import lie_heuristics


class TrieNode:
    def __init__(self):
        self.pass_times: int = 0
        self.end_times: int = 0
        self.next: list[TrieNode | None] = [None] * 26


class Trie1:
    def __init__(self):
        self.root = TrieNode()
        self.zero_idx_char_a = ord('a')

    def inset(self, s: str):
        cur = self.root
        cur.pass_times += 1
        for char in list(s):
            path_idx = ord(char) - self.zero_idx_char_a
            if cur.next[path_idx] is None:
                cur.next[path_idx] = TrieNode()
                # cur.pass_times += 1  # 我们应该增加新建节点的 pass times ，现在会重复增加cur节点的pass times
            cur = cur.next[path_idx]
            cur.pass_times += 1  # 写在这里是正确的
        cur.end_times += 1

    def count_with_prefix(self, s):
        cur = self.root
        for char in list(s):
            path_idx = ord(char) - self.zero_idx_char_a
            if cur.next[path_idx] is None:
                return 0
            cur = cur.next[path_idx]
        return cur.pass_times

    def count_string_num(self, s):
        cur = self.root
        for char in list(s):
            path_idx = ord(char) - self.zero_idx_char_a
            if cur.next[path_idx] is None:
                return 0
            cur = cur.next[path_idx]
        return cur.end_times

    # def delete(self, s):
    #     if self.count_string_num(s) > 0:
    #         cur = self.root
    #         for char in list(s):
    #             path_idx = ord(char) - self.zero_idx_char_a
    #             if cur.next[path_idx].pass_times == 1:
    #                 cur.next[path_idx] = None
    #                 return
    #             cur.pass_times -= 1
    #             cur = cur.next[path_idx]
    #         cur.pass_times -= 1  #  一定要注意这个循环中的cur是当前还是下一个节点，如果我们没有在45行让passtime减一，那么就要在最后减一，注意首尾节点的处理
    #         # 现在的函数是错误的，我们需要现在45行后循环前直接减一，否则进入48分支后，root节点pass time 没有正确处理
    #         cur.end_times -= 1

    def delete(self, s):
        """
        删除字符串 s 一次。
        如果 s 不存在，则不操作。

        注意：本方法保证“状态一致性”：
        - 所有被访问的节点，在删除前都会先执行 pass_times -= 1
        - 再判断 pass_times 是否为 0
        - 这样能确保：任何被删除的节点，其 pass_times 都已正确更新为 0
        - 避免出现“节点被删但计数未更新”的逻辑不一致问题
        - 此设计有利于调试、日志、节点复用等未来扩展
        """
        if self.count_string_num(s) > 0:
            cur = self.root
            cur.pass_times -= 1
            for char in list(s):
                path_idx = ord(char) - self.zero_idx_char_a
                next_node = cur.next[path_idx]
                next_node.pass_times -= 1
                if next_node.pass_times == 0:
                    cur.next[path_idx] = None
                    return
                cur = next_node
            cur.end_times -= 1


# def delete(self, s: str):
#     """
#     删除字符串 s 一次。
#     如果 s 不存在，则不操作。
#
#     注意：本方法保证“状态一致性”：
#     - 所有被访问的节点，在删除前都会先执行 pass_times -= 1
#     - 再判断 pass_times 是否为 0
#     - 这样能确保：任何被删除的节点，其 pass_times 都已正确更新为 0
#     - 避免出现“节点被删但计数未更新”的逻辑不一致问题
#     - 此设计有利于调试、日志、节点复用等未来扩展
#     """
#     if self.count_string_num(s) == 0:
#         return
#
#     cur = self.root
#     cur.pass_times -= 1  # 根节点引用数减一
#
#     for char in s:
#         path_idx = ord(char) - self.zero_idx_char_a
#         next_node = cur.next[path_idx]
#
#         # ✅ 先减少引用计数，保证状态一致性
#         next_node.pass_times -= 1
#
#         # ✅ 再判断是否为0，决定是否删除
#         if next_node.pass_times == 0:
#             cur.next[path_idx] = None  # 释放引用
#             return  # 提前返回，后续路径由 GC 回收
#
#         cur = next_node
#
#     # 完整匹配，减少结尾计数
#     cur.end_times -= 1


# 📝 注释说明：
# “状态一致性” 是工程中的重要概念：
#
# 指系统在每一步操作后，内部数据结构都保持逻辑自洽，不会出现“中间状态错误”。
# 你的 delete 方法通过 “先减计数，再删节点”，确保了：
# 被删节点的 pass_times 一定是 0
# 不会出现“计数虚高但节点已删”的矛盾
# 未来加日志、调试、复用节点时不会出错


class TrieNode2:
    def __init__(self):
        self.pass_times = 0
        self.end_times = 0
        # self.next: Optional[dict[int, TrieNode2]] = None  # 应该初始化为字典
        self.next = dict()


class Trie2:
    def __init__(self):
        self.root = TrieNode2()
        self.zero_index = ord('a')

    def insert(self, s: str):
        if not s:
            return
        cur = self.root
        cur.pass_times += 1
        for char in s:
            path_idx = ord(char) - self.zero_index
            if path_idx not in cur.next:
                cur.next.update({path_idx: TrieNode2()})
                # cur = cur.next[path_idx]
            cur = cur.next[path_idx]  # 统一移动
            cur.pass_times += 1
        cur.end_times += 1

    def count_start_with_prefix(self, prefix: str):
        if not prefix:
            return 0
        cur = self.root
        for char in prefix:
            path_idx = ord(char) - self.zero_index
            # if not path_idx in cur.next:  # 语法虽然合法，但风格不好，建议用 not in 而不是 not ... in。更重要的是：如果 cur.next 是 None，会崩溃
            if path_idx not in cur.next:
                return 0
            cur = cur.next[path_idx]
        return cur.pass_times

    def count_string_equal_to(self, s: str):
        if not s:
            return 0
        cur = self.root
        for char in s:
            path_idx = ord(char) - self.zero_index
            # if not path_idx in cur.next:  # 同上
            if path_idx not in cur.next:
                return 0
            cur = cur.next[path_idx]
        return cur.end_times

    def erase(self, s: str):
        if not s:
            raise ValueError("Illegal input")

        if self.count_string_equal_to(s) > 0:
            cur = self.root
            cur.pass_times -= 1
            for char in s:
                path_idx = ord(char) - self.zero_index
                next_node = cur.next[path_idx]
                next_node.pass_times -= 1
                if next_node.pass_times == 1:  # 优化内存，当节点的pass time 为0时，删除该节点以及之后的路径
                    del cur.next[path_idx]
                    return
                cur = next_node
            cur.end_times -= 1


def test_trie2():
    trie = Trie2()
    trie.insert("abc")
    trie.insert("abd")
    trie.insert("a")

    print(trie.count_start_with_prefix("ab"))  # 2
    print(trie.count_string_equal_to("abc"))  # 1

    trie.erase("abc")
    print(trie.count_string_equal_to("abc"))  # 0
    print(trie.count_start_with_prefix("ab"))  # 1

    trie.erase("abd")
    print(trie.count_start_with_prefix("ab"))  # 0

    trie.erase("a")
    print(trie.count_string_equal_to("a"))  # 0


test_trie2()
