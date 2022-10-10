# hot100-lc 322. 零钱兑换

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        rows = len(coins) + 1
        cols = amount + 1
        dp = [[float('inf')] * cols for _ in range(rows)]
        for i in range(rows):
            dp[i][0] = 0
        for i in range(1, rows):
            for j in range(1, cols):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]] + 1)
        ret = -1 if dp[-1][-1] == float('inf') else dp[-1][-1]
        return ret
