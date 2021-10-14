// leetcode 78. subsets cpp

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) 
    {
        vector<vector<int>> ret;
        int startIndex = 0;
        vector<int> combination;
        this->dfs(nums, startIndex, combination, ret);
        return ret;
    }

private:
    void dfs(vector<int>& nums, int startIndex, vector<int> combination, vector<vector<int>>& ret)
    {
        ret.push_back(combination);
        if(startIndex == nums.size())
        {
            return;
        }
        for(int i = startIndex; i < nums.size(); i++)
        {
            combination.push_back(nums[i]);
            this->dfs(nums, i+1, combination, ret);
            combination.pop_back();
        }
    }
};
