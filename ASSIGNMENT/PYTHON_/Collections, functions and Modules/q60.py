# Write a Python program to calculate the area of a trapezoid 

def area1(base1,base2,heigth):
    return (base1+base2) / 2 * heigth


base1=float(input("enter base1:"))
base2=float(input("enter base2:"))
heigth=float(input("enter heigth:"))

print("area of a trapezoid:",area1(base1,base2,heigth))