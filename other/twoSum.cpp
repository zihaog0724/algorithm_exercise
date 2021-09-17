// leetcode 1. two sum

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        vector<int> res;
        map<int, int> hashmap;
        for (int i = 0; i < nums.size(); i++)
        {
            hashmap.insert(map<int, int>::value_type(nums[i], i));
        }
        for (int i = 0; i < nums.size(); i++)
        {
            int diff = target - nums[i];
            if (hashmap.count(diff) > 0 && i != hashmap[diff])
            {
                res.emplace_back(i);
                res.emplace_back(hashmap[diff]);
                return res;
            }
        }
        return res;
    }
};
