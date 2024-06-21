

# file= open ("q2.txt",'r')
# file.read('q2.txt')

# # print()


name= """Write a python program to find the longest words.  
 Write a Python program to count the number of lines in a text file.  
 Write a Python program to count the frequency of words in a file. """.split()
print(name)

dict1 = {}

for i in name:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)

# dic1 = {
#     1: 'apple',
#     2: 'mango'
# }

# for i in dic1:
#     print(i)



