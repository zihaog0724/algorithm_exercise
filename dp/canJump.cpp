// leetcode 55. canJump cpp

class Solution {
public:
    bool canJump(vector<int>& nums) 
    {
        vector<int> dp(nums.size(), false);
        dp[0] = true;
        for (int i = 1; i < nums.size(); i++)
        {
            for (int j = i - 1; j >= 0; j--)
            {
                if (dp[j] && (j + nums[j]) >= i)
                {
                    dp[i] = true;
                    break;
                }
            }
            if (dp[nums.size() - 1])
            {
                break;
            }
        }
        return dp[nums.size() - 1];
    }
};
