'''
求给定二叉树的最大深度，
最大深度是指树的根结点到最远叶子结点的最长路径上结点的数量。
'''

# 
# @param root TreeNode类 
# @return int整型
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        # write code here
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

def create_tree(root, list, i):
    if i < len(list):
        if not list[i]: 
            return None
        else:
            root = TreeNode(list[i])
            root.left = create_tree(root.left, list, i*2+1)
            root.right = create_tree(root.right, list, i*2+2)
            return root
    return root

# Test
nums=[2,3,4,5,6,7,None,None,None,None,None,None,8]
root = create_tree(None, nums, 0)
solution = Solution()
print(solution.maxDepth(root))
