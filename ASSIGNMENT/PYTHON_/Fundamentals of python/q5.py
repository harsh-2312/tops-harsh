# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user. 
while(1):
     num=int(input("enter a number:"))
     
     if num %2==0:
        print(num,"is even number")
     else:
        print(num,"is odd number")  

     choice=input("do you want check again(y/n):").lower()  
     if(choice!='y'):
       break
print("thank you")     