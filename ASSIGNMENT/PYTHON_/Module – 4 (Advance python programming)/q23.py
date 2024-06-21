# Write a Python class named Rectangle constructed by a length and 
# width and a method which will compute the area of a rectangle  

class Rectangle:
    
    def __init__(self,length,width):
        self.l=length
        self.w=width

    def rectangle_(self):
        return self.l*self.w
    
length=int(input("enter length:"))
width=int(input("enter width:\n"))

rectangle=Rectangle(length,width)

area=rectangle.rectangle_()
print("area of a rectangle:",area)

