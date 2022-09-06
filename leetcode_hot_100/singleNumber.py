# hot100-lc 136. singleNumber

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic.keys():
                dic[nums[i]] = 1
            else:
                dic.pop(nums[i])
        return list(dic.keys())[0]
