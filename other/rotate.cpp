// leetcode 48. rotate cpp

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) 
    {
        int n = matrix.size();

        for(int i = 0; i < n - 1; i++)
        {
            for(int j = 1; j < n - i; j++)
            {
                this->swap(matrix[i][i+j], matrix[i+j][i]);                
            }
        }

        for(int i = 0; i < n; i++)
        {
            int left = 0;
            int right = n - 1;
            while(left < right)
            {
                this->swap(matrix[i][left], matrix[i][right]);
                left++;
                right--;
            }
        }
    }
    
    void swap(int & p1, int & p2)
    {
        int tmp = p1;
        p1 = p2;
        p2 = tmp;
    }
};
