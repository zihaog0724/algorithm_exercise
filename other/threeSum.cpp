// leetcode 15. threeSum cpp

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums)
    {
        int n = nums.size();
        vector<vector<int>> ret;
        if (n < 3)
        {
            return ret;
        }
        
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n-2; i++)
        {
            if (i > 0 && nums[i] == nums[i-1])
            {
                continue;
            }

            int left = i + 1;
            int right = n - 1;
            while(left < right)
            {
                if(nums[i] + nums[left] + nums[right] == 0)
                {
                    vector<int> tmp = {nums[i], nums[left], nums[right]};
                    ret.push_back(tmp);
                    while(left < right && nums[left+1] == nums[left])
                    {
                        left++;
                    }
                    while(left < right && nums[right-1] == nums[right])
                    {
                        right--;
                    }
                    left++;
                    right--;
                }
                else if(nums[i] + nums[left] + nums[right] > 0)
                {
                    right--;
                }
                else
                {
                    left++;
                }
            }
        }
        return ret;
    }
};
