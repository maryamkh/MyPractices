#!/usr/bin/python
'''
    The string contain only 'A' and 'B'.
    If two adjucent character are smillar, one should be deleted. Ex. AAB==> One A should be deleted
    Number of deletions for each string?
    Input: 1- number of queries(n)     2- n strings to check
    Output: number of deletions for each string
    '''
def alternating_char(string_arr):
    del_list = []
    
    for str in string_arr:
        del_cnt = 0
        A_checked = False
        B_checked = False
        for i in range(2):
            if not A_checked :
                A_checked = True
                repeatity = str.count('A')
                if repeatity:
                    adj_char = 'A'
            
            elif not B_checked:
                B_checked = True
                repeatity = str.count('B')
                if repeatity:
                    adj_char = 'B'
            
            pos = find_char_pos(str, adj_char, repeatity)
            del_cnt = del_cnt + del_frequency(pos, str)
        del_list.append(del_cnt)

    return del_list

def find_char_pos(string, adj_char, occurance):
    pos = []
    start = -1
    for oc in range(occurance):
        start = string.find(adj_char, start+1)
        pos.append(start)
    return pos

def del_frequency(pos, string):
    deletion = 0
        #for i in range(len(string)-1):
    for i in range(len(pos)-1):
        if string[i] == string[i+1]:
            deletion+=1
    return deletion

def main():
    query_count = int(input('enter number of queries: '))
    string_arr = []
    for i in range(query_count):
        in_string = input('enter the string: ')
        string_arr.append(in_string)
        
    result = alternating_char(string_arr)
    print result

if __name__ == '__main__':
    main()
