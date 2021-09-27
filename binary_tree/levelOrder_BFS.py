# leetcode 102. levelOrder bfs

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

        res = [[root.val]]
        curNodeList = [root]
        while len(curNodeList) > 0:
            tempNodeList = []
            temp_res = []
            for node in curNodeList:
                if node.left:
                    tempNodeList.append(node.left)
                    temp_res.append(node.left.val)
                if node.right:
                    tempNodeList.append(node.right)
                    temp_res.append(node.right.val)
            if len(temp_res) > 0:
                res.append(temp_res)
            curNodeList = tempNodeList
        return res
