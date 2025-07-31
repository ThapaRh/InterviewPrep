# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#the logic is to find the node == p or node==q and immediately return
#if we get to the node where left returned something and right did too, then that is the first root to be returned
#else we return one of two which has values
#TC: O(n)
#SC= O(h)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
                    1
                2       3
            4   5      6 7
        '''
        if root==None or root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        return left if left else right
    