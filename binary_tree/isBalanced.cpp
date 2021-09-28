// leetcode 110. isBalanced cpp

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
    bool isBalanced(TreeNode* root) 
    {
        if(!root)
        {
            return true;
        }
        int left = this->getDepth(root->left);
        int right = this->getDepth(root->right);
        if(abs(left - right) > 1)
        {
            return false;
        }
        return this->isBalanced(root->left) && this->isBalanced(root->right);
    }

    int getDepth(TreeNode* root)
    {
        if(!root)
        {
            return 0;
        }
        int left = this->getDepth(root->left);
        int right = this->getDepth(root->right);
        return max(left, right) + 1;
    }
};
