// hot100-lc 11. maxArea

#include "stdio.h"
#include <vector>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height)
    {
        int left = 0;
        int right = (int)height.size() - 1;
        int ret = 0;
        int tmp = 0;
        while (left < right)
        {
            if (height[left] < height[right])
            {
                tmp = height[left] * (right - left);
                left++;
            }
            else
            {
                tmp = height[right] * (right - left);
                right--;
            }
            if(tmp > ret)
            {
                ret = tmp;
            }
        }
        return ret;
    }
};
