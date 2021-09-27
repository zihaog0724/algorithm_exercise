// leetcode 104. maxDepth bfs cpp

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
    int maxDepth(TreeNode* root) 
    {
        if (!root)
        {
            return 0;
        }
        
        int depth = 0;
        vector<TreeNode*> curListNode;
        curListNode.push_back(root);

        while (curListNode.size() > 0)
        {
            depth += 1;
            vector<TreeNode*> tempListNode;
            for (int i = 0; i < curListNode.size(); i++)
            {
                if (curListNode[i]->left)
                {
                    tempListNode.push_back(curListNode[i]->left);
                }
                if (curListNode[i]->right)
                {
                    tempListNode.push_back(curListNode[i]->right);
                }
            }
            curListNode = tempListNode;
        }
        return depth;
    }
};
