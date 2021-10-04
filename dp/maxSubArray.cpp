// leetcode 53. maxSubArray cpp

class Solution {
public:
    int maxSubArray(vector<int>& nums) 
    {
        int n = nums.size();
        if (n == 1)
        {
            return nums[0];
        }

        vector<int> dp(n, 0);
        dp[0] = nums[0];
        int ret = dp[0];
        for (int i = 1; i < n; i++)
        {
            dp[i] = max(dp[i-1] + nums[i], nums[i]);
            if (dp[i] > ret)
            {
                ret = dp[i];
            }
        }
        return ret;
    }
};
