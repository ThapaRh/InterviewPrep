'''
ValidTree(leftLimit,rightLimit): initially set to neg inf and pos inf
if not root:
return True
if root.val>left and root.val<right:
l=recur(leftLimit,root.val)

TC: O(nodes)
SC: O(h) where h is the height of the tree, if its balanced tree its logn if not it's n  *****
'''

def is_valid_BST(root):
    
    def valid_tree(root,left_limit,right_limit):
        if not root:
            return True
        if not (root.val>left_limit and root.val<right_limit):
                    return False
        l = valid_tree(root.left,left_limit,root.val)
        r = valid_tree(root.right,root.val,right_limit)
        return l and r

    return valid_tree(root,-10**32,10**32)
    