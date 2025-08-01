'''

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
#this one creates new ListNode but we dont need to
def mergeTwoLists(self, list1, list2):
    dummy = ListNode(-1)
    curr = dummy
    while(list1 and list2):
        if list1.val<list2.val:
            curr.next = ListNode(list1.val)
            list1=list1.next
        else:
            curr.next = ListNode(list2.val)
            list2 = list2.next
        curr = curr.next
    curr.next = list1 if list1 else list2
    return dummy.next

class Solution:
    def mergeTwoLists(self, list1,list2):
        dummy = ListNode(-1)
        curr = dummy
        while(list1 and list2):
            if list1.val<list2.val:
                curr.next = list1
                list1=list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 if list1 else list2
        return dummy.next