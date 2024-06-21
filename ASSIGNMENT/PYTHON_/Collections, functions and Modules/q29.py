# Write a Python program to unzip a list of tuples into individual lists.  

list_tup=[(1,2,3),(4,5,6),(7,8,9)]

res=list(zip(*list_tup))

print(res)