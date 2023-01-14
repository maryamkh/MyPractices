class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[2,3,4,7,1,9]
        #A Divide and conquare algorithm
        #Select an index of nums as pivot 1(I selected the value in last index)
        #Define a pointer called partitionin_index in which identifies which index is the index where
        #the values smaller than pivot should be befor this index and the values after this index
        #should be bigger than pivot (pick index=0 as partitioning_index)
        #Start from begining of the list check till the item before pivot, compare each item with 
        #pivot value. 
        #If value of the current item > pivot, swap the current value with value in partitioning index
        #(since all the values bigger than pivot should come after the pivot in the list)
        #select the nex index as partitioning_index (since the partitioning index now has a value less
        #than pivot and we should change the position of this pointer to not mess up with swaped value
        #to this index)
        #Continue checking the values of other indexes with pivot and swap them if condition is true
        #When all the values are compared with pivot and swaped, now move the pivot to the index where 
        #partitioning_index is pointing to ==> Now all the values before pivot are smaller than it and
        #all the values after that are bigger.
        #return back this partitioning index
        #call the quicksort function for all the values from index 0 to partitioning_index -1
        #recursively
        #call the quicksort function for all the values from index partitioning_index +1 to last_index
        #-1 recursively
       
        # Function to find the partition position
        
        def partition(array, low, high):
            '''
            # Choose the rightmost element as pivot
            pivot = array[low]
            i = low
            j = high
            while(i<j):
                #print(f'pivot: {pivot}, i:{i}, array[i]:{array[i]}') 
                #while i<= len(array):   
                for i in range(len(array)):
                    print(f'pivot: {pivot}, i:{i}, array[i]:{array[i]}')
                    if pivot >= array[i]:
                        continue
                        #print("condition")
                        #i = i+1
                        #i+=1
                  #[2,0,1]      
                for j in range(len(array)-1, -1, -1):
                    print(f'pivot: {pivot}, j:{j}, array[j]:{array[j]}')
                    if pivot < array[j]:
                        continue
                        
                print(f'i: {i}, j: {j}')        #j-=1
                if i>j:
                    print('swap')
                    array[i], array[j] = array[j], array[i]
                    print(array)
            array[j] = pivot    
            return j
            '''
            pivot = array[high]
  
            # Pointer for greater element
            partitioning_index = low-1
  
            # Traverse through all elements
            # compare each element with pivot
            for i in range(low, high):
                if array[i] < pivot:
                    # If element smaller than pivot is found
                    # swap it with the greater element pointed by i
                    #partitioning_index = partitioning_index + 1
                    partitioning_index +=1
                    # Swapping element at i with element at j
                    (array[partitioning_index], array[i]) = (array[i], array[partitioning_index])
                    #######partitioning_index +=1


            # Swap the pivot element with 
            # e greater element specified by i
            (array[partitioning_index + 1], array[high]) = (array[high], array[partitioning_index + 1])
  
            # Return the position from where partition is done
            return partitioning_index + 1
  
        # Function to perform quicksort
        
  
        def quick_sort(array, low, high):
            if low < high:
  
                # Find pivot element such that
                # element smaller than pivot are on the left
                # element greater than pivot are on the right
                pi = partition(array, low, high)
  
                # Recursive call on the left of pivot
                quick_sort(array, low, pi - 1)
  
                # Recursive call on the right of pivot
                quick_sort(array, pi + 1, high)
  
  

        quick_sort(nums, 0, len(nums) - 1)
  
        
