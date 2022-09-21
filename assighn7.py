#7. Write a python program to create three dictionaries, then create one dictionary thatwill contain the other three dictionaries.


from unicodedata import name


d1={'dict_1': {'name':'Sarwar','age':18,'gender':'male'},
   'dict_2': {'name2':'Sarwar2','age2':18,'gender2':'male2'},
   'dict_3': {'name3':'Sarwar3','age3':18,'gender3':'male3'}

}
print(d1['dict_1'])
