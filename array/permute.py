# leetcode 46. permute

import copy

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        used = []
        self.backtrack(nums, path, used, res)
        return res
    
    def backtrack(self, nums, path, used, res):
        if len(path) == len(nums):
            res.append(copy.deepcopy(path))
            return
        
        for i in range(len(nums)):
            if nums[i] in used:
                continue
            path.append(nums[i])
            used.append(nums[i])
            self.backtrack(nums, path, used, res)
            path.pop()
            used.pop()
