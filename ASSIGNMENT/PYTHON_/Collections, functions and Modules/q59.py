# Write a Python program to convert degree to radian 



def d_to_r(degree):
    radian=((degree*3.14)/180)
    return radian

degree=float(input("enter degree:"))
print(d_to_r(degree))

    