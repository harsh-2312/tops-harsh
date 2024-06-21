# Differentiate between append () and extend () methods? 

# append(): The append() method adds a single element to the end of the list 

list1=[1,2,3,4]
# list1.append(5)
list1.append([5,6,7,8])
print(list1)


# extend():the extend() method adds all the elements of an iterable to the end of the list

list1=[1,2,3,4]
list1.extend([5,6,7,8])
print(list1)
