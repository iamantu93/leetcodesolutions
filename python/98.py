# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
# https://leetcode.com/problems/validate-binary-search-tree/
        """
        :type root: TreeNode
        :rtype: bool
        """
      
        self.prev = None
        return self.validate(root, self.prev)
    
    def validate(self, node, prev):
        if node == None:
            return True
        if not self.validate(node.left, self.prev):
            return False
        if self.prev != None and self.prev.val >= node.val:
            return False
        self.prev = node
        return self.validate(node.right, self.prev)
