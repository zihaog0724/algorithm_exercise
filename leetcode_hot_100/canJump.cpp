// hot100-lc 55. canJump

#include <cstdio>
#include <vector>

class Solution {
public:
    bool canJump(std::vector<int>& nums)
    {
        int n = (int)nums.size();
        std::vector<bool> dp(n, false);
        dp[0] = true;
        for (int i = 1; i < n; i++)
        {
            for (int j = i - 1; j >= 0; j--)
            {
                if(dp[j] && j + nums[j] >= i)
                {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n - 1];
    }
};
