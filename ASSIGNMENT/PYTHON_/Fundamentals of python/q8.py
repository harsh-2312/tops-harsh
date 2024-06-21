# Write a Python program that will return true if the two given integer values are equal
#  or their sum or difference is 5. 
while(1):
    num1=int(input("enter num1:"))
    num2=int(input("enter num2:"))

    if num1==num2 or num1+num2==5 or num1-num2==5:
        print("true")
    else:
        print("false")
        