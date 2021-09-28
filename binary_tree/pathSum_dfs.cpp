// leetcode 113. pathSum dfs cpp

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
 
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) 
    {
        vector<vector<int>> res;
        if(!root)
        {
            return res;
        }
        vector<int> path;
        int remain = targetSum;
        dfs(root, res, path, remain);
        return res;
    }

    void dfs(TreeNode* root, vector<vector<int>>& res, vector<int> path, int remain)
    {
        if (!root)
        {
            return;
        }

        path.push_back(root->val);
        if(!root->left && !root->right)
        {
            if (root->val == remain)
            {
                res.push_back(path);
                return;
            }
            path.pop_back();
            return;
        }
        
        remain -= root->val;
        this->dfs(root->left, res, path, remain);
        this->dfs(root->right, res, path, remain);
    }
};
