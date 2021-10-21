// leetcode 96. numBSTs cpp

class Solution {
public:
    int numTrees(int n) 
    {
        if(n < 2)
        {
            return 1;
        }
        else if(n == 2)
        {
            return 2;
        }

        int dp[n+1];
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;
        for(int i = 3; i < n + 1; i++)
        {
            dp[i] = 0;
            for(int j = i - 1; j >= 0; j--)
            {
                int k = i - 1 - j;
                dp[i] += dp[j] * dp[k];
            }
        }
        return dp[n];
    }
};
