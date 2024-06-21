# Write a Python class named Circle constructed by a radius and two 
# methods which will compute the area and the perimeter of a circle  

class circal:
    def __init__(self,radius):
        self.r=radius
        self.pi=3.14

    def area(self):
        return self.pi*self.r**2
    
    def perimeter(self):
        return 2*self.pi*self.r
    
radius=int(input("enter radius:"))
obj=circal(radius)

print("area:",obj.area())
print("peraimetar:",obj.perimeter())

    



