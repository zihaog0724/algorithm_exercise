// leetcode 102. levelOrder bfs cpp

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
    vector<vector<int>> levelOrder(TreeNode* root) 
    {
        vector<vector<int>> res;

        if(!root)
        {
            return res;
        }

        vector<int> head_val(1, root->val);
        res.push_back(head_val);
        vector<TreeNode*> curNodeList;
        curNodeList.push_back(root);

        while(curNodeList.size() > 0)
        {
            vector<TreeNode*> tempNodeList;
            vector<int> temp_res;
            
            for (int i = 0; i < curNodeList.size(); i++)
            {
                if (curNodeList[i]->left)
                {
                    tempNodeList.push_back(curNodeList[i]->left);
                    temp_res.push_back(curNodeList[i]->left->val);
                }
                if (curNodeList[i]->right)
                {
                    tempNodeList.push_back(curNodeList[i]->right);
                    temp_res.push_back(curNodeList[i]->right->val);
                }
            }

            curNodeList = tempNodeList;
            if(temp_res.size() > 0)
            {
                res.push_back(temp_res);
            }
        }
        return res;
    }
};
