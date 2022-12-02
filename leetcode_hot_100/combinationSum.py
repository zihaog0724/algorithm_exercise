# hot100-lc 39. 组合总和


import copy


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """
        dfs题解见https://zhuanlan.zhihu.com/p/556482306
        """
        self.ret = []
        self.dfs(candidates, target, [])
        return self.ret

    def dfs(self, candidates, target, combination):
        if sum(combination) == target:
            self.ret.append(copy.deepcopy(combination))
            return
        if sum(combination) > target:
            return

        for i in range(len(candidates)):
            combination.append(candidates[i])
            self.dfs(candidates[i:], target, combination)
            combination.pop()
