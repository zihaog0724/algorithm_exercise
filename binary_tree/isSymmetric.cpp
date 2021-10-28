// leetcode 101. isSymmetric cpp

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
    bool isSymmetric(TreeNode* root) 
    {
        return this->dfs(root->left, root->right);
    }

    bool dfs(TreeNode* left, TreeNode* right)
    {
        if(!left && !right)
        {
            return true;
        }
        if(!left || !right)
        {
            return false;
        }
        if(left->val == right->val)
        {
            return this->dfs(left->left, right->right) && this->dfs(left->right, right->left);
        }
        return false;
    }
};
