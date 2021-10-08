// leetcode 11. maxArea cpp

class Solution {
public:
    int maxArea(vector<int>& height) 
    {
        int left = 0;
        int right = height.size() - 1;
        int ret = 0;
        while (left < right)
        {
            if(height[left] <= height[right])
            {
                if(height[left] * (right - left) >= ret)
                {
                    ret = height[left] * (right - left);
                }
                left++;
            }
            else
            {
                if(height[right] * (right - left) >= ret)
                {
                    ret = height[right] * (right - left);
                }
                right--;
            }
        }
        return ret;
    }
};
