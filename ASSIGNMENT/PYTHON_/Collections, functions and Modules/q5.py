# How will you compare two lists?  

#>> Using the sort() Method or the sorted() Function to Compare Lists

# using sort()

list1 = [1,2,3,4,5]
list2 = [5,4,3,2,1]
list1.sort()
list2.sort()
print(list1 == list2)

# using sorted()

list1 = [1,2,3,4,5]
list2 = [5,4,3,2,1]
sorted_list1=sorted(list1)
sorted_list2=sorted(list2)
print(sorted_list1==sorted_list2)


