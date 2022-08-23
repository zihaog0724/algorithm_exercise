// hot100-lc 48. rotateImage

#include <cstdio>
#include <vector>

class Solution {
public:
    void rotate(std::vector<std::vector<int>>& matrix)
    {
        int n = (int)matrix.size();
        for (int row = 0; row < n - 1; row++)
        {
            for (int col = row + 1; col < n; col++)
            {
                this->swap(matrix[row][col], matrix[col][row]);
            }
        }

        int mid = n / 2;

        for (int row = 0; row < n; row++)
        {
            for (int col = 0; col < mid; col++)
            {
                this->swap(matrix[row][col], matrix[row][n - col - 1]);
            }
        }
    }

private:
    void swap(int & i, int & j)
    {
        int tmp = i;
        i = j;
        j = tmp;
    }
};
