#  Write a Python program to get the Fibonacci series of given range. 

num=int(input("enter number:"))

a=0
b=1
nextnumber=a+b
print(a,b,end=" ")
for i in range(1,(num+1)-2):
    nextnumber=a+b
    a=b
    b=nextnumber
    print(nextnumber,end=" ")
    
