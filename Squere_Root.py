#!/usr/bin/python
'''
    Find the squere root of a number. Return floor(sqr(number)) if the numebr does not have a compelete squere root
    Example: input = 11 ===========> output = 3
    Function sqrtBinarySearch(self, A): has time complexity O(n), n: given input: When the number is too big it becomes combursome
    '''

class Solution:
    def sqrt(self, A):
        n = 1
        while n*n <= A:
            n += 1
        if  A == n*n: return n
        elif n < (n-.5) * (n-.5):   return n-1
        else: return n+1

    def sqrtBinarySearch(self, A):
        searchList = []
        #print range(A)
        for i in range(A):
            searchList.append(i+1)
        
        for i in range(len(searchList)):
            mid = len(searchList)/2
                #if mid > 0:
            number = searchList[mid-1]
            sqrMid = number * number
            sqrMidPlus = (number+1) * (number+1)
            #print 'sqrMid...sqrMidPlus...', sqrMid, sqrMidPlus
            
            if sqrMid == A: return number
            
            elif sqrMid > A:   #sqrt is in the middle left side of the array
                searchList = searchList[:mid]
            #print 'left wing...', searchList
            
            elif sqrMid < A and sqrMidPlus > A: # sqrMid< sqrt(A)=number.xyz <sqrMidPlus==> return floor(number.xyz)
                print
                if (number + .5) * (number + .5) > A:   return number
                return number+1

            else:
                searchList = searchList[mid:]
#print 'right wing...', searchList




def main():
    inputNum = int(input('enter a number to find its squere root: '))
    
    sqroot = Solution()
    result = sqroot.sqrt(inputNum)
    result1 = sqroot.sqrtBinarySearch(inputNum)
    print result
    print result1

if __name__ == '__main__':
    main()
