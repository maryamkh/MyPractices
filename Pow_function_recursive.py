'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
Example:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Time Complexity: O(log(n))===> In this solution n is reduce to half and therefore this is the time cimplexity
Spcae Complexity: We need to do the computation for O(log⁡n) times, so the space complexity is O(log⁡n)
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = abs(n)
        if n==0:
            return 1
        
        res = self.myPow(x, n//2)
        
        if n%2 == 0:
            return res*res  
        else:
            return res*res*x
