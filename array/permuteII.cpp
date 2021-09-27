// leetcode 47. permuteII cpp

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) 
    {
        vector<vector<int>> res;
        vector<int> path;
        vector<bool> used(nums.size(), false);
        sort(nums.begin(), nums.end());
        this->backtrack(nums, path, used, res);
        return res;
    }
    
    void backtrack(vector<int>& nums, vector<int> &path, vector<bool>& used, vector<vector<int>>& res)
    {
        if (path.size() == nums.size())
        {
            res.push_back(path);
            return;
        }
        
        for (int i = 0; i < nums.size(); i++)
        {
            if (used[i])
            {
                continue;
            }

            if (i > 0 && nums[i] == nums[i-1] && used[i-1] == false)
            {
                continue;
            }

            path.push_back(nums[i]);
            used[i] = true;
            this->backtrack(nums, path, used, res);
            path.pop_back();
            used[i] = false;
        }
    }
};
