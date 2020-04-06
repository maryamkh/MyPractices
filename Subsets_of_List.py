#!/usr/bin/python
class SubsetFinder:

    def subsetFinder(self, inputList):
        sortedInput = sorted(inputList)
        subSets = []
        tempArr = []
        for i in range(len(sortedInput)):
            for j in range(i+1,len(sortedInput)+1): #skip item[i:i] =[] ([0:0], [1:1],...) since there will be multiple of them in the resulted list and we cannot remove the redundent ones unless we know their index (which is complecated) ==> add all other subsets to subSets() list and at the end insert item [] at the begining of the list
                tempArr = sortedInput[i:j]
                subSets.append(sortedInput[i:j])
        subSets.insert(0,[])
        return subSets


def main():
    input = input('enter a lsi of integers:   ')
    
    intInput = map(int,input.split(' '))
    print intInput
    #rel_arr = map(int, arr.split(' '))
    finder = SubsetFinder()
    result = finder.subsetFinder(intInput)
    print result

if __name__ == '__main__':
    main()
