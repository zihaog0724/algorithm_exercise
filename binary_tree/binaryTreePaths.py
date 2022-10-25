# leetcode 257. 二叉树的所有路径

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.ret = []
        self.dfs(root, "")
        return self.ret

    def dfs(self, root, path):
        if not root:
            return
        path += str(root.val)
        if root.left is None and root.right is None:
            self.ret.append(path)
            return
        self.dfs(root.left, path+"->")
        self.dfs(root.right, path+"->")
