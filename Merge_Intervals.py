#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
#and return an array of the non-overlapping intervals that cover all the intervals in the input.
#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#T(O): O(nlogn)
#Other than the sort invocation, we do a simple linear scan of the list, so the runtime is dominated 
#by the O(nlog⁡n)complexity of sorting.

#Space complexity : O(log⁡N)(or O(n))
#If we can sort intervals in place, we do not need more than constant additional space,
#although the sorting itself takes O(log⁡n)O(\log n)O(logn) space. Otherwise, we must allocate linear space to store a copy of intervals and sort that.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
