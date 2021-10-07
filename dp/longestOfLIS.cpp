// leetcode 300. longestOfLIS

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) 
    {
        int n = nums.size();
        if (n == 1)
        {
            return 1;
        }

        int dp[n]; // LIS at index n
        for (int i = 0; i < n; i++)
        {
            dp[i] = 1;
        }

        int ret = 1;
        for (int i = 1; i < n; i++)
        {
            for (int j = i-1; j >= 0; j--)
            {
                if (nums[i] > nums[j])
                {
                    dp[i] = max(dp[j] + 1, dp[i]);
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
