from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):#
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pre = []
        def recurse(root: Optional[TreeNode], pre):
            print(pre)
            if (root):
                pre.append(root.val)
                recurse(root.left, pre)
                recurse(root.right, pre)
        recurse(root, pre)
        return pre

    def preIterative(self, root: Optional[TreeNode]) -> List[int]:
        pre = []
        stack = []
        while(root):
            pre.append(root.val)
            if root.left:
                if root.right:
                    stack.append(root.right)
                root=root.left
            elif root.right:
                root = root.right
            else:
                if len(stack) == 0:
                    root = None
                else:
                    root = stack.pop(-1)  #-1 not needed, pop defaults to -1
        #print(pre)
        return pre

    def betterIterative(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)        #can use stack for both left and right nodes
        return ret



#a  = TreeNode(3)
#b = TreeNode(2,None,a)
#c = TreeNode(1,b)

#d = Solution()
#d.preIterative(c)

ab  = TreeNode(1)
bb = TreeNode(2)
cb = TreeNode(3,ab,bb)

db = Solution()
db.preIterative(cb)
