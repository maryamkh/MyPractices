#!/user/bin/python
'''
    Problem limitation: The overall run time complexity should be O(log(m+n))
    To find the median, we use the binary search
    '''
class Median:

    def __init__(self):
        self.returned = 0
    
    def findMedian(self, A, B):
        while len(B)>0:
            print 'A is...B is...', A, B
            self.insertBinA(A, B[0])
            B = B[1:]
        self.calMedian(A)
        print 'final result...,', A
            
    def insertBinA(self, list, number):
        print 'list in insert function...', list
        low = 0
        high = len(list) - 1
        index = 0
        print 'index before assignment..', index
        self.findPos(list, number, low, high)
        list.insert(self.returned + 1, number)
    
    def findPos(self, list, number, low, high):
        print 'low, high....!!!', low, high
        if high < low:
            print 'before return...', high
            self.returned = high
            return high
        
        mid = low +(high - low)/2
        print 'mid.. low.. high..', mid, low, high
        
        if list[mid] == number:
            return mid
        
        if number > list[mid]: #check the right half
            print 'right...'
            low = mid + 1
            self.findPos(list, number, low, high)

        else:   #check the left half
            print 'left...'
            high = mid - 1
            self.findPos(list, number, low, high)
       
    def calMedian(self, final):
        median = 0
        mid = 0
        mid = len(final)/2
        if mid % 2 == 0:
            median = (final[mid] + final[mid+1])/2
        else:
            median = final[mid]

        print 'median...', median

def main():
    A= [1, 3, 8]
    B = [2, 4, 10]
    fMedian = Median()
    fMedian.findMedian(A, B)

if __name__ == '__main__':
    main()
