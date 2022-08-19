# hot100-lc39. combinationSum

import copy

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        combination = []
        self.process(candidates, combination, target, ret)
        return ret

    def process(self, candidates, combination, target, ret):
        if sum(combination) == target:
            ret.append(copy.deepcopy(combination))
            return
        if sum(combination) > target:
            return

        for i in range(len(candidates)):
            combination.append(candidates[i])
            self.process(candidates[i:], combination, target, ret)
            combination.pop()
