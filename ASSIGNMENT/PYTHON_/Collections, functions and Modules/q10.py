# Write a Python program to generate and print a list of first and last 5 
# elements where the values are square of numbers between 1 and 30.  

square=0
list1 = []

for i in range(1,31):
    square=i*i
    list1.append(square)

first=list1[:5]
last=list1[-5:]

print(first + last)


