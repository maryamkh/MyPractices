#!usr/bin/python
'''
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    push(x) – Push element x onto stack.
    pop() – Removes the element on top of the stack. Do nothing on empty stack
    top() – Get the top element. Retunrs -1 on empty stack
    getMin() – Retrieve the minimum element in the stack. Retunrs -1 on empty stack
    Note: All the operations have to be constant time operations.
    '''
class MinStack:
    # @param x, an integer
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    # @return nothing
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()

    # @return an integer
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return -1


    # @return an integer
    def getMin(self):
        min = self.top()
        tempStack = self.stack[:]   #make a clone of stack not a copy
        for r in range(len(self.stack)):
            if self.top() < min:
                min = self.top()
                self.pop()
        self.stack = tempStack
        return min

def main():
    myStak = MinStack()
    result = []
    result.append(myStak.push(19))
    result.append(myStak.push(7))
    result.append(myStak.push(6))
    result.append(myStak.getMin())
    result.append(myStak.push(4))
    result.append(myStak.getMin())
    result.append(myStak.pop())
    result.append(myStak.getMin())
    print result

if __name__ == '__main__':
    main()
