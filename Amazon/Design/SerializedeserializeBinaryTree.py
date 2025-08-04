# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#It's crazy i did it in 40 mins and i hadnot seen this question before, gal is getting good at leetcode ahahah
#TC: O(n)
#SC: O(2^height)
class Codec:
    def serialize(self,root):
        if not root:
            return ""
        arr = [root.val]
        q = deque([root])
        while(q):
            lq = len(q)
            while(lq):
                lq-=1
                r = q.popleft()
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
                arr.append(r.left.val if r.left else -1001) #node can be -1000 to 1000 so adding null as -1001
                arr.append(r.right.val if r.right else -1001)
        return "%".join(str(a) for a in arr)
    
    def deserialize(self,data):
        if not data:
            return None

        i = 1
        # %1%2%3%-1
        arr = data.split('%')
        print(arr)
        root = TreeNode(int(arr[0]))
        q = deque([root])
        i = 1
        while(q):
            lq = len(q)
            while(lq):
                lq-=1
                r = q.popleft()
                if i<len(arr) and arr[i]!="-1001":
                    r.left = TreeNode(int(arr[i]))
                    q.append(r.left)
                i+=1
                if i<len(arr) and arr[i]!="-1001":
                    r.right = TreeNode(int(arr[i]))
                    q.append(r.right)
                i+=1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))