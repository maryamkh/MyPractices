#!usr/bin/python
'''
    Bubble Sort:
    Two adjucent elements are compared and if they are not in order they are swapped
    The pass through the list is repeated until the whole list is sorted.
    Algorithm is ver slow and impratical and can be practical if the input is in mostly sorted order with some elements out of order nearly in position.
    Worst-case and avg complexity: O(n^2) > O(nlogn): typical complexity of sorting algorithms
    '''
class BubbleSort:

    #sort ascendingly
    def bubbleSort(self, inList):
        temp = 0
        print 'inList...', inList
        for i in range(len(inList)-1):
            for j in range(len(inList)-1):
                if inList[j] > inList[j+1]:
                    temp = inList[j]
                    inList[j] = inList[j+1]
                    inList[j+1] = temp
        


def main():
    list = [7, 128, 12, 9, 3, 5,1, 12, 0, 18]
    bubble = BubbleSort()
    bubble.bubbleSort(list)
    print 'sorted list...', list
                       
if __name__ == '__main__':
    main()
