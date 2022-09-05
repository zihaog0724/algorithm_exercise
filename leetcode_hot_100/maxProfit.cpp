// hot100-lc 121. maxProfit

class Solution {
public:
    int maxProfit(std::vector<int>& prices)
    {
        int n = (int)prices.size();
        std::vector<int> dp(n, 0);
        int min_price = prices[0];
        for (int i = 1; i < n; i++)
        {
            min_price = std::min(min_price, prices[i-1]);
            dp[i] = std::max(dp[i-1], prices[i] - min_price);
        }
        return dp[n-1];
    }
};
