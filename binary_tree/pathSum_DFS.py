'''
leetcode 113. 路径总和2
给定一个二叉树和一个值\ sum sum，请找出所有的根节点到叶子节点的节点值之和等于 sum 的路径
'''

# 
# @param root TreeNode类 
# @param sum int整型 
# @return int整型二维数组
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        self.ret = []
        self.dfs(root, targetSum, [])
        return self.ret

    def dfs(self, root, targetSum, path):
        if not root:
            return
        path.append(root.val)
        targetSum -= root.val
        if root.left is None and root.right is None and targetSum == 0:
            self.ret.append(path)
            return
        self.dfs(root.left, targetSum, copy.deepcopy(path))
        self.dfs(root.right, targetSum, copy.deepcopy(path))
