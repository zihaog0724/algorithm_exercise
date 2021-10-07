// leetcode 718. findLength cpp

class Solution {
public:
    int findLength(vector<int>& nums1, vector<int>& nums2) 
    {
        int m = nums1.size();
        int n = nums2.size();
        int dp[m+1][n+1];

        for (int i = 0; i < m; i++)
        {
            dp[i][0] = 0;
        }

        for (int i = 0; i < n; i++)
        {
            dp[0][i] = 0;
        }

        int ret = 0;
        for (int i = 1; i < m + 1; i++)
        {
            for (int j = 1; j < n + 1; j++)
            {
                if (nums1[i-1] == nums2[j-1])
                {
                    dp[i][j] = dp[i-1][j-1] + 1;
                }
                else
                {
                    dp[i][j] = 0;
                }
                if (dp[i][j] > ret)
                {
                    ret = dp[i][j];
                }
            }
        }
        return ret;
    }
};
