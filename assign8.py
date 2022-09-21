#8. Write a python program to convert two lists into a dictionary in a way that item fromlist1 is the key and item from list2 is the value.




def Convert(list_1,list_2):
    res_dct = {list_1[i]: list_2[i] for i in range(0, len(list_1))}
    return res_dct
         
# Driver code
list_1=['key_1','key_2','key_3']
list_2=['key_21','key_22','key_23']
print(Convert(list_1,list_2))
