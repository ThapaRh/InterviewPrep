'''

'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        i = 1
        d = ListNode(-1)
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        d.next = lists[0]
        def mergeNodes(n1,d):
            node1 = lists[n1]
            node2 = d.next
            dummy = ListNode(-2)
            c = dummy
            while(node1 and node2):
                if node1.val<node2.val:
                    dummy.next = node1
                    node1=node1.next
                else:
                    dummy.next = node2
                    node2=node2.next
                dummy = dummy.next
            if(node1):
                dummy.next = node1
            if(node2):
                dummy.next = node2
            d.next = c.next
                
        while(i<len(lists)):
            mergeNodes(i,d)
            i+=1
        return d.next
    
#we could just put everything in array better is heap and then create new linkedlist poppong that heap