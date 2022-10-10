# hot100-lc 494. 目标和

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total = sum(nums)
        if abs(target) > total:
            return 0
        if (total + target) % 2 != 0:
            return 0

        pos = (total + target) // 2
        rows = len(nums) + 1
        cols = pos + 1
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = 1
        for i in range(1, rows):
            for j in range(cols):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
        return dp[-1][-1]
