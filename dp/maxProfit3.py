# leetcode 123. 买卖股票最佳时机3

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        """
        五种状态
        dp[i][0]: 第i天的状态为一直没操作
        dp[i][1]: 第i天的状态为第一次买入，可能为i-1天的状态是一直没操作，第i天买入；或i-1天的状态是第一次买入
        dp[i][2]: 第i天的状态为第一次卖出，可能为i-1天的状态第一次买入，第i天卖出；或i-1天的状态是第一次卖出
        dp[i][3]: 第i天的状态为第二次买入，可能为i-1天的状态第一次卖出，第i天买入；或i-1天的状态是第二次买入
        dp[i][4]: 第i天的状态为第二次卖出，可能为i-1天的状态第二次买入，第i天卖出；或i-1天的状态是第二次卖出
        """
        dp = [[0] * 5 for _ in range(len(prices))]
        dp[0][1] = -1 * prices[0]
        dp[0][3] = -1 * prices[0]
        
        for i in range(1, len(prices)):
            # dp[i][0] = dp[i-1][0] = 0 恒成立，就不更新了
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
        return max(dp[-1])
