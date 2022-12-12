# hot100-lc 46. 全排列

import copy


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        全排列dfs解法
        最重要的是确定递归函数里需要什么: 
        需要原输入nums用于遍历, 需要combination更新当前的组合, 还需要一个used数组, 存放已经用过的数字
        """
        self.ret = []
        self.dfs(nums, [], [])
        return self.ret

    def dfs(self, nums, combination, used):
        if len(combination) == len(nums):
            self.ret.append(copy.deepcopy(combination))
            return

        for i in range(len(nums)):
            if nums[i] not in used:
                combination.append(nums[i])
                used.append(nums[i])
                self.dfs(nums, combination, used)
                combination.pop()
                used.pop()
