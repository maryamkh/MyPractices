#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
#and return an array of the non-overlapping intervals that cover all the intervals in the input.
#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        starts = []
        ends = []
        for i in range(len(intervals)):
            starts.append(intervals[i][0])
            ends.append(intervals[i][-1])
        starts.sort()
        ends.sort()
        start_p = 0
        end_p = 0
        merged = list()
        print(starts)
        print(ends)
      
        arr = [starts[0], ends[0]]
        
        while(end_p < len(starts)):
            print(f'start_p, end_p {start_p}, {end_p}')
            print(f'{starts[start_p]}, {ends[end_p]}')
            if starts[start_p] <= arr[1]:
                ending = ends[end_p]
                print(f'ending: {ending}')
                arr = [arr[0], ending]
                print(f'arr: {arr}')
                print(f'merged: {merged}')
                start_p += 1
                end_p += 1
                
            else:
                print("else:")
                
                merged.append(arr)
                print(f'else merged: {merged}')
                arr = [starts[start_p], ends[end_p]]
                print(f'else: arr: {arr}')
               
                print(f'else: arr: {arr}')
                
        merged.append(arr)
        print(merged)     
        return(merged)
