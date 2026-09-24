# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # current = head
        # temp = current.next
        # while temp != None:
        #     current = temp
        #     temp = current.next
        #     if temp == None:
        #         return False
        #     if temp.val < current.val:
        #         return True
        # return False

        if head == None:
            return False
        nodes = set()
        nodes.add(head)
        current = head
        temp = current.next
        while temp != None:
            current = temp
            temp = current.next
            if temp == None:
                return False
            if temp not in nodes:
                nodes.add(temp)
            else:
                return True
            
        return False