// hot100-lc.34

#include <cstdio>
#include <vector>

class Solution {
public:
    std::vector<int> searchRange(std::vector<int>& nums, int target)
    {
        int n = (int)nums.size();
        int low = 0;
        int high = n - 1;
        int l = 0;
        while(low < high)
        {
            int mid = (low + high) / 2;
            if(target <= nums[mid])
            {
                high = mid;
            }
            else
            {
                low = mid + 1;
            }
        }
        if(nums[low] != target)
        {
            return {-1, -1};
        }
        l = low;

        low = 0;
        high = n - 1;
        int r = 0;
        while(low < high)
        {
            int mid = (low + high + 1) / 2; // +1 避免死循环
            if(target >= nums[mid])
            {
                low = mid;
            }
            else
            {
                high = mid - 1;
            }
        }
        r = high;
        return {l, r};
    }
};
