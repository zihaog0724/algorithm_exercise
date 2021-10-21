// leetcode 98. isValidBST cpp

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
    bool isValidBST(TreeNode* root) 
    {
        return this->dfs(root, nullptr, nullptr);
    }

private:    
    bool dfs(TreeNode* root, TreeNode* maximum, TreeNode* minimum)
    {
        if(!root)
        {
            return true;
        }
        if(maximum != nullptr && root->val >= maximum->val)
        {
            return false;
        }
        if(minimum != nullptr && root->val <= minimum->val)
        {
            return false;
        }
        return this->dfs(root->left, root, minimum) && this->dfs(root->right, maximum, root);
    }
};
