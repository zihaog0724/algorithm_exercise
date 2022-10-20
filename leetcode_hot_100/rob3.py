# hot100-lc 337. 打家劫舍3

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.map = {}

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        对于一个节点的收益，两种偷法
        method1: 偷子节点
        method2: 偷自己+孙子节点
        """
        if not root:
            return 0

        if root in self.map.keys():
            return self.map[root]

        method1 = self.rob(root.left) + self.rob(root.right)
        method2 = root.val
        if root.left:
            method2 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            method2 += self.rob(root.right.left) + self.rob(root.right.right)
        self.map[root] = max(method1, method2)
        return max(method1, method2)
