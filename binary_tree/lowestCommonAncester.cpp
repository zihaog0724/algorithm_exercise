// leetcode 236. lowestCommonAncestor cpp

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) 
    {
        if(!root)
        {

            return nullptr;
        }    

        if(p->val == root->val || q->val == root->val)
        {
            return root;
        }

        TreeNode* left = this->lowestCommonAncestor(root->left, p, q);
        TreeNode* right = this->lowestCommonAncestor(root->right, p, q);

        if(left && right)
        {
            return root;
        }
        if(left)
        {
            return left;
        }
        if(right)
        {
            return right;
        }
        return nullptr;
    }
};
