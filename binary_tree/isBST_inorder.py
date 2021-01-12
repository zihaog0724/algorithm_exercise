class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Checker:
    def checkBST(self, root):
        # write code here
        self.inorder = []
        if not root:
            return False
        self.in_order(root)
        pre = self.inorder[0]
        for i in range(1, len(self.inorder)):
            if self.inorder[i] <= pre:
                return False
            pre = self.inorder[i]
        return True
            
    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        self.inorder.append(root.val)
        self.in_order(root.right)


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
