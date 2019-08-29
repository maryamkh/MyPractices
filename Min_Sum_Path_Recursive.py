#!usr/bin/python
'''
    This program finds the min sum path in a matrix from the top left to bottom right of the matrix.
    Condition: the movements can be done only to the right to down
    
    1- The recursive approach: In this approach many sub problems are solved multiplet imes. The time complexity is O(n^2) since there are 2 options(down/right).===> not a good option
    2- The Dynamic programming approach: To avoid redundent implementation of the solution to sub-problems.
    '''
import math
class MinSumPath:
    def findMinSumPath(self, matrix):
        row = 0
        col = 0
        topLeftVal = matrix[0][0]

#        result = self.findPath(matrix, row, col)
#        result += topLeftVal
#        return result

    ####################################################################
        sum = matrix[0][0]
        result = self.findPathRecursive2(matrix, row, col, sum)
        return result
    
    def findPath(self, matrix, row, col):
        if len(matrix) == len(matrix[0]) == 1:
            return mtrix[0][0]
        
        #base case:
        if row >= len(matrix)-1 or col >= len(matrix[0])-1:
            sum = 0
            while row < len(matrix) - 1: #we are in the last col of the matrix and should travers all the remaining rows till reaching the bottom-right corner
                sum += matrix[row+1][-1]
                print 'sum in row travers...', sum
                row += 1
        
            while col < len(matrix[0]) - 1:    #we are on the last row of the matrix and should travers all the remaining columns to reach the bottom-right corner of the matrix
                sum += matrix[-1][col+1]
                print 'sum in column travers...', sum
                col += 1
            return sum
            
        if row < len(matrix)-1 and col < len(matrix[0])-1:
            if matrix[row][col+1] < matrix[row+1][col]: #make a right step
                #sum += math.min(matrix[row][col+1], matrix[row+1][col])
                #sum += matrix[row][col+1]
                #col = col + 1
                print 'matrix[row+1][col] in righ move...', matrix[row][col+1]
                return (matrix[row][col+1] + self.findPath(matrix, row, col+1))
                
            else:   #make a down step
                #sum += matrix[row+1][col]
                #row = row + 1
                print 'matrix[row+1][col] in down step...', matrix[row+1][col]
                return (matrix[row+1][col] + self.findPath(matrix, row+1, col))


    def findPathRecursive2(self, matrix, row, col, sum):
        if len(matrix) == len(matrix[0]) == 1:
            return matrix[0][0]

        if row == len(matrix) - 1 and col == len(matrix[0]) - 1 :
            print 'final sum...', sum
            return sum

#        if row == len(matrix) - 1 and col < len(matrix[0]) - 1:
#            print 'in last row: ... and col:...sum:', row, col, sum
#            return sum + self.findPathRecursive2(matrix, row, col+1, sum)
#
#        if col == len(matrix[0]) - 1 and row < len(matrix) - 1:
#            print 'in last column...'
#            return sum + self.findPathRecursive2(matrix, row+1, col, sum)

        if row < len(matrix) - 1 and col < len(matrix[0]) - 1:
            print 'row... col..., sum', row, col, sum
            return sum + min(self.findPathRecursive2(matrix, row+1, col, sum), self.findPathRecursive2(matrix, row, col+1, sum))


def main():
    #matrix = [[1,7,9,2],[8,6,3,2],[1,6,7,8],[2,9,8,2]]
    matrix = [[1,3], [5,2]]
    minPath = MinSumPath()
    result = minPath.findMinSumPath(matrix)
    print result

if __name__ == '__main__':
    main()
