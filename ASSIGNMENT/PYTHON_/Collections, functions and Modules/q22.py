# Write a Python program to check whether an element exists within a tuple.  

tup=(1,2,3,4,5,6)

check=int(input("enter number :"))

if check in tup:
    print(f"{check} exists in a tuple")
else:
    print(f"{check} not exists within a tuple")