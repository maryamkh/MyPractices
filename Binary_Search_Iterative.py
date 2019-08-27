#!/usr/bin/python
class IterativeBinSearch:

    def iterSearch (self, list, number):
        print 'list....', list
        low = 0
        high = len(list)-1
        #mid = (high - low)//2 + low

        while not low > high:
            mid = mid = (high - low)//2 + low
            print 'mid....', mid
            if number == list[mid]:
                print 'item is found...'
                return True
            if number > list[mid]:  #search in the right half
                low = mid + 1
            elif number < list[mid]:  #search in the left half
                high = mid -1
        print 'not found...'
        return False

def main():

    number = int(raw_input('Please enter the number to search: '))
    array = raw_input('Please enter the array of integers to search number within it in form of space seperated numbers   ')

    list = map(int,array.split(' '))

    iterBinS = IterativeBinSearch()
    result = iterBinS.iterSearch(list, number)
    print result

if __name__ == '__main__':
    main()
