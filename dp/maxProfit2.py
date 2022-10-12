# leetcode 122. 买卖股票最佳时机2

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        dp = [[0] * 4 for _ in range(len(prices))]
        """
        dp[i][0]: 第i天不持有，i-1天未持有，第i天不买
        dp[i][1]: 第i天不持有，i-1天持有，第i天卖掉
        dp[i][2]: 第i天持有，i-1天不持有，第i天买
        dp[i][3]: 第i天持有，i-1天持有，第i天不卖
        """

        # 初始化，第0天持有的话，相当于收益为负数
        dp[0][2], dp[0][3] = -1 * prices[0], -1 * prices[0]

        for i in range(1, len(prices)):
            # 第i天不持有，i-1天未持有，第i天不买
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            # 第i天不持有，i-1天持有，第i天卖掉
            dp[i][1] = max(dp[i-1][2], dp[i-1][3]) + prices[i]
            # 第i天持有，i-1天不持有，第i天买
            dp[i][2] = max(dp[i-1][0], dp[i-1][1]) - prices[i]
            # 第i天持有，i-1天持有，第i天不卖
            dp[i][3] = max(dp[i-1][2], dp[i-1][3])

        return max(dp[-1][0], dp[-1][1])
