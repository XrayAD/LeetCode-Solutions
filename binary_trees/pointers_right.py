
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        current = root
        next = current.left
        while(next):
            current.left.next = current.right
            if (current.next):
                current.right.next = current.next.left
                current = current.next
            else:
                current = next
                next = current.left
        return root
