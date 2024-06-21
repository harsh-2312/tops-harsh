# Write a Python program to remove duplicates from a list.  

list1=[1,2,7,3,2,6,1]

# print(list(set(list1)))
f_list=[]
for i in list1:
    if i not in f_list:
        f_list.append(i)
print(f_list)


