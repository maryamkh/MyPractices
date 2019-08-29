class Stack(object):
    
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
    
    def push(self, item):
        """Push a new item onto the stack"""
        print 'item to push:...', item
        self.items.append(item)
    
    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        
        return self.items.pop()
    
    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack(Stack):
    #import Stack(Stack)
    def get_max(self):
        print 'get max...'
        stackCopy = self.items[:]
        print 'stack is...', stackCopy
        max = self.items[-1]
        print 'max...', max
        for item in self.items:
            #print 'item...', item
            if self.peek() > max:
                #print 'self.peek..', self.peek()
                max = self.peek()
            #print 'new max...', max
            self.pop()
    
        self.items = stackCopy
        print 'self.items...', self.items
        return max

def main():
    
    inArray = [2, 7, 3, 9, 4]
    stackMax= MaxStack()
    for item in inArray:
        stackMax.push(item)
    result = stackMax.get_max()
    print 'max is ...', result

if __name__ == '__main__':
    main()
