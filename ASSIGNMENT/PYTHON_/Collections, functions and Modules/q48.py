# Write a Python function to calculate the factorial of a number (a non negative integer) 

def fac(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

num=int(input("enter number:"))
print(fac(num))

