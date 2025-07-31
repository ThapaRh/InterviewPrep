# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
             1 1
            /
            2 2+1
        /   \
     1+1 3    4 1+1
        /    /
      1 6    5 1
      
      1 
      /
      2 1
       
TC: O(n)
SC: O(h)
'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_height = 0
        def max_diameter(root):
            nonlocal max_height
            if root==None:
                return 0
            left = max_diameter(root.left)
            right = max_diameter(root.right)
            diameter = left+right
            max_height = max(max_height,diameter)
            return max(left,right)+1
        max_diameter(root)
        return max_height