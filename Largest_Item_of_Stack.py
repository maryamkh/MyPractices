#!usr/bin/python
class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not slef.stack:
            return None
        self.stack.pop()

    def peek(self):
        '''return the last item without removing it'''
        if not self.stack:
            return None

        return slef.stack[-1]

class MaxStack(Stack):
    
    def get_max(self):
        max = 0
        temp = 0
        stackSize = len(Stack.stack)
        
        
        for i in range(stackSize):
            temp = Stack.peek()
            if temp > max:
                max = temp
            Stack.push(temp)
            Stack.pop()
        return max

    def get_max_recursive(self, max):
        temp = Stack.peek()
        
        if temp is None:
            return max
        
        if temp > max:
            max = temp
        
        Stack.push(temp)
        Stack.pop()
        get_max_recursive(max)

def main():
    stackInstance = Stack()
    stack.push(1)
    stack.push(3)
    stack.push(2)
    maxVal = MaxStack(Stack)

if __name__ == '__main__':
    main()
