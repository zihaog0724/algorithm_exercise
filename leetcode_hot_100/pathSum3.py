# hot100-lc 437. 路径总和3

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.count = 0

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0
        self.dfs(root, targetSum)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        return self.count

    def dfs(self, root, target):
        if not root:
            return
        target = target - root.val
        if target == 0:
            self.count += 1
        self.dfs(root.left, target)
        self.dfs(root.right, target)

