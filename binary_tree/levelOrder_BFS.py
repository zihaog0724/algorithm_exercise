'''
给定一个二叉树，返回该二叉树层序遍历的结果，（从左到右，一层一层地遍历）
例如：
给定的二叉树是{3,9,20,#,#,15,7},
该二叉树层序遍历的结果是
[
[3],
[9,20],
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
    def levelOrder(self, root):
        # write code here
        queue = []
        if not root:
            return queue
        else:
            queue.append(root)

        res = []
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
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
nums=[2,3,4,5,6,7,None,None,None,None,None,None,8]
root = create_tree(None, nums, 0)
solution = Solution()
print(solution.levelOrder(root))
