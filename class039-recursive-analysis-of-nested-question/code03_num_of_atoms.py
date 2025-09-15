# // 含有嵌套的分子式求原子数量
# // 测试链接 : https://leetcode.cn/problems/number-of-atoms/

class Solution:
    def __init__(self):
        self.where = 0

    def countOfAtoms(self, formula: str) -> str:
        # ans: dict[str, int] = dict()
        # self.recursive_count1(formula, 0, ans)
        ans = self.recursive_count(formula, 0)
        ans_str = []
        for name, val in sorted(ans.items()):
            # ans_str.extend([name, str(val)])
            ans_str.append(name)
            if val > 1:
                ans_str.append(str(val))
        return "".join(map(str, ans_str))

    # wrong ans
    def recursive_count1(self, formula: str, i: int, ans: dict[str, int]) -> dict[str, int]:
        repeat_times = 0
        local_dict: dict[str, int] = dict()
        name: str = ""
        while i < len(formula) and formula[i] != ')':
            if 'A' <= formula[i] <= 'Z':
                self.update_ans(name, local_dict, repeat_times, ans)
                repeat_times = 0
                local_dict = dict()
                name = formula[i]
                i += 1
            elif 'a' <= formula[i] <= 'z':
                name += formula[i]
                i += 1
            elif formula[i] != '(':
                repeat_times += repeat_times * 10 + int(formula[i])
                i += 1
            else:
                self.update_ans(name, local_dict, repeat_times, ans)
                repeat_times = 0
                name = ""
                local_dict: dict[str, int] = self.recursive_count(formula, i + 1, ans)
                i = self.where + 1
        self.where = i
        return local_dict

    def recursive_count(self, formula: str, i: int) -> dict[str, int]:
        repeat_times = 0
        ans: dict[str, int] = dict()
        name: str = ""
        local_dict: dict[str, int] = dict()
        while i < len(formula) and formula[i] != ')':
            if 'A' <= formula[i] <= 'Z' or formula[i] == "(":
                self.update_ans(name, local_dict, repeat_times, ans)
                repeat_times = 0
                name = ""
                local_dict = dict()
                if 'A' <= formula[i] <= 'Z':
                    name = formula[i]
                    i += 1
                else:
                    local_dict = self.recursive_count(formula, i + 1)
                    i = self.where + 1
            elif 'a' <= formula[i] <= 'z':
                name += formula[i]
                i += 1
            else:
                repeat_times = repeat_times * 10 + int(formula[i])
                i += 1
        self.where = i
        # ans.update({name: 1})
        self.update_ans(name, local_dict, repeat_times, ans)
        return ans

    def update_ans(self, name: str, local_dict: dict[str, int], repeat_times: int, ans: dict[str, int]):
        # 第一个位置字母，此时name和local_dict均为空
        if name == "" and len(local_dict) == 0:
            return
        repeat_times = 1 if repeat_times == 0 else repeat_times
        if name:
            ans.update({name: ans.get(name, 0) + repeat_times})
        else:
            for name, val in local_dict.items():
                ans.update({name: ans.get(name, 0) + local_dict.get(name) * repeat_times})


print(Solution().countOfAtoms("Mg(OH)2"))
