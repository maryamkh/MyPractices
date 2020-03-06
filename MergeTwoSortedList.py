'''
Wire a fucntion to merge two sorted list into one sorted one.
Input:
my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

Output:
orderdMerged = [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
'''

def sortedMerged(list1, lis2):
    loop = len(list1)
    if len(list2) < len(list1):
        loop = len(list2)
      
    first = 0
    end = len(list1) - 1
    for number in list2:
        pos = binSearch(number, first, end, list1)
        print (pos, number)
        list1.insert(pos, number)
        print (list1)
        first = 0
        end = len(list1) -1
        
def binSearch(number, first, end, list1):
    if first > end:
        return first
#    #if end - first == 0:
#    if len(list1[first:end]) == 1:
#        return end
    
    mid = (end - first)//2 + first
    if number == list1[mid]:
        #list1.insert(mid, number)
        return mid
        
    elif number > list1[mid]:
        return binSearch(number, mid+1, end, list1)
    
    else:
        return binSearch(number, first, mid-1, list1)
        
list1 = [3, 4, 6, 10, 11, 15]

list2 = [1, 4, 8, 12, 14, 19]
sortedMerged(list1, list2)
