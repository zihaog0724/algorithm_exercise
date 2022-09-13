// hot100-lc 198. 打家劫舍

class Solution {
public:
    int rob(std::vector<int>& nums)
    {
        int n = (int)nums.size();
        if(n == 1)
        {
            return nums[0];
        }

        std::vector<int> dp(n);
        dp[0] = nums[0];
        dp[1] = std::max(nums[0], nums[1]);
        int ret = std::max(dp[0], dp[1]);
        for (int i = 2; i < n; i++)
        {
            int tmp = 0;
            for (int j = i - 2; j >= 0; j--)
            {
                if (dp[j] + nums[i] > tmp)
                {
                    dp[i] = dp[j] + nums[i];
                    tmp = dp[j] + nums[i];
                }
            }
            if (dp[i] > ret)
            {
                ret = dp[i];
            }
        }
        return ret;
    }
};
