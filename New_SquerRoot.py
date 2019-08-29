class SquerRoot:
    def findSR(self, number):
        print 'in function'
        for i in range(number/2+1):
            #print i
            if i*i > number:
                print 'in if'
                #print number
                return i - 1
            elif i*i == number:
                print 'in else'
                #print number
                return i

def main():
    
    sqr = SquerRoot()
    number = 12
    result = sqr.findSR(number)
    #result = steps.calStepsRecursive(5)
    print result

if __name__ == '__main__':
    main()
