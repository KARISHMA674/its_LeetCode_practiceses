# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
           

            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            
            successor = self._find_min(root.right)
            
            root.val = successor.val
            
            root.right = self.deleteNode(root.right, successor.val)

        return root

    def _find_min(self, node):
        curr = node
        while curr.left:
            curr = curr.left
        return curr
        