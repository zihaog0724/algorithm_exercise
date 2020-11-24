'''
给定一个二叉树和一个值\ sum sum，请找出所有的根节点到叶子节点的节点值之和等于 sum 的路径
'''

# 
# @param root TreeNode类 
# @param sum int整型 
# @return int整型二维数组
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        # write code here
        res = []
        temp = []
        if not root:
            return res
        self.DFS(root, sum, res, temp)
        return res

    def DFS(self, root, sum, res, temp):
        if not root:
            return
        if root.val == sum:
            res.append(temp + [root.val])
            return
        temp.append(root.val)
        self.DFS(root.left, sum - root.val, res, temp)
        self.DFS(root.right, sum - root.val, res, temp)
        temp.pop()

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
nums=[5,4,8,1,11,None,9,None,None,2,7,None,None,None,None]
root = create_tree(None, nums, 0)
solution = Solution()
print(solution.pathSum(root, 22))
