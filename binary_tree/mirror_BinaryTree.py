'''
操作给定的二叉树，将其变换为源二叉树的镜像。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return None

        left, right = root.left, root.right
        root.left, root.right = right, left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root

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
nums=[8,6,10,5,7,9,11]
root = create_tree(None, nums, 0)
solution = Solution()
print(solution.Mirror(root).left.left.val)
