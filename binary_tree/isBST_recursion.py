class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Checker:
    def checkBST(self, root):
        # write code here
        return self.process(root, float("inf"), -float("inf"))
        
    def process(self, root, maxVal, minVal):
        if not root:
            return True
        if root.val >= maxVal or root.val <= minVal:
            return False
        return self.process(root.left, root.val, minVal) and self.process(root.right, maxVal, root.val)


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
nums = [7,3,9,1,5,8,10]
tree = create_tree(None, nums, 0)
solution = Checker()
print(solution.checkBST(tree))
