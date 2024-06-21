# Write a Python program to read first n lines of a file. 

def read(n):
    file=open("q4.txt",'r')
    for i in range(n):
        print(file.readline())
        
n=int(input("enter number:"))
read(n)




