// leetcode 213. rob2 cpp

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
        return max(this->robWithoutCircle(nums, 0, n-2), this->robWithoutCircle(nums, 1, n-1));
    }

    int robWithoutCircle(vector<int>& nums, int start, int end)
    {
        int n = end - start + 1;
        if (n == 1)
        {
            return nums[start];
        }
        if (n == 2)
        {
            return max(nums[start], nums[start + 1]);
        }
        
        int dp[n];
        dp[0] = nums[start];
        dp[1] = nums[start + 1];
        int ret = max(nums[start], nums[start + 1]);
        for (int i = start + 2; i <= end; i++)
        {
            int tmp = 0;
            for (int j = i - 2; j >= start; j--)
            {
                if (dp[j - start] >= tmp)
                {
                    dp[i - start] = nums[i] + dp[j - start];
                    tmp = dp[j - start];
                }
            }
            if (dp[i - start] >= ret)
            {
                ret = dp[i - start];
            }
        }
        return ret;
    }
};

