# Write a Python function that takes two lists and returns true if they have 
# at least one common member.  


def common(list1,list2):
    res=False

    for i in list1:
        for j in list2:
            if i==j:
                res=True
    return res

list1=[1,2,3,4]
list2=[6,7,8,9,4]    

print(common(list1,list2))
