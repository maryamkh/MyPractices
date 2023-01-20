#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

#If target is not found in the array, return [-1, -1].

#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #Binary search
        low = 0
        high = len(nums)  
        mid = (high-low)//2 + low
        #[1,1,2,6]
                
        def find_target(low, high, nums, target):
            print(f'low: {low}, high: {high}')
            if len(nums) == 0 or low >= high:
                return -1
           
            mid = (high-low)//2 + low
            print(f'mid: {mid}')
            if target > nums[mid]:  #search the righ half
                low = mid +1  
                return find_target(low, high, nums, target)
            
            if target < nums[mid]:  #search the left half
                high = mid
                return find_target(low, high, nums, target)
            
            if target == nums[mid]:
                #count = nums.count(target)
                #if count == 1:
                return mid
                #else:
                #    if 
        target_pos = find_target(low, high, nums, target)
        print(target_pos)
        target_count = nums.count(target)
        if target_count == 0:
            return[-1, -1]
        if target_count == 1:
            return [target_pos, target_pos]
        if target_pos < len(nums)-1 and target_pos > 0:   #the target is not the last element of the 
            #list ==> Check both right and left side if the target for repeatitive taregt values if any
            
            if nums[target_pos+1] > target: #look for positions before found position(target_pos)
                return[target_pos - target_count+1 ,target_pos]
            
            if nums[target_pos-1] < target:
                return[target_pos, target_pos + target_count-1]
            
            #nums[target_pos-1] = target = nums[target_pos+1]==> 3 items are already found
            new_count = target_count - 1
            print(new_count)
            first_pos, end_pos = 0, 0
            for i in range(1, new_count):
                if target_pos + i < len(nums):
                    if nums[target_pos+i] == target:
                        end_pos = target_pos + i
            for i in range(new_count):
                if target_pos - i > -1:
                    if nums[target_pos-i] == target:
                        first_pos = target_pos - i
            return[first_pos, end_pos]
               
        if target_pos == 0:
            return[target_pos, target_pos + target_count-1]
         
        if target_pos == len(nums) - 1:
            return[target_pos - target_count+1, target_pos]
            
