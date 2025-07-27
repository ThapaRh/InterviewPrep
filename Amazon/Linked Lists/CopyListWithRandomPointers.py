'''
dict = {oldnode:newNode}
7:newNode
13:newNode()
dict[old].random = dict[old.random] 
TC = O(n)
Sc: O(N)
'''
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
class Solution:
    def copyRandomList(self, head):
        curr = head
        dict = {None:None}
        dummy = Node(-1)
        curr_dummy = dummy
        while(curr):
            copy_node = Node(curr.val)
            dict[curr] = copy_node
            curr_dummy.next = copy_node
            curr = curr.next
            curr_dummy = curr_dummy.next
        temp = head
        while(temp):
            dict[temp].random = dict[temp.random]
            temp = temp.next
        return dummy.next