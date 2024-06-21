# Write a Python program to combine two dictionary adding values for 
# common keys. 

d1 = {'a': 100, 'b': 200, 'c':300} 
d2 = {'a': 300, 'b': 200,'c':400} 

for i in d2:
    if i in d1:
        d2[i]=d2[i]+d1[i]
    else:
        pass
print(d2)


