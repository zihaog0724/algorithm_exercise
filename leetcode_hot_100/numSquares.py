# hot100-lc 279. 完全平方数

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = []
        i = 1
        while i**2 <= n:
            nums.append(i**2)
            i += 1

        cols = n + 1
        rows = len(nums) + 1
        dp = [[float("inf")] * cols for _ in range(rows)]
        dp[0][0] = 0

        for i in range(1, rows):
            for j in range(cols):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-nums[i-1]] + 1)
        return dp[-1][-1]
