# Write a Python program to convert a list of tuples into a dictionary.

list_tup=[('a',1), ('b',2),('c',3)]

dict1={key:value for key ,value in list_tup }



# for key, value in list_tup:
#     if key in dict1:
#         dict1[key].append(value)
#     else:
#         dict1[key]=[value]

print(dict1)



