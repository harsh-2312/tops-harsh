# Write a Python program to replace last value of tuples in a list. 

tup_list=[(1,2,3),(4,5,6),(7,8,9)]

new=[i[:-1]+(10,) for i in tup_list]

print(new)



# new=[(11,12,13)]

# re=tup_list[:-1]+new

# print(re)

