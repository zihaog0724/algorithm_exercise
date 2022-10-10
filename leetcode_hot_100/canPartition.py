# hot100-lc 416. 分割等和子集

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        if max(nums) > target:
            return False

        rows = len(nums) + 1
        cols = target + 1
        dp = [[False] * cols for _ in range(rows)]
        for i in range(0, rows):
            dp[i][0] = True

        for i in range(1, rows):
            for j in range(1, cols):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[-1][-1]
