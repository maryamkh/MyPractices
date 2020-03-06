'''
Fid the middle value of a given linked list
Input: Head to the given Linked list
Output: A value located in the middle node of the given list
1->3->4->5->4
Linked list is a linear data structure which if it is singly it can only be traveres forward and the accessibility to its items are only through traversing the list ===> To get access to the middle node we have to start travesring the list from the begininig but since we cannot get the size of the list till we reach the end of the list we can do 2 things to get the middle node:
1- Travers the whole list and keep the nodes in a list (not set since set doesn't have index and does not have direct access possibility to its elements since it is not defined for this purpose) and then get the value of the middle node out of the list.
2- Use 2 pointers:
Pointer 1: travers the whole linked list
Pointer 2: travers the list with the speed of half of the speed of pointer 1 ===> For every 2 moves of pointer 1, pointer 2 will move one step forward ===> When the pointer 1 reaches the end of the list, pointer 2 is in the middle of the list ===> We can read the middle node value

Head->2->3->5->1       2->3->Head->5->1
headHalf->2->3->5->1   2->headHalf->3->5->1
Pseducode:
Head = Biggining of the list
headHalf = Biggining of the list
If Head.next is not None:
    Move head one step forward
    Increment headConter by one
if headCounter = 2:
    move headHalf pointer one setp forward
    headConter = 0
if not go to setp 15
'''

class node():
    def __init__(self, initData):
        self.data = initData
        self.next = None
        
def midValueofLinkedList(Head):
    headCounter = 0
    headHalf = Head
    while Head.next is not None and Head.next.next is not None:
        print('here')
        Head = Head.next.next
        headHalf = headHalf.next
    #midValue = traversList(Head, headHalf, headCounter)
    midValue = headHalf.data
    return midValue
    
def traversList(Head, headHalf, headCounter):
    if Head.next is None:
        #print(headHalf.data)
        return headHalf.data
    
    headCounter += 1
    if headCounter == 2:
        headHalf = headHalf.next
        headConter = 0
            
    
    return traversList(Head.next, headHalf, headCounter)

n1 = node(1)
n2 = node(3)
n3 = node(5)
#n4 = node(1)
#
n1.next = n2
n2.next = n3
#n3.next = n4

midValue = midValueofLinkedList(n1)
print(midValue)
