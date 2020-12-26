# -*- coding:utf-8 -*-
"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
则重建二叉树并返回。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None
        head = TreeNode(pre[0])
        head_idx = tin.index(pre[0])
        head.left = self.reConstructBinaryTree(pre[1:head_idx+1], tin[:head_idx])
        head.right = self.reConstructBinaryTree(pre[head_idx+1:], tin[head_idx+1:])
        return head

pre = [1,2,3,4,5,6,7]
tin = [3,2,4,1,6,5,7]
solution = Solution()
print(solution.reConstructBinaryTree(pre, tin))