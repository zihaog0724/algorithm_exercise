'''
判断是否为平衡二叉树
平衡二叉树（Balanced Binary Tree），具有以下性质：
它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，
并且左右两个子树都是一棵平衡二叉树
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        left = self.getDepth(pRoot.left)
        right = self.getDepth(pRoot.right)
        if abs(right - left) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) & self.IsBalanced_Solution(pRoot.right)
        
    def getDepth(self, root):
        if not root:
            return 0
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        return max(left, right) + 1

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

nums = [1,2,3,4,None,None,None,5]
root = create_tree(None, nums, 0)
solution = Solution()
print(solution.IsBalanced_Solution(root))
