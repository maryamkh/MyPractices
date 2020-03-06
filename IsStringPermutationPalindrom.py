'''
I have a stirng and I want to check if any permutation of the string is palindrom?
Input: A String
Output:
    True: If the string is palindrom
    False: otherwise
To be palindrom means the string is read the same waye when you reverse it ===> civic is palindrom
===> To see if a string is palindrom I can reverse the strigna and compare it with the origin one
if string == reversed_stringe: string is palindrom
The better and faster and more efficient is to keep the letters of the string in a dictionary as the keys. The values will be the number of redundency of each letter in the string.
A string is plaindrom if all its letters have even redundency with at most one letter with one redundency
Example:
googg ===> A permutation of this string can be palindrom: gogog
gjkjgk ===> A permutation of this string can be palindrom:kgjjgk, kjggjk
onnin ===> No permutation of the string can be palindrom since both letters 'i' and 'o' redundency is one
lkjjkjl ===> lkjjjkl, jkljlkj
Pseudocode:
for letter in string:
    if letter in dic.keys():
        dic[letter] += 1
    else:
        dic[letter] = 1
for number in dic.values:
    if number%2 != 0:
        odd+=1
if odd > 1:
    return False
else:
    return True
    
'''
def IsPermutationPalindrom(string):
    strDic = {}
    odd = 0
    if len(string) == 0:
        return False
        
    for letter in string:
        if letter in strDic.keys():
            strDic[letter] += 1
        else:
            strDic[letter] = 1
    
    for val in strDic.values():
        if val%2 != 0:
            odd += 1
    if odd > 1:
        return False
    else:
        return True
        
string = ""
result = IsPermutationPalindrom(string)
if result:
    print(f'{string} is palindrom')
else:
    print(f'{string} is not palindrom')
    
string = "s"
result = IsPermutationPalindrom(string)
if result:
    print(f'{string} is palindrom')
else:
    print(f'{string} is not palindrom')
string = "mn"
result = IsPermutationPalindrom(string)
if result:
    print(f'{string} is palindrom')
else:
    print(f'{string} is not palindrom')
string = "bb"
result = IsPermutationPalindrom(string)
if result:
    print(f'{string} is palindrom')
else:
    print(f'{string} is not palindrom')
string = "nbgbn"
result = IsPermutationPalindrom(string)
if result:
    print(f'{string} is palindrom')
else:
    print(f'{string} is not palindrom')
string = "pldlep"
result = IsPermutationPalindrom(string)
if result:
    print(f'{string} is palindrom')
else:
    print(f'{string} is not palindrom')
