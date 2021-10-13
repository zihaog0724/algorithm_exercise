// leetcode 34. searchRange cpp

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) 
    {
        int n = nums.size();
        if (n == 0)
        {
            return {-1, -1};
        }
        
        int low = 0;
        int high = n - 1;
        int l = 0;
        int r = n - 1;
        while (low < high)
        {
            int mid = (low + high) / 2;
            if (target <= nums[mid])
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
        else
        {
            l = low;
        }

        low = 0;
        high = n - 1;
        while (low < high)
        {
            int mid = (low + high + 1) / 2;
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
