'''
loop thru lists:
sum 
createnode and put it there
store carryover 
go to next, sum carry over plus whatever is there
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carryOver = 0
        dummy = ListNode(-1)
        curr = dummy
        while(l1 and l2):
            sum = l1.val + l2.val + carryOver
            curr.next = ListNode(sum%10)
            carryOver = sum//10
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
            
        while(l1):
            sum = l1.val+carryOver
            curr.next = ListNode(sum%10)
            carryOver = sum//10
            curr=curr.next
            l1=l1.next
        while(l2):
            sum = l2.val+carryOver
            curr.next = ListNode(sum%10)
            carryOver = sum//10
            curr=curr.next
            l2=l2.next
        if carryOver!=0:
            curr.next = ListNode(carryOver)
        return dummy.next
    
    #cleaner version
    def addTwoNumbers(self, l1, l2):
        carryOver = 0
        dummy = ListNode(-1)
        curr = dummy
        while(l1 or l2 or carryOver):
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carryOver
            curr.next = ListNode(sum%10)
            carryOver = sum//10
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2  else None
        return dummy.next
            
        
        pass
