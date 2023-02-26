#You are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#Example:
#Input: n = 3
#Output: 3
#Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step

class Solution:
    #top(n) = top (n-1) + top(n-2)
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.stairs(n, memo)

    def stairs(self, n, memo):	
        if n == 1:
            memo[1]= 1
            return 1
        if n == 2:
            memo[2] = 2
            return 2
            
        if n in memo:
            return memo[n]
            
        memo[n] = self.stairs(n-1, memo) + self.stairs(n-2, memo)
        #memo[n] = stairs(n-1) + stair(1)
        return memo[n]
