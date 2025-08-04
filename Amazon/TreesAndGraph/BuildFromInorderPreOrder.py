# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        3
        find index of 3 and which will give us left subtree and right subtree
        pre = 3 9 20 15 7 11 19
        in = 9 3 15 20 11 7 19
        root = pre[0] 3
        left = in[:indexof(root] 9 , 9
        right = in[indexofroot+1:]  15,20,11,7,19
        root.left = buildTree(leftt)
        root

        3 9 15 7 20
        15 9 7 3 20

        in 15 9 7
        pre 9 15 7

        in 15
        pre 15



        15

        value = preorder[0]
        indx = in.indexof(value)
        left_arr = in[:indx]
        right_arr = in[indx+1:]
        pre_left = pre[1:len(left_arr)]
        pre_right = pre[1+len(left_arr):]
        '''
        if len(preorder)==0 or len(inorder)==0:
            return None
        if len(preorder)==1:
            val = preorder[0]
            return TreeNode(val)
        val = preorder[0]
        r = TreeNode(val)
        index_inorder = inorder.index(val)
        left_inorder = inorder[:index_inorder]
        right_inorder = inorder[index_inorder+1:]
        left_pre = preorder[1:1+len(left_inorder)]
        right_pre = preorder[1+len(left_inorder):]
        r.left = self.buildTree(left_pre,left_inorder)
        r.right = self.buildTree(right_pre,right_inorder)
        return r
        

