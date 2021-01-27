"""
Morris Traversal to inOrder 
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution:
    def MorrisPre(self, head):
        if not head:
            return

        cur = head
        while cur:
            # print(cur.val) Morris Traversal
            mostRight = cur.left
            if mostRight:
                while mostRight.right and mostRight.right != cur:
                    mostRight = mostRight.right
                if not mostRight.right:
                    mostRight.right = cur
                    cur = cur.left
                    continue
                if mostRight.right == cur:
                    print(cur.val)
                    mostRight.right = None
                    cur = cur.right
                    continue
            else:
                print(cur.val)
                cur = cur.right

def create_tree(root, nums, i):
    if i < len(nums):
        if not nums[i]:
            return None
        else:
            root = TreeNode(nums[i])
            root.left = create_tree(root.left, nums, i*2+1)
            root.right = create_tree(root.left, nums, i*2+2)
            return root
    return root


nums = [1,2,3,4,5,6,7]
head = create_tree(None, nums, 0)
s = solution()
s.MorrisPre(head)

