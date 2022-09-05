# hot100-lc 124. 二叉树最大路径和

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = root.val
        ret = self.dfs(root)
        return self.maxSum

    def dfs(self, root):
        if not root: 
            return 0
        left = max(0, self.dfs(root.left))
        right = max(0, self.dfs(root.right))
        if root.val + left + right > self.maxSum:
            self.maxSum = root.val + left + right
        return max(root.val, root.val + left, root.val + right)
