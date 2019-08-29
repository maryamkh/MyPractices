'''
    Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.
    Elements for which no smaller element exist, consider next smaller element as -1.
    Output: An array of prev .smaller value of each item or -1(if no smaller value exists for one item.)
    Example:
    Input 1:
    A = [4, 5, 2, 10, 8]
    Output 1:
    G = [-1, 4, -1, 2, 2]
    Explaination 1:
    index 1: No element less than 4 in left of 4, G[1] = -1
    index 2: A[1] is only element less than A[2], G[2] = A[1]
    index 3: No element less than 2 in left of 2, G[3] = -1
    index 4: A[3] is nearest element which is less than A[4], G[4] = A[3]
    index 4: A[3] is nearest element which is less than A[5], G[5] = A[3]
    '''
class NearestSmallerElement:
    # @param array : list of integers
    # @return a list of integers
    def prevSmaller(self, array):
        nearestIndex = []
        nearestIndex.append(-1)    #first item in array does not have any item in its back==> no smaller value in its back
        if len(array) == 1:
            return nearestIndex
        
        nearestItem = 0
        for pivot in range(1,len(array)):
            stack = array[:pivot]#array[:pivot]
            
            while len(stack) > 0:
                nearestItem = stack.pop()
                if nearestItem < array[pivot]: #pivot:
                    nearestIndex.append(nearestItem) #len(stack) + 1
                    break
        
            if len(nearestIndex) < pivot + 1:    #array[i] has no value smaller than itself in its left side.===> inser -1 in nearestIndex array
                nearestIndex.append(-1)

                    
        return nearestIndex

def main():
    previousSmaller = NearestSmallerElement()
    array = [2,7,-1,9,12,-3]
    result = previousSmaller.prevSmaller(array)
    print result

if __name__ == '__main__':
    main()
