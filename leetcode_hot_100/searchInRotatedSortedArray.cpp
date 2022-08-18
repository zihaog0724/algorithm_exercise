// hot100-lc 33.

#include <cstdio>
#include <vector>

class Solution {
public:
    int search(std::vector<int>& nums, int target)
    {
        int n = (int)nums.size();
        int low = 0;
        int high = n - 1;
        while (low <= high)
        {
            int mid = (low + high) / 2;
            if (target == nums[mid])
            {
                return mid;
            }
            if (nums[mid] >= nums[low]) // 说明low~mid有序
            {
                if(target <= nums[mid] && target >= nums[low]) // target在这个有序区间内
                {
                    high = mid;
                }
                else // target不在这个有序区间内
                {
                    low = mid + 1;
                }
            }
            else // 说明low~mid无序，即mid~high有序
            {
                if(target >= nums[mid] && target <= nums[high]) // target在这个有序区间内
                {
                    low = mid;
                }
                else // target不在这个有序区间内
                {
                    high = mid - 1;
                }
            }
        }
        return -1;
    }
};
