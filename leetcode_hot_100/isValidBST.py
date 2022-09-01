# hot100-lc 98. 验证二叉搜索树

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, root, minimum, maximum):
        if not root:
            return True
        return minimum < root.val < maximum and self.dfs(root.left, minimum, root.val) and self.dfs(root.right, root.val, maximum)
