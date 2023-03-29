'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
Example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Input: list1 = [], list2 = [0]
Output: [0]
Time Complexity: O(m+n)
Space Complexity: O(1)
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        print(merged.val, list2)
        dummy_head = merged
        print(dummy_head)
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                #merged.val = list1.val
                merged.next = list1
                list1 = list1.next
               
            elif list2.val < list1.val:
                merged.next = list2
                list2 = list2.next
            print(f"current: {merged.val}, {merged.next}")   
            merged = merged.next
            #print(merged) 
        if list1 is not None:
            merged.next = list1
        else:
            merged.next = list2
        return dummy_head.next
