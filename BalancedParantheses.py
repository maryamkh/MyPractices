#!usr/bin/python
'''
    The program checks only for the parantheses (), [], {}. The rule is that any opening paranthese should ends with a closing
    paranthese of the same type otherwise the parantheses are not balanced.
    In fact the last opening panathese should ends with the same closing paranthes.
    We can use a stack to check if this true? We add any opening paranthese into a stack and check the rest of the string when reaching to the next paranthese, then we check the last elemnt of the stack to see whether it is the opening paranthese of the same type? if yes we remove this last element from our stack (since we have found its closing paranthese in its correct place) and continue searchin in the string. If not the parantheses are not balanced ( each opening paranthese has not its closing part at the right place), therefore we exit from the loop and return 0.
    Output: 1: if parantheses are balanced
    0: if parantheses are not balanced
    '''
class BalancedParantheses:
    def CheckParantheses(self, string):
        openParsStack = []
        par = ''
        for char in string:
            if char == '(' or char == '[' or char == '{':
                openParsStack.append(char)    #push paranthese into the stack

            elif char == ')' and len(openParsStack) > 0 and openParsStack.pop() is not '(':
                return 0

            elif char == ']' and len(openParsStack) > 0 and openParsStack.pop() is not '[':
                return 0

            elif char == '}' and len(openParsStack) > 0 and openParsStack.pop() is not '{':
                return 0

        if len(openParsStack) == 0: #All the opening parantheses have a closing one
            return 1
        return 0

def main():
    balancedPars = BalancedParantheses()
    string = '()[[]]{(mmkk}'
    result = balancedPars.CheckParantheses(string)
    print result

if __name__ == '__main__':
    main()
