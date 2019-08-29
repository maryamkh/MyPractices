class FindLCMOfArray:

    def findLCM(self, array):
        lcm = array[0]
        lcm = self.calLCM(array,lcm)
        print lcm

    def calLCM(self, array, lcm):

        for i in range(1,len(array)):
            gcd = self.calGCD(array[i],lcm)
            print 'gcd of array[i], lcm is:...)', array[i], lcm, gcd
            lcm = lcm * array[i]/ gcd
            print ' new lcm is:...', lcm
        return lcm
    #return calLCM(array[i], lcm)

    def calGCD(self, num1, num2):
#        if num1 == 1 or num2 ==1:
#            return 1
        ####no need to calculate prime values###
#        arr = [num1, num2]
#        for i in range(len(arr)):
#            for j in range(2,int(arr[i]**0.5)+1):
#                if arr[i]%j == 0:  #number is not prime
#                    break
#            else:   #num1 is prime gcd = 1
#                return 1

        if num2 == 0:
            return num1
        return self.calGCD(num2, num1%num2)

def main():
    findLCM = FindLCMOfArray()
    inArray = [2, 7, 3, 9, 4]
    findLCM.findLCM(inArray)

if __name__ == '__main__':
    main()
