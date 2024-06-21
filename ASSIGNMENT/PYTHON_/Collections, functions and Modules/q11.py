# Write a Python function that takes a list and returns a new list with unique 
# elements of the first list.  

def uniqu(list1):
    
    for i in list1:
        if i not in un:
            un.append(i)
    return un


list1=[1,5,8,3,8,7,3,2]
un=[]

print(uniqu(list1))