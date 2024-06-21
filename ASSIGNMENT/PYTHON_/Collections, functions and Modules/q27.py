#  Write a Python program to find the repeated items of a tuple.  

tup=(1,2,2,3,4,4,5,5,)
list1=[]

for i in tup:
    if tup.count(i) > 1:
        if i not in list1:
            list1.append(i)
print(list1)