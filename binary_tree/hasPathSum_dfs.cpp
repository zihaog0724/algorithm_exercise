// leetcode 112. hasPathSum dfs cpp

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
    bool hasPathSum(TreeNode* root, int targetSum) 
    {
        bool res = false;
        if(!root)
        {
            return res;
        }
        int curSum = 0;
        res = dfs(root, curSum, targetSum);
        return res;
    }
    
    bool dfs(TreeNode* root, int curSum, int targetSum)
    {
        if(!root)
        {
            return false;
        }
        curSum += root->val;
        if(!root->left && !root->right)
        {
            if(curSum == targetSum)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        return dfs(root->left, curSum, targetSum) || dfs(root->right, curSum, targetSum);
    }
};
