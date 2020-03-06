'''
Function fib()
Input : an integer n
Output: nth fibonacci number

Fib seq = 0, 1, 1, 2, 3, 5, 8, 13, ...
n = 0 ---> 0th fib = 0
n = 1 ---> 1st fib = 1 = fib(0) + 1 = 1
n = 2 ---> 2nd fib = 1==(0+1) = fib(0) + fib(1)
n = 3 ---> 3rd fib = 2== (1+1) = fib(1) + fib(2)
n = k ---> kth fib = fib(k-1)+fib(k-2)

Psedo Code:
if n == 0 or n == 1
    return  n
else:
    retrun fib(n-1) + fib(n-2)
'''

def fib(n):
    if n == 0 or n == 1:
        return n
    return(fib(n-1) + fib(n-2))

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
