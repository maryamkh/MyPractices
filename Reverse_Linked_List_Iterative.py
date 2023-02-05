# Given the head of a singly linked list, reverse the list, and return the reversed list.
#Constraints:
#The number of nodes in the list is the range [0, 5000].
#-5000 <= Node.val <= 5000
#Time Complexity: O(n)
#Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curr = head.next
        prev = head
        head.next = None
        if curr is None:
            return head
        while curr.next is not None:
            next = curr.next
            curr.next= prev
            prev = curr
            curr = next 
        curr.next = prev
        return curr
