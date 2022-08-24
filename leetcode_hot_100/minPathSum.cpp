// hot100-lc 64. 最小路径和

class Solution {
public:
    int minPathSum(std::vector<std::vector<int>>& grid)
    {
        int rows = (int)grid.size();
        int cols = (int)grid[0].size();
        int dp[rows][cols];
        dp[0][0] = grid[0][0];
        for (int i = 1; i < rows; i++)
        {
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }
        for (int j = 1; j < cols; j++)
        {
            dp[0][j] = dp[0][j-1] + grid[0][j];
        }
        for (int i = 1; i < rows; i++)
        {
            for (int j = 1; j < cols; j++)
            {
                dp[i][j] = std::min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j]);
            }
        }
        return dp[rows-1][cols-1];
    }
};
