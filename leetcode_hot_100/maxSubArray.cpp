// hot100-lc 53. maxSubArray

#include <cstdio>
#include <vector>

class Solution {
public:
    int maxSubArray(std::vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }

        std::vector<int> dp(nums.size(), 0);
        dp[0] = nums[0];
        int ret = dp[0];
        for (int i = 1; i < dp.size(); i++)
        {
            dp[i] = std::max(nums[i], nums[i] + dp[i-1]);
            if (dp[i] > ret)
            {
                ret = dp[i];
            }
        }
        return ret;
    }
};
