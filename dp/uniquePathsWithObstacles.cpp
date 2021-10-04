// leetcode 63. uniquePathsWithObstacles cpp

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) 
    {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        int dp[m][n];
        
        int i = 0;
        while(i < m && obstacleGrid[i][0] == 0)
        {
            dp[i][0] = 1;
            i++;
        }
        while(i < m)
        {
            dp[i][0] = 0;
            i++;
        }

        i = 0;
        while(i < n && obstacleGrid[0][i] == 0)
        {
            dp[0][i] = 1;
            i++;
        }
        while(i < n)
        {
            dp[0][i] = 0;
            i++;
        }  

        for (int i = 1; i < m; i++)
        {
            for (int j = 1; j < n; j++)
            {
                if (obstacleGrid[i][j] == 1)
                {
                    dp[i][j] = 0;
                }
                else
                {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
        }
        return dp[m-1][n-1];
    }
};
