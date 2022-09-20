# hot10o-lc 226. 翻转二叉树

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root
