// leetcode 198. rob cpp

class Solution {
public:
    int rob(vector<int>& nums) 
    {
        int n = nums.size();
        if (n == 1)
        {
            return nums[0];
        }
        if (n == 2)
        {
            return max(nums[0], nums[1]);
        }

        int dp[n];
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        int ret = max(dp[0], dp[1]);
        for (int i = 2; i < n; i++)
        {
            int tmp = 0;
            for (int j = i-2; j >=0; j--)
            {
                if (dp[j] >= tmp)
                {
                    dp[i] = dp[j] + nums[i];
                    tmp = dp[j]; 
                }
            }
            if (dp[i] >= ret)
            {
                ret = dp[i];
            }
        }
        return ret;
    }
};
