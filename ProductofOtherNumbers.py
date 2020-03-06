'''
Function get_products_of_all_ints_except_at_index()
Takes the input list and for each index finds the product of all the numbers except the number in that index
Input: A list of integers
Output: A list of all products
Example:
In = [2, 3, 5, 4]
Out = [3*5*4, 2*5*4, 2*3*5]
Infact the value in each index in the output list is the result of production of all the values in the input list / the value in that index ===>
out[0] = (2*3*5*4) / In[0]
out[1] = (2*3*5*4) / In[1]
out[2] = (2*3*5*4) / In[2]
Pseudocode:

for int in range(len(In)):
    if In[int] == 0:
        production = 0
        break
        
    production = Production * In[int]
    

for index in range(len(In)):
    if In[index] != 0:
        Out.append(production/In[index])
    else:
        Out.append(0)
return Out list
Edges: In[index] = 0 ===> Out[index] = 0
'''

def get_products_of_all_ints_except_at_index(In):
    production = 1
    Out = []
    print(In)
    for index in range(len(In)):
        if In[index] == 0:
            production = 0
            break
        production *= In[index]


    for index in range(len(In)):
        if In[index] != 0:
            Out.append(production // In[index])
        else:
            Out.append(0)

    return Out

    
In = [2, 3, 5, 4]

result = get_products_of_all_ints_except_at_index(In)
print(result)
