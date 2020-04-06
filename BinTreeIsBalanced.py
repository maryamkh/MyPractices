#!/usr/bin/python

class Node:
    def __init__(self, data):
        #create a node
        self.data = data;
        self.right = None
        self.left = None
        print self.data, self.right, self.left, '\n'
    
    #add new node to the binary tree
    def insert(self, data):
        print 'data is:  ', data
        if self.data:   #root node exists
            print 'self.data is:  ', self.data
            if self.data > data:    #add node to the left subtree
                print 'in left subtree\n'
                if self.left is None:
                    print 'parent node when creating left...', self.data
                    self.left = Node(data)  #create a new node on the left side to create left subtree
                else:
                    self.left.insert(data)
            
            elif self.data < data:
                print 'in right subtree\n'
                if self.right is None:
                    print 'parent node when creating right...', self.data
                    self.right = Node(data) #create a new node on the right subtree
                
                else:
                    self.right.insert(data) #add node(data) to the right subtree

        else:       #create the root node
                self.data = data

    #print whole tree
    def printTree(self):
        if self.left:
            print 'it is left tree...'
            self.left.printTree()

        print(self.data),            #Reads the numbers in ascending order (in-order travers)

        if self.right:
            print 'it is right tree...'
            self.right.printTree()
#print(self.data)                       #Reads  first the left subtree (not in order), then raight subtree and then the root node (post-order)

def calculateTreeHeight(self, root):
    if root:
        leftHeight = leftTreeHeight(self, root)
        rightHeight = rightTreeHeight(self, root)
        if abs(leftHeight - rightHeight) <=1:
            #if leftHeight == rightHeight or leftHeight = rightHeight + 1 or leftHeight = rightHeight -1:
            return True
        return False

def leftTreeHeight(self, root):
#nodeCounter = nodeCounter + self.leftTreeHeight(root.left)
    if root is None:
        return 0
    return self.leftTreeHeight(root.left)

def rightTreeHeight(self, root):
    #nodeCounter = nodeCounter + self.leftTreeHeight(root.left)
    if root is None:
        return 0
    return self.rightTreeHeight(root.right)

def main():
    print 'this is main'
    input = int(input("enter the root node value: "))
    root = Node(input)
    root.insert(20)
    root.insert(16)
    root.insert(91)
    root.insert(10)
    root.insert(18)
    root.printTree()
#root.insert(91)

if __name__ == '__main__':
    main()
