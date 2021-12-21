// leetcode 114. flatten binary tree

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
    void flatten(TreeNode* root) 
    {
        if(!root)
        {
            return;
        }

        this->flatten(root->left);
        this->flatten(root->right);
        
        TreeNode* tmp = root->right;
        root->right = root->left;
        root->left = nullptr; 
        while(root->right)
        {
            root = root->right;
        }
        root->right = tmp;
    }
};
