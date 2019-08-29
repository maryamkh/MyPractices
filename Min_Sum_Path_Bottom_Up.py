#!usr/bin/python
'''
    The approach is to calculate the minimum cost for each cell to figure out the min cost path to the target cell.
    Assumpthion: The movementns can be done only to the right and down.
    In the recursive approach there is a lot of redundent implementation of the sub-problems. With Dynamic programming we optimize the implementation. Dynamic programming is done by bottom-up approach in an iterative loop.
    Main function: calMinCost()
    '''
class MinCostPath:

    def calMinCost(self, matrix, inRow, inCol):
        if len(matrix) == len(matrix[0]) == 1:
            return matrix[0][0]

                #initialize the tracker matrix with 0
        cost = [[0 for col in range(inCol)] for row in range(inRow)]

        print 'cost after init...', cost
        # In the first row and first column the min cost to reach each cell is equal of the cost of the cell + cost of passing all the previous cells
        cost[0][0] = matrix[0][0]
        #if row == 0:
        #for col in range(1, len(matrix[0])):
        for col in range(1, inCol):
            cost[0][col] = cost[0][col-1] + matrix[0][col]
        #print 'matrix[0][col]...', matrix[0][col]

        #if col == 0:
        #for row in range(1,len(matrix)):
        for row in range(1,inRow):
            cost[row][0] = cost[row-1][0] + matrix[row][0]
        #print 'matrix[row][0]..', matrix[row][0]
        print cost

    # To calculate the min cost of other cells, for each cell we calculate the cost of reaching the cell above the target cell and the cell on the left side of the target cell (since the movements can be done only to the down and right) and choose the one which has min cost.
    #for row in range(1,len(matrix)):
    #for col in range(1,len(matrix[0])):
        for row in range(1,inRow):
            for col in range(1,inCol):
                print 'row...col...', row, col
                above = cost[row-1][col]
                print 'above...', above
                left = cost[row][col-1]
                cost[row][col] = min(above, left) + matrix[row][col]
                print 'cost[row][col]...,,,...', cost[row][col]
        print 'row...col....cost[row-1][col-1]...', cost[row-1][col-1]
        return cost[inRow-1][inCol-1]

                #######################################################

    def findPath(self, matrix, row, col):
        print 'in function...'
        if len(matrix) == len(matrix[0]) == 1:
            return mtrix[0][0]
        sum = 0
        #untraversed rows/cols:
        if row >= len(matrix)-1 or col >= len(matrix[0])-1:
          
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
                sum = matrix[row][col+1] + self.findPath(matrix, row, col+1)
            
            else:   #make a down step
                #sum += matrix[row+1][col]
                #row = row + 1
                print 'matrix[row+1][col] in down step...', matrix[row+1][col]
                sum = matrix[row+1][col] + self.findPath(matrix, row+1, col)
        sum = sum + matrix[0][0]
        return sum

def main():
    #matrix = [[1,3], [5,2]]
    matrix = [[1,7,9,2],[8,6,3,2],[1,6,7,8],[2,9,8,2]]
    minPath = MinCostPath()
    #result = minPath.calMinCost(matrix, 4, 4)
    result = minPath.findPath(matrix, 1, 1)
    print result

if __name__ == '__main__':
    main()
