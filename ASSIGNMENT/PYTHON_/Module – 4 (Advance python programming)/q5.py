# Write a Python program to read last n lines of a file.  

# n=int(input("enter number:"))

# file=open("q4.txt",'r')
# print(file.readlines()[-n:])


def read(n):
    file=open("q4.txt",'r')
    for i in file.readlines()[n:]: 
        print(i)

n=int(input("enter number:"))
read(n)