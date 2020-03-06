'''
Reverse back a linked list
Input: A linked list
Output: Reversed linked list

In fact each node pointing to its fron node should point to it back node ===> Since we only have one direction accessibility to a link list members to reverse it I have to travers the whole list, keep the data of the nodes and then rearrange them backward.
Example:
Head -> 2-> 3-> 9-> 0
Head -> 0-> 9-> 3-> 2

Pseudocode:
currentNode = Head
nodeSet = set ()
While currentNode != None:
    nodeSet.add(currentNode.next)
    currentNode = currentNode.next
    
reversedSet = list(reverse(set))
currentNode = Head
while currentNode != None:
    currentNode.value =  reversedSet.pop()
    currentNode = currentNode.next
Tests:
Head -> None
Head -> 2
Head -> 0-> 9-> 3-> 2
'''
class node:
    def __init__(self, initVal):
        self.data = initVal
        self.next = None
        
def reverseList(Head):
    currNode = Head
    nodeStack = []
    while currNode != None:
        #listSet.add(currNode)
        #nodeStack.append(currNode.data)
        nodeStack.append(currNode)
        currNode = currNode.next
        
#    currNode = Head
#    print (nodeStack)
#    while currNode != None:
#        #currNode.value = listSet.pop().value
#        currNode.value = nodeStack.pop().data
#        print (currNode.value)
#        currNode = currNode.next
    if len(nodeStack) >= 1:
        Head = nodeStack.pop()
    currNode = Head
    #print (currNode.data)
    while len(nodeStack) >= 1:
        currNode.next = nodeStack.pop()
        #print (currNode.data)
        currNode = currNode.next
        #print (currNode.data)
        
        
        
        
def showList(Head):
    #print(f'list before reverse: {Head}')
    while Head != None:
        print(f'{Head.data}')
        Head = Head.next
    print(f'{Head}')
    
#Head = None
#print(f'list before reverse:\n')
#showList(Head)
#reverseList(Head)
#print(f'list after reverse:\n')
#showList(Head)





def reverse(Head):
    nxt = Head.next
    prev = None
    Head = reverseList1(Head,prev)
    print(f'new head is: {Head.data}')
    
def reverseList1(curr,prev):
#Head->2->3->4
#None<-2<-3<-4
    if curr == None:
        return prev
    
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
    return reverseList1(curr, prev)

n1 = node(2)
Head = n1
#print(f'list before reverse:\n')
#showList(Head)
#reverseList(Head)
#print(f'list after reverse:\n')
#showList(Head)

n2 = node(0)
n3 = node(88)
n4 = node(22)
n1.next = n2
n2.next = n3
n3.next = n4
Head = n1
print(f'list before reverse:\n')
showList(Head)
##reverseList(Head)
reverse(Head)
Head = n4
print(f'n1 value: {Head.data}')
showList(Head)

