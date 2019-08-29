#!usr/bin/python
class SearchRotatedSortedArray:
    
    def searchNumber(self, array, number):    #[3,5,6,9,12,13,20] [9,12,13,20,3,5,6]
        pivot_index = self.findPivot(array)
        if array[pivot_index] == number:
            return pivot_index
        left = array[:pivot_index]
        right = array[pivot_index+1:]
        if  left[0] <= number <= left[-1]:    #number is in the left array
            low = 0
            high = len(left) - 1
            index =self.binSearch(number, left, low, high)
        
        elif right[0] <= number <= right[-1]:   #number is in right array
            low = 0
            high = len(right) - 1
            index = self.binSearch(number, right, low, high)
        
        return index
            
    def binSearch(self, number, array, low, high):
        if high < low:
            return -1
                
        mid = (high -low)/2 + low
        if number > array[mid]:
            return self.binSearch(number, array, mid+1, high)
                
        elif number < array[mid]:
            return self.binSearch(number, array, low, mid-1)
                
        return mid
                    
    def findPivot(self, array):
        for index in range(len(array)-1):
            if array[index] > array[index+1]:
                return index+1

def main():
    rotatedSortedArray = SearchRotatedSortedArray()
    number = 0
    array = [4, 5, 6, 7, 0, 1, 2]
    result = rotatedSortedArray.searchNumber(array, number)
    print result
#    recResult = factorial.calFactorialRecursive(number)
#    linResult = factorial.calFactorialLinearly(number)
#    print 'Recursive result...', recResult
#    print 'Linear result...', linResult

if __name__ == '__main__':
    main()

