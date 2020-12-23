'''
给定一棵二叉树以及这棵树上的两个节点 o1 和 o2，
请找到 o1 和 o2 的最近公共祖先节点。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self , root , o1 , o2 ):
        if not root:
            return None
        if o1 == root.val or o2 == root.val:
            return root.val

        left = self.lowestCommonAncestor(root.left, o1, o2)
        right = self.lowestCommonAncestor(root.right, o1, o2)

        if left and right:
            return root.val
        if left:
            return left
        if right:
            return right
        return None

def create_tree(root, nums, i):
    if i < len(nums):
        if not nums[i]:
            return None
        else:
            root = TreeNode(nums[i])
            root.left = create_tree(root.left, nums, i*2+1)
            root.right = create_tree(root.right, nums, i*2+2)
            return root
    return root

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,None,None]
root = create_tree(None, nums, 0)
solution = Solution()
print(solution.lowestCommonAncestor(root, 8, 7))


