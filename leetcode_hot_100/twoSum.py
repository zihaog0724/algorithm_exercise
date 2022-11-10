# hot100-lc 1. 两数之和

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        做一个dict{value: idx}, 遍历数组nums, 算差值，在dict里找这个差值
        用空间换时间
        """
        dct = {}
        for i, value in enumerate(nums):
            dct[value] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dct:
                if dct[diff] != i:
                    return [i, dct[diff]]
