# hot100-lc 312. 戳气球

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for _ in range(len(nums))]

        for interval in range(2, len(nums)):
            for i in range(len(nums)):
                j = i + interval
                if j < len(nums):
                    for k in range(i + 1, j):
                        dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        return dp[0][-1]
