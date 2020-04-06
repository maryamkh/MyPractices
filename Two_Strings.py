#!/usr/bin/python
'''
    Compairs 2 string and return 'Yes' if strings have any common char.
    Input: 1- Integer: number of pairs to compair
           2- pairs of strings to compair
    Output: list of Yes/ No based on whether string pais have common chars?
    '''
    
def compair_pairs(all_pairs):
    result = []
    for tuple in all_pairs:
        result.append(compair_string_pair(tuple))
    return result

def compair_string_pair(tuple):
    print tuple
    pos = 0
    for char in tuple[0].lower():
        pos = tuple[1].lower().find(char)
        print 'char...pos:...', char, pos
        if pos >= 0:
            return 'Yes'
    return 'No'


def main():
    tc_count = int(input('enter the numebr of string pairs you want to check:   '))
    string_pair = []
    all_pairs = list()
    
    for pair in range(tc_count):
        string_pair.append(input('please enter 1st string of the pair of strings to compair:   '))
        string_pair.append(input('please enter 2nd string of the pair of strings to compair:   '))
        #print string_pair
        all_pairs.append(tuple(string_pair))
        del string_pair [:]
    #print all_pairs
    
    result = compair_pairs(all_pairs)
    print result

if __name__ == '__main__':
    main()
