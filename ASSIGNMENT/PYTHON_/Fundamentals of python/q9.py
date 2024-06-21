#  Write a python program to sum of the first n positive integers. 

n=int(input("enter num1:"))
sum=0

for number in range(1,n+1):
    
    sum=sum+number
print(sum)

