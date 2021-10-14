# leetcode 39. combinationSum

import copy

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        combination = []
        self.dfs(combination, candidates, target)
        return self.res
        
    def dfs(self, combination, candidates, target):
        if sum(combination) == target:
            self.res.append(copy.deepcopy(combination))
            return 
        if sum(combination) > target:
            return
        for i, num in enumerate(candidates):
            combination.append(num)
            self.dfs(combination, candidates[i:], target)
            combination.pop()
