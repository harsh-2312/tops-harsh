""" Write a Python program to check if a number is positive, negative or zero. """


while(1):

    number=int(input("enter a number:"))

    if number>0:
       print("number is positive")
    elif number<0:
       print("number is negative")
    elif number==0:
       print("number is zero") 

    choice=input("do you want check again(y/n):").lower()  
    if(choice!='y'):
       break  

print("thnak you")

        