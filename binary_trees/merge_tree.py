# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
#        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return recurse(root1, root2)


    def recurse(self, root1: Optional[TreeNode], root2: Optional[TreeNode]):
        if root1 and root2:
            new = TreeNode(val = root1.val + root2.val)
            new.left = self.recurse(root1.left, root2.left)
            new.right = self.recurse(root1.right, root2.right)
        elif root1:                 #can return subtree here no need to keep  recursing
            return root1
        elif root2:
            return root2
        else:
            return None
        return new
