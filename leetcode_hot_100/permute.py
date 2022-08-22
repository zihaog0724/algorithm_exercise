# hot100-lc 46. permute

import copy

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        combination = []
        used = []
        self.process(nums, ret, used, combination)
        return ret

    def process(self, nums, ret, used, combination):
        if len(combination) == len(nums):
            ret.append(copy.deepcopy(combination))
            return

        for i in range(len(nums)):
            if nums[i] in used:
                continue
            combination.append(nums[i])
            used.append(nums[i])
            self.process(nums, ret, used, combination)
            combination.pop()
            used.pop()
