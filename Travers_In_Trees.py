#!/usr/bin/python
''' In this program I create a binary tree and then travers the tree in different orders.
    The travers function can be onsidered for any kind of tree
    '''
class Node:
    def __init__(self, node):
        self.node = node
        self.right = None
        self.left = None

    def insert(self, newNode):
        if self.node:   #the root (parent) exists
#compare the new node with the root node to decide whether it should be in right ot left tree
            if newNode > self.node: #put it in the right tree
                if self.right is None:  #the parent node has no right child (right tree),
                    #create right subtree of the node
                    self.right = Node(newNode)

                else:   #the node already has right subtree,
                    #insert the new node into the tree
                    self.right.insert(newNode)

            elif newNode < self.node: #put it in the left tree
                if self.left is None:   # the parent node has no left child (left tree)
                    #create the left subtree of the node
                    self.left = Node(newNode)
                
                else:   #the node already has left subtree,
                    #insert the new node into the tree
                    self.left.insert(newNode)

        else:
            self.node = newNode
                
    '''
    Print the tree
    '''
    def printTree(self):
        print 'in printTree function...'
        if self.left:
            self.left.printTree()
        
        print slef.node,

        if self.right:
            self.right.printTree()

    '''
    to travers the tree we always start from the root node since we have not access to a random node
    in the tree
    This travers reades as this: left subtree--> root node--> right subtree
    Output: a list containing all nodes in inordertraversal format
    '''
    def inOrderTraverse(self, root):
        nodesList = []
        if root:
            nodesList = self.inOrderTraverse(root.left)
            nodesList.append(root.node)
            nodesList = nodesList + self.inOrderTraverse(root.right)
        return nodesList

    '''
    This travers reades as this: Root--> left subtree--> right subtree
     Output: a list containing all nodes in postordertraversal format
    '''
    def preOrderTraverse(self, root):
        nodesList = []
        if root:
            nodesList.append(root.node)
            nodesList = nodesList + self.preOrderTraverse(root.left)
            nodesList = nodesList + self.preOrderTraverse(root.right)
        return nodesList

    '''
    This travers reades as this: Left subtree--> right subtree--> root
    Output: a list containing all nodes in postordertraversal format
    '''
    def postOrderTraverse(self, root):
        nodesList = []
        if root:
            nodesList = nodesList + self.postOrderTraverse(root.left)
            nodesList = nodesList + self.postOrderTraverse(root.right)
            nodesList.append(root.node)
        return nodesList

def main():
    root_node = int(input('please enter the root node: '))
    root = Node(root_node)
    root.insert(20)
    root.insert(16)
    root.insert(91)
    root.insert(10)
    root.insert(18)

    '''root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)'''
    print (root.inOrderTraverse(root))    #pass the root object to the function
    print (root.preOrderTraverse(root))    #pass the root object to the function
    print (root.postOrderTraverse(root))    #pass the root object to the function

if __name__ == '__main__':
    main()
