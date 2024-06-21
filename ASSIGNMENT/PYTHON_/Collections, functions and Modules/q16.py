# Write a Python program to check whether a list contains a sub list  

def check(list1,sub):
    res=False
    for i in range(len(list1)):
        if list1[i:i+len(sub)]==sub:
            res=True
    return res

list1=[1,2,3,4,5,6,7]
sub=[4,5,6]

print(check(list1,sub))