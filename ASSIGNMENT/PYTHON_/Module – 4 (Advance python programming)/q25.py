# find area of traingal

class traingal:
    def __init__(self,base,heigth):
        self.b=base
        self.h=heigth
    
    def area(self):
        return 0.5*self.b*self.h
base=int(input("enter base:"))
heigth=int(input("enter heigth:"))
obj=traingal(base,heigth)

print("area of traingal:",obj.area())



