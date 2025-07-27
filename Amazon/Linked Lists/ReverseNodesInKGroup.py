# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#TC: O(n*k)  SC= O(1)
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        -1->1->2->3->4->5
        prev = dummy
        curr=dummy
        k iteration with curr and save next=curr.next
        reversed = reverse(head,k) = 2->1->next
        prev.next = reversed
        prev = reversed
        '''
        dummy = ListNode(-1)
        dummy.next = head
        oldPrev = dummy
        curr = dummy
        oldNext = None
        
        def reverseNode(h,c,nxt):
            prev = nxt
            while(h!=nxt):
                next = h.next
                h.next = prev
                prev = h
                h = next
            return prev
        
        while(True):
            count = k
            print(curr)
            while(count and curr):
                curr=curr.next
                count-=1
            print(count)
            if not curr: #i made a mistake here where I did k!=0 instead of not curr, be careful
                break
            print(curr)
            oldNext = curr.next #-1->1->2->3->4->  oldNext = 3, 5
            reversedNode = reverseNode(head,k,oldNext) # 2->1->3->4->5       4-3-5
            oldPrev.next = reversedNode #-1->2->1->3->4->5    1->4->3->5
            oldPrev = head #1 , 3
            curr = head #1 , 3   #made mistake here I had this line and the line below swapped which caused issues
            head = oldNext #3, 5
        return dummy.next
            
    