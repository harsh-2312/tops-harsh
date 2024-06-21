# Write a Python program to count the frequency of words in a file. 

with open('q10.txt','r') as file:
    file_=file.read().split()

    dec1={}

    for i in file_:
        if i in dec1:
            dec1[i]+=1
        else:
            dec1[i]=1
            
    print(dec1)


# from collections import Counter
# file_name='q10.txt'

# def count_(file_name):
#     try:
#         with open(file_name,'r') as file:
#          return Counter(file.read().split())
#         # return frequency
#     except FileNotFoundError:
#         print("file not found")

# print(count_(file_name))







