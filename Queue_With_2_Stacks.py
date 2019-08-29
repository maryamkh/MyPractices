#!/usr/bin/python

class QueueWithStacks:
    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def enqueue(self, value):
        self.first_stack.append(value)
                
    def dequeue(self):
        while len(self.first_stack) > 0:
            self.second_stack.append(self.first_stack.pop())
            
        if len(self.second_stack) > 0:
            return self.second_stack.pop()

def main():
    myqueue = QueueWithStacks()
    queue_values =  [1,3,4,6]
    for item in queue_values:
        myqueue.enqueue(item)
        
    print myqueue.dequeue()

if __name__ == '__main__':
    main()
