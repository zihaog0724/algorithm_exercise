'''
分别按照二叉树先序，中序和后序打印所有的节点。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def threeOrders(self, root):
        # write code here
        self.preOrder = []
        self.inOrder = []
        self.postOrder= []
        self.pre_order(root)
        self.in_order(root)
        self.post_order(root)
        return [self.preOrder, self.inOrder, self.postOrder]

    def pre_order(self, root):
        if not root:
            return
        self.preOrder.append(root.val)
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        self.inOrder.append(root.val)
        self.in_order(root.right)

    def post_order(self, root):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        self.postOrder.append(root.val)

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

# Test
nums=[1,2,3,4,5,6,7]
root = create_tree(None, nums, 0)
solution = Solution()
print(solution.threeOrders(root))