'''
给定一个二叉树，返回该二叉树的之字形层序遍历，（第一层从左向右，下一层从右向左，一直这样交替）
例如：
给定的二叉树是{3,9,20,#,#,15,7},
该二叉树层序遍历的结果是
[
[3],
[20,9],
[15,7]
]
'''

# 
# @param root TreeNode类 
# @return int整型二维数组
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        # write code here
        if not root:
            return []
        
        res = []
        queue = [root]
        flag = 1
        while len(queue) > 0: 
            temp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            if flag == 1:
                res.append(temp[::-1])
            else:
                res.append(temp)
            flag = flag * (-1)
        return res

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
nums=[1,2,3,4,5,6,7]
root = create_tree(None, nums, 0)
solution = Solution()
print(solution.zigzagLevelOrder(root))
