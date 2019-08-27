#!usr/bin/python

class RecBinSearch:

    def recursiveBinSearch(self, list, number, low, high):

        #base condition
        if low > high:  #the given number is not found in the list
            return False

        mid = (high - low)//2 + low

        if number == list[mid]:
            return True

        if number > list[mid]:  #search in the right half
            low = mid + 1
            self.recursiveBinSearch(list, number, low, high)

        if number < list[mid]:  #search in the left half
            high = mid -1
            self.recursiveBinSearch(list, number, low, high)



def main():

    number = int(raw_input('Enter the number to search for...'))
    list =raw_input('Enter the list of numbers to search within them: 1 3 5...')
    intList = map(int, list.split(' '))

    low = 0
    high = len(intList)
    recursBinS =  RecBinSearch()
    result = recursBinS.recursiveBinSearch(intList, number, low, high)
    if result:
        print 'number exist in the list'
    else:
        print 'number does not exist'

if __name__ == '__main__':
    main()
