#!usr/bin/python
'''
    Find the numbers of ways we can reach the top of the stairs if we can only clime 1 or 2 steps each time?
    Input: Integer: The stair number in which we should reach to
    Output: Integer: The numebr of ways we can clime up to reach target stair
    Reaching any stair with only 1 step climing or 2 steps climing means that we should first reach either:
    1- A stair one step below the target step them make 1 step climing to reach the target step or
    2- Two steps below the target step and then make a 2 steps climing to reach the target
    ===> this means that the function to each step is a fonction of its pervious step + 1 OR the functions of its 2nd previous step + 2: f(n) = f(n-1) + f(n-2)==> This is the fibonnachi series
    Note: For making steps of 1, 2 or 3 climings the function is: f(n) = f(n-1) + f(n-2) + f(n-3)
    
    Solution:
    1- the problem can be solved recursively which contanins many redundent of the implementation of the subproblems.
    2- the second way is to do dynamic programming using buttom-up solution and solve the problem in linear time complexity.
    '''
class StairsSteps:

    def calSteps(self, stairs):
        checkedSteps = []
        for i in range(stairs+1): #init the array with 0
            checkedSteps.append(0)

        if stairs == 1 or stairs == 0:
            checkedSteps[stairs] = 1
            return 1

        for step in range(2, stairs+1):
            if checkedSteps[step] == 0:
                checkedSteps[step] = self.calSteps(step-1) + self.calSteps(step-2)
            else:
                return checkedSteps[step]
        return checkedSteps[step]

                ###############################################################
    def calStepsRecursive(self, stairs):
        if stairs == 0 or stairs == 1:
            return 1

        return self.calStepsRecursive(stairs-1) + self.calStepsRecursive(stairs-2)

def main():

    steps = StairsSteps()
    result = steps.calSteps(4)
    #result = steps.calStepsRecursive(5)
    print result

if __name__ == '__main__':
    main()
