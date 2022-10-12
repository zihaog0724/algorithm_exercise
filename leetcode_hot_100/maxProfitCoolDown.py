# hot100-lc 309. 买卖股票最佳时机含冷冻期

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        dp = [[0] * len(prices) for _ in range(4)]
        """
        dp[0][i]: 第i天不持有，i-1天未持有，第i天不买
        dp[1][i]: 第i天不持有，i-1天持有，第i天卖掉
        dp[2][i]: 第i天持有，i-1天不持有，第i天买
        dp[3][i]: 第i天持有，i-1天持有，第i天不卖
        """

        # 初始化，第0天持有的话，相当于收益为负数
        dp[2][0], dp[3][0] = -1 * prices[0], -1 * prices[0]

        for i in range(1, len(prices)):
            # 第i天不持有，i-1天未持有，第i天不买，不用考虑冷冻期
            dp[0][i] = max(dp[0][i-1], dp[1][i-1])
            # 第i天不持有，i-1天持有，第i天卖掉
            dp[1][i] = max(dp[2][i-1], dp[3][i-1]) + prices[i]
            # 第i天持有，i-1天不持有，第i天买，需要考虑冷冻期，i-1天不持有且不能卖
            dp[2][i] = dp[0][i-1] - prices[i]
            # 第i天持有，i-1天持有，第i天不卖
            dp[3][i] = max(dp[2][i-1], dp[3][i-1])

        return max(dp[0][-1], dp[1][-1])
