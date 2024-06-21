# Write a Python program to remove an empty tuple(s) from a list of tuples.  

list_tup=[(1,2,3),(4,5,6),()]

for i in list_tup:
    if (len(i)==0):
        list_tup.remove(i)

print(list_tup)