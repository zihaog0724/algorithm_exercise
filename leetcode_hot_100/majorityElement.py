# hot100-lc 169. 多数元素

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dic = dict()
        ret = 0
        for i in nums:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1
            if dic[i] / n > 0.5:
                ret = i
        return ret
