# hot100-lc 102. 层序遍历

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret = [[root.val]]
        curNodes = [root]
        while len(curNodes) > 0:
            tmp_ret = []
            nextLevel = []
            for node in curNodes:
                if node.left:
                    tmp_ret.append(node.left.val)
                    nextLevel.append(node.left)
                if node.right:
                    tmp_ret.append(node.right.val)
                    nextLevel.append(node.right)
            if len(tmp_ret) > 0:
                ret.append(tmp_ret)
            curNodes = nextLevel
        return ret
