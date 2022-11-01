# hot100-lc 560. 和为K的子数组

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # preSum = [0]
        # s = 0
        # for i in nums:
        #     s += i
        #     preSum.append(s)
        #
        # ret = 0
        # # preSum[i] ~ [0, i-1]的和
        # for i in range(1, len(preSum)):
        #     for j in range(i):
        #         # [j, i-1]的和
        #         # if (preSum[i] - preSum[j]) == k:
        #         #     ret += 1
        #         if preSum[j] == (preSum[i] - k):
        #             ret += 1

        ret = 0
        sums = 0
        preSum = {0: 1}
        for i in nums:
            sums += i
            if (sums - k) in preSum:
                ret += preSum[sums - k]
            if sums in preSum:
                preSum[sums] += 1
            else:
                preSum[sums] = 1
        return ret
