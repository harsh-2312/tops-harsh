# Write a Python function to check whether a number is in a given range 

def range_(num,start,end):
    if start <= num <= end:
        return True
    return False

num=int(input("enter number:"))
start=int(input("enter starting range:"))
end=int(input("enter ending range:"))

flag=range_(num,start,end)

if flag:
    print("number is in a given range")
else:
    print("number is not a given range")
