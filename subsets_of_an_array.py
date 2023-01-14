#Given an integer array nums of unique elements, return all possible subsets (the power set).
#The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #items of list nums can have 2^len(nums) different subsets
        #We rotate a 1(j in th code) along the items of nums, in each iteration of 2^len(nums) 
        #iterations to find the subsets in that iteration
        #Example: 
        #nums=[1,2,3]=> 2^3 = 8: There are 8 subsets ==> 0,1,2..,7
        #if i=0, rotate 1, three times (len(nums))(to travers all the items of nums list) and logical & 
        #it with i to identify if the item is a member of the subset. if the result of & is 1 it means 
        #the item is a member of subset ==> j=0: 1==> (i=0) & (j=1) = 0: No item is selected. j=1: 
        #shift 1 once to the left: 10==> (i=0) & (j=10)=0: No item, j=2: shift 1 twice: (i=0) & (j=100)
        # = 0
        #i=3, j=0: (i=011)&(001)=001: Item at index 0 is a member of subset (subsets=[1])
        #i=3, j=1: (i=011)&(010)=010: Item at index 1 is a member of subset (subsets=[1,2])
        #i=3, j=2: (i=011)&(100)=000: No item is selected.==> The subset for i=3 is [1,2]
        result=[]
        for i in range(2**len(nums)):  #rotate 2^len(nums)
            subsets = []
            for j in range(len(nums)): #rotate number of along the items of nums
                if (1<<j & i):    #rotate 1 and & it with value of i, where the result of & is 1 it
                    #means that the item in j is a member of this subset
                    subsets.append(nums[j])
                    
            #add the created subset to final list
            print(f'subsets: {subsets}')
            result.append(subsets)
            #print(result)
        return result
