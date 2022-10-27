# leetcode 94. inorderTraversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ret = []
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.ret.append(root.val)
        self.dfs(root.right)
