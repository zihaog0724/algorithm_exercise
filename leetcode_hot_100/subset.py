# hot100-lc 78. subsets

import copy


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        combination = []
        self.dfs(nums, combination, ret)
        return ret

    def dfs(self, nums, combination, ret):
        ret.append(copy.deepcopy(combination))
        if len(nums) == 0:
            return
        for i in range(len(nums)):
            combination.append(nums[i])
            self.dfs(nums[i+1:], combination, ret)
            combination.pop()

