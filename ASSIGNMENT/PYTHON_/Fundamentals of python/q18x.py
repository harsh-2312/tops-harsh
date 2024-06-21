#  Write a Python function to reverses a string if its length is a multiple of 4.


str1=input("enter string :")
if len(str1)%4==0:
    str2=str1[::-1]
    print(str2)
else:
    print("string not multiple by 4")



