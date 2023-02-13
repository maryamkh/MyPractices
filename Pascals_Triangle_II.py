#Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#Example 1:
#Input: rowIndex = 3
#Output: [1,3,3,1]
#Constraints:
#0 <= rowIndex <= 33
#Time complexity: O(n^2)
#Space complexity: O(n)

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for i in range(1, rowIndex+2):
            triangle.append([0]*i)
            #print(triangle[i-1])
            for j in range(len(triangle)):
                if j == 0 or j == len(triangle)-1:
                    print(i,j)
                    triangle[i-1][j] = 1
                else:
                    triangle[i-1][j] = triangle[i-2][j-1] + triangle[i-2][j]
        print(triangle)
        last_row = len(triangle)-1
        print(f'final: {triangle[len(triangle)-1]}')
        return triangle[len(triangle)-1]	
