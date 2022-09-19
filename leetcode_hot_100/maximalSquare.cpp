// hot100-lc 221. 最大正方形

#include <vector>

class Solution {
public:
    int maximalSquare(std::vector<std::vector<char>>& matrix)
    {
        int rows = (int)matrix.size();
        int cols = (int)matrix[0].size();
        int dp[rows][cols];

        int maxLength = 0;
        for(int j = 0; j < cols; j++)
        {
            if(matrix[0][j] == '1')
            {
                dp[0][j] = 1;
                maxLength = 1;
            }
            else
            {
                dp[0][j] = 0;
            }
        }

        for(int i = 0; i < rows; i++)
        {
            if(matrix[i][0] == '1')
            {
                dp[i][0] = 1;
                maxLength = 1;
            }
            else
            {
                dp[i][0] = 0;
            }
        }


        for(int i = 1; i < rows; i++)
        {
            for(int j = 1; j < cols; j++)
            {
                if(matrix[i][j] == '1')
                {
                    dp[i][j] = std::min(std::min(dp[i-1][j-1], dp[i][j-1]), dp[i-1][j]) + 1;
                    maxLength = std::max(dp[i][j], maxLength);
                }
                else
                {
                    dp[i][j] = 0;
                }
            }
        }
        return maxLength * maxLength;
    }
};
