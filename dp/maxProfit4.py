# leetcode 188. 买卖股票最佳时机4

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        """
        dp[i][0]: 第i天的状态为一直没操作
        dp[i][j]: 第i天的状态为第n次买入或第m次卖出
        设j除以2等于a余b，
        （1）如果b=1，则状态为第a+1次买入，此时可能为第i-1天状态为第a次卖出，第i天买入；或i-1天的状态就是第a+1次买入
            注：如果是第1次买入，此时可能为第i-1天的状态为一直没操作，第i天买入；或i-1天的状态就是第1次买入
        （2）如果b=0，则状态为第a次卖出，此时可能为第i-1天状态为第a次买入，第i天卖出；或i-1天的状态就是第a次卖出
        """
        dp = [[0] * (2 * k + 1) for _ in range(len(prices))]
        for j in range(1, 2 * k + 1, 2):
            dp[0][j] = -1 * prices[0]

        for i in range(1, len(prices)):
            # dp[i][0] = dp[i-1][0] = 0 恒成立，就不更新了
            for j in range(1, 2 * k + 1):
                a, b = j // 2, j % 2
                if b == 1:  # 买入状态
                    if a == 0:  # 第一次买入
                        dp[i][j] = max(dp[i-1][j], dp[i-1][0] - prices[i])
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] - prices[i])  # 非第一次买入
                else:  # 卖出状态
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + prices[i])
        return max(dp[-1])
