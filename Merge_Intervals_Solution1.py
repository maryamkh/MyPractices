# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
#and return an array of the non-overlapping intervals that cover all the intervals in the input.
#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #intervals.sort(key=lambda x: x[0])
        intervals.sort()
        print(f'sorted: {intervals}')
        merged = list()
        
        arr = intervals[0]
        merged.append(intervals[0])
        print(arr)
        for i in range(len(intervals)):
            print(f'intervals[i][-1]: {intervals[i][-1]}')
            if intervals[i][0] <= merged[-1][1]: 
                merged[-1][1] = max(intervals[i][1], merged[-1][1])
                print(f'merged: {merged}')
            else:  
                merged.append(intervals[i])
                print(f'else merge: {merged}')
                
        return merged
