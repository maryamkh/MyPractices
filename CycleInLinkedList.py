'''
contains_cycle() that takes the first node in a singly-linked list and returns a boolean indicating whether the list contains a cycle
Input: :Linked list
Output: True: list contanis a cycle
        False: Otherwise
head->2->3->0->4->Null ===> False
head->2->3->0->  4->Null ===> True
            3<-
psduo code:
travers the linkedlist
put a pointer(Head) that points to the last node of the current node.
if currentNode.next == Head:
    there is a cycle
elif node.next == None:
    No cycle
    retun False
else:
    currentNode = currentNode.next
    Head = currentNode
    there is a cycle
    return True
'''
class node():
    def __init__(self, initData):
        self.data = initData
        self.next = None

def contains_cycle(firstNode):
    #currentNode = firstNode
    #root = firstNode
    checkdSet = set()
    checkdSet.add(firstNode)
    
    result = travers(firstNode, checkdSet)
    return result
    
    
def travers(currentNode, checkdSet):
    if currentNode in checkdSet:
        return True
        
    if currentNode.next is None:
        return False
    
    checkdSet.add(currentNode)
    return travers(currentNode.next, checkdSet)

    
n1 = node(2)
n2 = node(3)
n3 = node(3)
n4 = node(5)
n5 = node(8)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n4.next = n3
result = contains_cycle(n1)
print(result)
if result:
    print ("has cycle")
else:
    print ("has no cycle")
