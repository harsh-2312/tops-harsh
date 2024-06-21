# Write a Python program to get the Factorial number of given number. 

number=int (input("enter a number"))
fact=1


if number< 0:
    print("pliz enter positive number--")
elif number==0:
    print("factorial of 0 is : 1")    
else:    
 for i in range(1,number+1):
    fact=fact*i
 print("factorial:",i,"is",fact)




