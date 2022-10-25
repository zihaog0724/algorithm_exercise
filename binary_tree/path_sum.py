'''
给定一个仅包含数字\ 0-9 0−9 的二叉树，每一条从根节点到叶子节点的路径都可以用一个数字表示。
例如根节点到叶子节点的一条路径是1\to 2\to 31→2→3,那么这条路径就用\ 123 123 来代替。
找出根节点到叶子节点的所有路径表示的数字之和

根节点到叶子节点的路径1→2 用数字 12 代替
根节点到叶子节点的路径1→3 用数字 13 代替
所以答案为 12+13=25
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self , root ):
        # write code here
        if not root:
            return 0
        return self.helper(root, 0)
    
    def helper(self, root, sums):
        if not root: #若无此节点，不参与计算
            return 0
        sums += root.val
        if root.left or root.right: #若不是叶子节点
            sums = 10 * sums
        else: #若是叶子节点
            return sums
        sum_left = self.helper(root.left, sums)
        sum_right = self.helper(root.right, sums)
        return sum_left + sum_right

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

nums = [1,2,3,4,5,6,7]
root = create_tree(None, nums, 0)
solution = Solution()
print(solution.sumNumbers(root))
