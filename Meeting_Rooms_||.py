#Problem:
#Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
#We need to have a room available for meeting if all the occupied rooms are still busy with a meeting. This means that if a start_time of a new meeting is 
#before end_time of the ongoing meeting, we should allocate a new room for this new meeting. ===> The start_times of the meetings should be compared to 
#end_time of the meetings and decide whether a new rooms is required?
#Example:[[0,30], [5,10], [15, 20]
#We define a variable rooms which tells un in any given point of time, what is the number of meetings going on? 
#Question asks about max number of required rooms, which means that the answer is the max value that rooms would have which counting the number of required
#rooms. 
#If the start_time of a meeting is equal to the end_time of an other meeting, we do not need a new rooms since the new meetig can just be held in the room
#where the already finished meeting(at the time of starting of this new meeting) was running.
#Store start times and end times in 2 different arrays. Sort arrays.
#Asign a pointer to each array and start traversing arrays comparing the first start_time with the first end_time. obviously for the first one we need to 
#one room (rooms+=1. Then we increment the pointer in the starts array and compare the next value of the array with the end time to see if we need a new room?
#If, so incremment the rooms and move on to the next value in the starts array. If the comparison of the start_time and end_time results in the fact thet a
#room is released (start_time>end_time), this means that the number of rooms we need at the moment is one less since one room is released. Therefore: rooms
#-= 1. But since the question asks about max required rooms, we should always keep track of the max value of required rooms. There fore in each round that
#we check that we calculate the number of required rooms for that momemnt (value of the variable rooms) we keep the max value in an other variable (result)
#to not lose the max value or required rooms.

class Solution:
    #Store start times and end times in 2 different lists
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        #[[0,30],[5,10],[15,20]]
        rooms = 0
        starts = list()
        ends = list()
        result = 0
        
        for meeting in intervals:
            starts.append(meeting[0])
            ends.append(meeting[1])
        
        starts.sort()
        ends.sort()
        start_pointer = 0
        end_pointer = 0
        result = 0
        #if the starting time is earlier than the ending time means we need a new meeting room
        #for i in range(len(starts)):
        while(start_pointer < len(starts)):
            if starts[start_pointer] < ends[end_pointer]:
                print(f'1start: {starts[start_pointer]}, end: {ends[end_pointer]}')
                rooms += 1
                start_pointer += 1   #increment the start_pointer to check the next start time with 
                #the current end_time
                
            #if start_time is bigger that current ending time, it means that a room is released.
            #===> The number of required rooms should be decreased by one
            #elif start_pointer < len(starts) and starts[start_pointer] > ends[end_pointer]:
            #If start time is after or at the same time of an end time, it means that we have a free room available for this meeting to be started.
            #Therefore the number of occupied rooms (rooms) should be decreased by one (rooms -= 1). Also, move the end_pointer to check the
            #next end time
            elif starts[start_pointer] >= ends[end_pointer]:
                print(f'3start: {starts[start_pointer]}, end: {ends[end_pointer]}')
                print(start_pointer)
                end_pointer += 1  #increment the end_pointer to check the next end time with the current start_time
                rooms -= 1        #decrement the number of occupied rooms. Since one rooms is just released. 
            result = max(rooms, result)
        return result
       
