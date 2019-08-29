'''
    Given an array of positive numbers, find the maximum sum of a subsequence with the constraint that no 2 numbers in the sequence should be adjacent in the array.
    Examples :
    Input : arr[] = {5, 5, 10, 100, 10, 5}
    Output : 110
    Solution: In each index we calculate sum including current index such that:
    incl = array[currentIndex] + previous Excluding element (since sum should be with inadjucent elements)==> our max sum is either the new calculated incl value or the our previous includ==> maxSum = max(new incl, old incl) = max(array[currentindex]+excl, incl)==> the result of this max is our new incl value (infact in each index we decide on what is the best max sum we can have including our including values and our current value which is either to sum our current index with all previous non excluding ones or just keep our previous including one)
        The new excluding value then will be our previous including value
    '''

def findMaxSumOfInadjucentElements(array):

    incl = arra[0]
    excl = 0
    temp = 0
    
    for i in range(len(array)):
        temp = incl
        incl = max(incl, excl + array[i])
        excl = temp
    


