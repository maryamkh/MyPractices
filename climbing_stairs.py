#You are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#Example:
#Input: n = 3
#Output: 3
#Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step
'''
This problem is Dynamic programming problem. We cal look at this problem in a tree (like brute forth) starting from stair zero and then each time taking either 1 step or 2 steps until we reach the 
final stair (stair n). ===> A Tree has a recursive solution and since some of the steps are redundent we can haveme memoization.
To reach step n, we have 2 ways:
1- Stay on stair n-1 and take 1 step to reach stair n.
2- Stay on stair n-2 and take 2 steps to reach stair n.
======>number of ways to reach step n = number of ways to reach step n-1 + number of steps to reach step n-2.
Time Complexity T(O) = O(n) ===> Since I usded "memoization" then each step is implemented only once and there is no redundent implementation.
Space Complexity S(O) = O(n)
'''
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
