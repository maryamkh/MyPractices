#!usr/bin/python
class findSubsets:
    
    def subsetSearch(self, list):
        low = 0
        high = 0
        sortedList = sorted(list)
        subSets = []
        self.setsAppend(sortedList, subSets, low, high)

    def setsAppend(self, list, subSets, low, high):
        print 'sorted list...', list
        if high > len(list) and low >= len(list)-1:
            print 'time to return...'
            #subSets.insert(0, [])
            print 'subSets...', subSets
            return subSets

        if high <= len(list):
            print 'in high...'
            subSets.append(list[low:high])
            high += 1
            self.setsAppend(list, subSets, low, high)
        elif low < len(list)-1:
            print 'in low...'
            low += 1
            high = low + 1
            self.setsAppend(list, subSets, low, high)



def main():
    list = raw_input('please enter a list of camma seperated integers:   ')
    intList = map(int, list.split(','))
    fSubsets = findSubsets()
    resultList = fSubsets.subsetSearch(intList)
    print resultList

if __name__ == '__main__':
    main()
